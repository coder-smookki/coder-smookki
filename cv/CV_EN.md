<p><a href="../README.md">← Profile</a> · <a href="CV_RU.md">Русский</a> · <a href="Kirill_Ilyin_CV_EN.pdf">Download PDF</a></p>

# Kirill Ilyin

**Fullstack Developer / AI Developer / Mobile Developer**

Saint Petersburg, Russia · +7 951 981-30-33<br />
[smookki@yandex.ru](mailto:smookki@yandex.ru) · [Telegram: @smokkkkiiii](https://t.me/smokkkkiiii) · [GitHub: coder-smookki](https://github.com/coder-smookki)

I build Python backends and mobile applications with Kotlin, Swift and Flutter. Co-founder of F-Rent, an item rental marketplace, with app releases on the App Store and RuStore. In 2026, I led the team that won first place in the IT track of PRO STROY 4.0 and won first place at Nuclear IT Hack 2026. Founder of the Lumnex IT agency.

## Experience

### Founder / Lumnex IT Agency

**June 2026 - Present**

- Deliver IT projects for businesses, public-sector organisations and individual clients, from analysing client processes to launching the product.
- Build a service that matches an uploaded CV with leads and job opportunities on popular platforms.

### Co-founder and CEO / F-Rent

**2026 - Present** · [f-rent.ru](https://f-rent.ru/)

- Develop a peer-to-peer item rental platform: owners set rental terms and deposits; bookings range from a few hours to several months.
- Implement business logic and integrations in Python with MySQL. The website backend uses JavaScript; mobile apps use Kotlin and Swift, with some Java code.
- Integrated T-Bank online payment processing and a cash-register system for fiscal receipts. Released the app on the App Store and RuStore in May 2026.
- Set up the team's GitHub workflow: branches, code reviews, GitHub Actions CI/CD and automated tests.

**Stack:** Python, MySQL, Kotlin, Swift, Java, JavaScript, Docker, GitHub Actions.

### IT Specialist / TANA HOMITZ

**April 2026 - Present** · T. A. Tsimokh, sole proprietor · [tanahomitz.com](https://tanahomitz.com/)

- Develop a premium clothing brand's Tilda online store: catalogue, cart, payments, collection pages and journal. Launched a Telegram Mini App on Unitee.
- Configured SEO in Yandex Webmaster: search impressions rose from single digits to 200+, with 65 clicks, during July-August 2026.

### Developer / Moscow Exchange Trading Bot

**February 2026 - Present**

- Built a Telegram bot for stock monitoring and buy, additional-buy and sell signals. Settings include RSI, take-profit, trailing stop and three additional-buy stages.
- Implemented five daily market checks across 37 tickers, PnL, cost and loss calculations, a virtual portfolio and per-ticker profit charts.

**Stack:** Python, aiogram, MOEX ISS API.

### Developer / PRONALOG

**February - August 2026** · PRONALOG LLC · [pronaloginfo.ru](https://pronaloginfo.ru/)

- Built a Telegram and MAX bot for legal questions from Russian and international clients, together with an admin panel and payment acceptance.
- Created an accounting-services landing page for Wildberries and Ozon sellers in August 2026.

### Developer / Taxi Booking Service in MAX

**March - August 2026** · Miass and Tarusa

- Built three connected bots for an operating taxi service: passenger, dispatcher and driver bots.
- Implemented order hand-off from passenger to dispatcher, driver assignment and trip display in the driver's bot.

**Stack:** Python, MAX Bot API, maxo.

### Developer / Gazstroyprom

**April - May 2026** · [gsprom.ru](https://gsprom.ru/)

- Developed an employee file-sharing service with uploads, access permissions, external links, DLP checks and antivirus scanning for every file.

**Stack:** Python, TypeScript.

### Mentor / Khantathon, Junior Track

**2024 - Present** · Surgut, Khanty-Mansi Autonomous Okrug

- Mentored 8 teams: problem definition, architecture, code reviews and preparation for project presentations.

## Hackathons and Case Competitions

### Nuclear IT Hack 2026 / Developer / First Place

**November 2026** · Team Mugsize · "Neuro-stenographer" case (Hex.team) · [GitHub](https://github.com/coder-smookki/NuclearItHack)

- Built Skvor, an Android app that transcribes conversations entirely offline: the app has no `INTERNET` permission and all models ship inside the APK.
- Speech recognition (GigaAM v3), speaker diarization, timestamps, a JSON file and a meeting summary from the on-device Qwen3-0.6B language model.
- Measured: WER 7.01 on a Russian podcast, DER 10.07 on 49 labelled files; a 3-minute recording is processed in 88 seconds on a Snapdragon 662.

**Stack:** Kotlin, Jetpack Compose, sherpa-onnx, GigaAM v3, Silero VAD, llama.cpp, Docker, GitHub Actions.

### Cyber 102 / Team Lead / Developer

**November 2026** · Ufa · Team AIst · KST ENERGO ENGINEERING case · [GitHub](https://github.com/coder-smookki/AIst-CyberHack102)

- Built KST Vizor, an AR assistant for equipment inspectors: the unit is identified from its nameplate, and parts and external defects are highlighted over the live camera image alongside sensor readings and remaining life.
- Three recognition models (YOLOv9-tiny, RF-DETR nano) run on the plant server's CPU without internet; on unseen photos, part detection precision is 95% with 0 false defects on 29 photos of healthy equipment.
- 26 diagnostic rules using the client's thresholds, five roles with a security log, PDF and Excel reports, and a web panel with an assistant that runs commands only after confirmation; 552 automated server tests.

**Stack:** Flutter, Python, FastAPI, ONNX Runtime, Next.js, Docker.

### RLT.hack / Developer / 6th Place of 19

**October 2026** · Roseltorg University · Team 404: Loss not found · [GitHub](https://github.com/coder-smookki/RLT.hack-404LossNotFound)

- Built a supplier-matching web app for procurement: from two CSV files it ranks candidate suppliers for each lot, with per-item evidence, a confidence score and a company profile.
- Hybrid retrieval with the nnPU35 ranker: NDCG@10 of 0.329 versus 0.261 for the baseline formula.

**Stack:** Python, Django, PostgreSQL, React, TypeScript, Docker.

### DomPulse / Frontend and Release

**September 2026** · VK Education and MAX hackathon · [GitHub](https://github.com/coder-smookki/VkEducation-and-MessangerMax-Hackathon-2026)

A Mini App and bot in the MAX messenger for residents' requests: work reports are linked to specific items of a request, and the author confirms the result. Responsible for the interface, MAX styling, builds and release.

**Stack:** React, TypeScript, Java, Spring Boot, PostgreSQL, Python, FastAPI.

### PRO STROY 4.0 / Team Lead / First Place in the IT Track

**August 2026** · Team AIst · Gazstroyprom · Saint Petersburg · [GitHub](https://github.com/coder-smookki/GSP-Project-AIst)

- Built a corporate-regulation search system running on our own servers without external APIs.
- Integrated a multi-agent graph with the interface, including streaming answers and displaying sources before the first token.
- Configured tracing with OpenTelemetry and OpenLIT; identified a query-parsing issue in structured output.
- Implemented relevance filters and numerical checks against sources: 10 correct refusals out of 10.
- Ran an A/B test on 121 questions: replacing `gpt-oss:20b` with `gemma4:26b` reduced median response time from 23.2 seconds to 9-12 seconds.

**Case results:** hit@5 - 0.926; MRR - 0.851; "not found" - 7.4%; 654 automated tests.<br />
**Stack:** Python, LangGraph, Chainlit, Qdrant (dense + BM25 + RRF), Ollama, PostgreSQL, OpenLIT, Prefect, Docker.

### SSD Video Conferencing Platform / Developer / Second Place

**December 2024** · Khantathon-2025 · Surgut · [GitHub](https://github.com/coder-smookki/Hackathon-SSD-2024)

Built a video conferencing platform using the Khanty-Mansi regional API for a regional government department. Integrated it into Telegram through a WebApp so users could join meetings without a separate application.

### untitled.py AI Assistant / Developer / First Place

**December 2023** · Khantathon-2024 · Surgut · Client: Recifra agency

The assistant analyses sentiment in Telegram conversations, extracts tasks and displays them in a web dashboard for managers. The agency adopted the solution in its operations.

### Games for Yandex Alice / Developer

**2022 - 2023** · [Lord of the Empire on GitHub](https://github.com/coder-smookki/YandexSkill_Game_Lord_of_the_Empire)

"Mafia War" won first place and the Grand Prix at the Yandex Textbook and Alice hackathon on 7 May 2022 (team SSD). "Lord of the Empire" won first place at a Yandex hackathon in 2023.

### SSD QR Code and Link Checker / Developer / Third Place

**February 2023** · devHACK · Rostov-on-Don · [Website](https://github.com/coder-smookki/QRCode-website) · [Bot](https://github.com/coder-smookki/Telegram-Bot-QRcode)

Implemented URL and QR code checks using VirusTotal and custom XSS checks. Awarded a third-degree diploma.

## Additional Achievements

- Winner's diploma at AI Challenge, an international artificial intelligence hackathon.
- Prize winner in the Cybersecurity track of the Scientific Universe competition (2023).

## Projects

### Funora / Multi-language SDK and Framework for FunPay

**2026 - Present** · Open source · Apache-2.0 · [GitHub](https://github.com/Funora-Develop/Funora)

Designing the specification and Python reference implementation. Shared contracts for models, events and errors; common test vectors across SDKs. A consistent model: `Client`, services, events, router and filters. Planned implementations include TS/JS, Java, .NET, C++ and C. The project is in the design stage; no package has been released yet.

### Habit+ / Mini App and Bot in MAX

**November 2025** · VK Education and MAX hackathon · [GitHub](https://github.com/coder-smookki/VkEducation-and-MessangerMax-Hackathon)

Productivity as a game: a character grows with completed tasks, goals and Pomodoro sessions. Python, FastAPI, PostgreSQL, Redis, React.

### Ocean Wallet / Cryptocurrency Wallet with Payment Features

**2026 - Present**

Developing a cross-platform Flutter app. Screens and automatic wallet creation are implemented; business logic is in progress. Preparing an MVP and an investment application in the UAE.

### Petersburg Energy-Saving Company

**2026** · [GitHub](https://github.com/coder-smookki/Test-Task-PESK)

Completed a developer test assignment and received a job offer.

### PyGame-DOOM-1993 / 2.5D Shooter

**2022 - 2025** · [GitHub](https://github.com/coder-smookki/PyGame-DOOM-1993)

Python and Pygame personal project with ray casting, textures, sprites, collisions, weapons and sound. Other personal projects include an [Alice skill built at an ITMO hackathon](https://github.com/coder-smookki/YandexSkill_ITMO).

## Skills

**Python - primary language:** FastAPI, Django / DRF, Flask / Starlette, aiogram, python-telegram-bot, vkbottle / vk_api, MAX Bot API, MOEX ISS API, maxo, discord.py, SQLAlchemy, Alembic, Pydantic, asyncio, aiohttp, Celery, Redis-py, requests, httpx, BeautifulSoup, Scrapy, NumPy, Pandas, Matplotlib, scikit-learn, OpenCV, Pillow, pytest, Poetry, Ruff, PyQt6, Pygame.

**LLMs and agents:** LangGraph, RAG, Adaptive / Corrective RAG, multi-agent graphs, Qdrant, dense + BM25 + RRF, reranking, Ollama, Chainlit, OpenLIT / OpenTelemetry, Prefect.

**AI-assisted development:** Claude Code, Codex, task decomposition for agents, multi-agent runs, prompts and context, generated-code reviews, automated testing and A/B tests.

**Java:** Spring Boot, Spring MVC, Spring Data JPA, Hibernate, JAX-RS, Maven / Gradle, JUnit.

**Mobile:** Kotlin, Jetpack Compose, Ktor, Swift, SwiftUI / UIKit, Flutter / Dart, Bloc / Provider / Dio.

**Other languages:** JavaScript / TypeScript, Go, C++, C - syntax, algorithms and procedural programming. Familiar with Express, React, Gin, Fiber, Qt, STL, POSIX, SDL2.

**Data and DevOps:** PostgreSQL, MySQL, SQLite, MongoDB, Redis; SQL, indexes, migrations; Docker, Docker Compose, Git / GitHub, CI/CD, Linux, Nginx, Postman / Swagger.

**Tools and languages:** Figma, Photoshop, MS Office. Russian - native; English - A1.

## Education

### D. F. Ustinov Baltic State Technical University "Voenmekh"

**2024 - 2028** · Saint Petersburg

Bachelor's degree in Software Engineering (09.03.04), third year, in progress.

### Yandex Lyceum

**2021 - 2023**

Industrial Programming Fundamentals (2022-2023), with honours; Python Programming (2021-2022).

### Yandex Dialogs and ITMO

**March 2023**

Theory and practical training in developing voice-assistant applications as part of the Alice and ITMO online hackathon (4-26 March 2023).

---

<sub>Updated 16 November 2026. Experience and results are based on the supplied CV; 2025-2026 hackathons were checked against their public repositories.</sub>
