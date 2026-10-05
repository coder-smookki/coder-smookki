"""Render a daily profile card from GitHub's contribution calendar.

Uses the GitHub CLI and its GH_TOKEN environment variable. No third-party
image endpoint, extra Python packages, or personal access token is required
in GitHub Actions. On API failure the last successful SVG stays untouched.
"""

import json
import subprocess
from datetime import datetime, time, timedelta, timezone
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LOGIN = "coder-smookki"
QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    repositories(privacy: PUBLIC, ownerAffiliations: OWNER, isFork: false) {
      totalCount
    }
    contributionsCollection(from: $from, to: $to) {
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays { date weekday contributionCount }
        }
      }
    }
  }
}
"""


def fetch_activity():
    now = datetime.now(timezone.utc)
    start = datetime.combine(now.date() - timedelta(days=364), time.min, timezone.utc)
    payload = {"query": QUERY, "variables": {
        "login": LOGIN, "from": start.isoformat(), "to": now.isoformat(),
    }}
    result = subprocess.run(
        ["gh", "api", "graphql", "--input", "-"],
        input=json.dumps(payload), text=True, capture_output=True, timeout=60,
    )
    if result.returncode:
        raise RuntimeError("GitHub API request failed; previous activity card preserved.")
    response = json.loads(result.stdout)
    if response.get("errors") or not response.get("data", {}).get("user"):
        raise RuntimeError("GitHub returned incomplete activity data; previous card preserved.")
    return response["data"]["user"], now.date()


def render_activity(user, updated, compact=False):
    calendar = user["contributionsCollection"]["contributionCalendar"]
    weeks = calendar["weeks"]
    days = [day for week in weeks for day in week["contributionDays"]]
    if not 1 <= len(weeks) <= 54 or not days:
        raise ValueError("Invalid contribution calendar.")
    dates = [datetime.fromisoformat(day["date"]).date() for day in days]
    counts = [day["contributionCount"] for day in days]
    if dates != sorted(set(dates)) or any(b - a != timedelta(days=1) for a, b in zip(dates, dates[1:])):
        raise ValueError("Contribution calendar dates must be unique and consecutive.")
    if any(type(count) is not int or count < 0 for count in counts):
        raise ValueError("Contribution counts must be non-negative integers.")
    if sum(counts) != calendar["totalContributions"]:
        raise ValueError("Contribution total does not match its calendar.")
    for day in days:
        date = datetime.fromisoformat(day["date"]).date()
        if day["weekday"] != (date.weekday() + 1) % 7:
            raise ValueError("Contribution weekday does not match its date.")

    active_days = sum(count > 0 for count in counts)
    longest = streak = 0
    for count in counts:
        streak = streak + 1 if count else 0
        longest = max(longest, streak)

    colours = ["#202630", "#503942", "#815662", "#AF7D8D", "#DBAFBE"]
    width, height = (360, 370) if compact else (960, 350)
    label_size = 10 if compact else 11
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        f'<title id="title">{LOGIN} / GitHub activity</title>',
        f'<desc id="desc">{calendar["totalContributions"]} contributions, {active_days} active days, longest streak {longest} days. Updated {updated.isoformat()} UTC.</desc>',
        f'<style>text{{font-family:Arial,Helvetica,sans-serif}}.label{{font-size:{label_size}px;fill:#98A1AF;letter-spacing:1px}}.small{{font-size:11px;fill:#98A1AF}}</style>',
        f'<rect x=".5" y=".5" width="{width-1}" height="{height-1}" rx="16" fill="#10141C" stroke="#303440"/>',
        '<rect x="28" y="28" width="4" height="18" rx="2" fill="#C6A1AC"/>',
        '<text x="44" y="42" fill="#F1ECEF" font-size="17" font-weight="700">ON THE GRID</text>',
    ]
    if not compact:
        parts.append(f'<text x="932" y="41" class="label" text-anchor="end">UPDATED {updated.strftime("%d %b %Y").upper()} / UTC</text>')
    metrics = [(calendar["totalContributions"], "CONTRIBUTIONS"),
               (active_days, "ACTIVE DAYS"), (longest, "LONGEST STREAK / DAYS"),
               (user["repositories"]["totalCount"], "PUBLIC REPOS / NO FORKS")]
    for i, (value, label) in enumerate(metrics):
        x = 24 + (i % 2) * 174 if compact else 32 + i * 230
        y = 99 + (i // 2) * 73 if compact else 100
        if compact:
            label = ["CONTRIBUTIONS", "ACTIVE DAYS", "LONGEST STREAK / DAYS", "PUBLIC REPOS"][i]
        parts.append(f'<text x="{x}" y="{y}" fill="#F1ECEF" font-size="32" font-weight="700">{value:,}</text>')
        parts.append(f'<text x="{x}" y="{y+24}" class="label">{label}</text>')
        if i and not compact:
            parts.append(f'<path d="M{x-18} 73v55" stroke="#303440"/>')
    divider_y = 211 if compact else 143
    parts.append(f'<path d="M28 {divider_y}H{width-28}" stroke="#303440"/>')
    grid_x, grid_y, step, cell = (34, 247, 5.5, 4.2) if compact else (62, 184, 16, 12)
    if not compact:
        for weekday, label in [(1, "Mon"), (3, "Wed"), (5, "Fri")]:
            parts.append(f'<text x="28" y="{grid_y + weekday*step + 10}" class="small">{label}</text>')
    last_month = None
    last_label_x = -100
    for col, week in enumerate(weeks):
        first = datetime.fromisoformat(week["contributionDays"][0]["date"]).date()
        x = grid_x + col * step
        if first.month != last_month and x - last_label_x >= 44:
            parts.append(f'<text x="{x}" y="{grid_y-14}" font-size="{8 if compact else 11}" fill="#98A1AF">{first.strftime("%b")}</text>')
            last_label_x = x
        last_month = first.month
        for day in week["contributionDays"]:
            count = day["contributionCount"]
            level = 0 if count == 0 else 1 if count <= 2 else 2 if count <= 5 else 3 if count <= 10 else 4
            y = grid_y + day["weekday"] * step
            parts.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" rx="{1 if compact else 3}" fill="{colours[level]}"><title>{escape(day["date"])}: {count} contributions</title></rect>')
    date_range = f'{dates[0].strftime("%d %b %Y")} - {dates[-1].strftime("%d %b %Y")}'
    parts.append(f'<text x="28" y="{307 if compact else 325}" class="small">{date_range}{"" if compact else " / GitHub contribution calendar"}</text>')
    parts.append(f'<text x="{55 if compact else 767}" y="{331 if compact else 325}" class="small" text-anchor="end">Less</text>')
    for i, colour in enumerate(colours):
        parts.append(f'<rect x="{67+i*19 if compact else 779+i*19}" y="{320 if compact else 314}" width="12" height="12" rx="3" fill="{colour}"/>')
    parts.append(f'<text x="{171 if compact else 883}" y="{331 if compact else 325}" class="small">More</text>')
    if compact:
        parts.append(f'<text x="28" y="352" class="label">UPDATED {updated.strftime("%d %b %Y").upper()} / UTC</text>')
    parts.append('</svg>')
    return "\n".join(parts) + "\n"


def main():
    user, updated = fetch_activity()
    cards = [("activity.svg", render_activity(user, updated)),
             ("activity-mobile.svg", render_activity(user, updated, compact=True))]
    for filename, svg in cards:
        target = ROOT / "assets" / filename
        target.parent.mkdir(exist_ok=True)
        temporary = target.with_suffix(".svg.tmp")
        temporary.write_text(svg, encoding="utf-8")
        temporary.replace(target)
    print(f"Activity card updated: {updated.isoformat()}")


if __name__ == "__main__":
    main()
