# VibeCheck — Project Structure

> Optimized for hackathon scoring: Code Quality, Security, Accessibility, and Gen-AI documentation.

```
VibeCheck/
├── README.md                   # Project description + Gen-AI tools table (REQUIRED for submission)
├── .gitignore                  # node_modules, .env, dist, __pycache__, .venv
├── .eslintrc.json              # JS linting config (Code Quality)
│
├── backend/                    # ═══ PYTHON (FastAPI) — AI Logic ═══
│   ├── main.py                 # FastAPI app, CORS, CSP headers, rate limiting
│   ├── requirements.txt        # fastapi, uvicorn, google-generativeai, python-dotenv, slowapi
│   ├── pyproject.toml          # Ruff linter config (Code Quality)
│   ├── .env                    # GEMINI_API_KEY (NEVER committed)
│   ├── .env.example            # Template: GEMINI_API_KEY=your-key-here
│   │
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── insights.py         # POST /api/insights — Gen-AI #1: Mood pattern analysis
│   │   ├── journal.py          # POST /api/journal  — Gen-AI #2: Journal theme extraction
│   │   ├── suggestions.py      # POST /api/suggestions — Gen-AI #3: Activity recommendations
│   │   ├── sentiment.py        # POST /api/analyze-note — Gen-AI #4: Sentiment auto-tag
│   │   └── accessibility.py    # POST /api/describe-chart — Gen-AI #6: Chart descriptions
│   │
│   ├── prompts/
│   │   ├── __init__.py
│   │   ├── mood_analyzer.py    # System prompt + context builder for mood analysis
│   │   ├── journal_insights.py # System prompt + context builder for journal review
│   │   ├── activity_suggest.py # System prompt + context builder for suggestions
│   │   ├── sentiment.py        # System prompt for sentiment analysis
│   │   └── chart_describer.py  # System prompt for chart accessibility descriptions
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini_client.py    # Gemini API wrapper (rate limiting, error handling, caching)
│   │   ├── ai_validator.py     # Gen-AI #5: AI-powered input validation
│   │   └── data_processor.py   # Sanitize/structure incoming mood data
│   │
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── security.py         # CSP headers, CORS config (Security score)
│   │   └── rate_limiter.py     # Rate limiting on AI endpoints (Security score)
│   │
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_routes.py      # Route smoke tests (Testing score)
│   │   └── test_prompts.py     # Prompt builder unit tests (Testing score)
│   │
│   └── utils/
│       ├── __init__.py
│       └── safety.py           # Prompt safety guardrails, content filtering
│
├── frontend/                   # ═══ JAVASCRIPT (Vite) — UI ═══
│   ├── index.html              # Semantic HTML, ARIA landmarks, meta tags (Accessibility)
│   ├── package.json            # vite, chart.js, eslint
│   ├── vite.config.js          # Vite config + API proxy for dev
│   │
│   ├── public/
│   │   ├── favicon.ico
│   │   └── assets/
│   │       └── icons/          # SVG icons (no heavy images — keeps repo < 10MB)
│   │
│   └── src/
│       ├── main.js             # App init, router, keyboard nav setup
│       │
│       ├── styles/
│       │   ├── index.css       # Design tokens, CSS custom properties
│       │   ├── components.css  # Card, button, input styles
│       │   ├── layout.css      # App shell, nav, responsive grid
│       │   ├── animations.css  # Micro-animations, transitions
│       │   ├── themes.css      # Dark mode variables
│       │   └── a11y.css        # Focus indicators, skip links (Accessibility score)
│       │
│       ├── components/
│       │   ├── mood-logger.js  # Mood input + note (ARIA labels on all controls)
│       │   ├── mood-timeline.js# History list (keyboard navigable)
│       │   ├── dashboard.js    # Charts + AI chart descriptions
│       │   ├── journal.js      # Journal view
│       │   ├── insights.js     # AI insights panel
│       │   ├── settings.js     # Export, theme
│       │   └── nav.js          # Tab nav (ARIA roles, keyboard support)
│       │
│       ├── services/
│       │   ├── db.js           # IndexedDB CRUD (with indexes for efficiency)
│       │   ├── api-client.js   # Fetch wrapper with error handling
│       │   ├── analytics.js    # Computed stats (averages, streaks)
│       │   └── export.js       # JSON export/import
│       │
│       └── utils/
│           ├── date-helpers.js # Date formatting
│           ├── mood-config.js  # Emoji/label/color config
│           └── sanitize.js     # Client-side input sanitization (Security)
│
├── docs/                       # ═══ PLANNING & DOCUMENTATION ═══
│   ├── PRD.md                  # Product requirements + Gen-AI integration table
│   ├── implementation-plan.md  # Hackathon-day build plan with time blocks
│   ├── project-structure.md    # This file
│   ├── project-log.md          # Build log + AI tools usage log
│   └── memory.md               # AI pair programming context
│
└── scripts/
    └── seed-demo-data.js       # Realistic demo data seeder
```

---

## Architecture Diagram

```
┌──────────────────────────────────────────────────────────┐
│                    USER'S BROWSER                         │
│                                                          │
│  ┌────────────┐  ┌──────────┐  ┌──────────┐  ┌───────┐  │
│  │ Mood Logger│  │Dashboard │  │ Journal  │  │Insights│  │
│  └─────┬──────┘  └────┬─────┘  └────┬─────┘  └───┬───┘  │
│        │              │             │             │       │
│  ┌─────┴──────────────┴─────────────┴─────────────┴───┐  │
│  │           IndexedDB (all data stays local)          │  │
│  └─────────────────────┬──────────────────────────────┘  │
│                        │ HTTPS (only on user action)     │
└────────────────────────┼─────────────────────────────────┘
                         ▼
┌──────────────────────────────────────────────────────────┐
│              FASTAPI BACKEND (Render)                     │
│                                                          │
│  ┌─── Security Layer ──────────────────────────────────┐ │
│  │ CORS · CSP Headers · Rate Limiting · Input Sanitize │ │
│  └─────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌─── Gen-AI Endpoints ───────────────────────────────┐  │
│  │ #1 /insights    #2 /journal      #3 /suggestions  │  │
│  │ #4 /analyze-note  #5 AI Validation  #6 /describe  │  │
│  └──────────────────────┬─────────────────────────────┘  │
│                         │                                │
│  ┌─── Prompt Engine ────┴───────────────────────────┐    │
│  │ System prompts · Context builders · Parsers      │    │
│  │ Safety guardrails · Few-shot examples            │    │
│  └──────────────────────┬───────────────────────────┘    │
└─────────────────────────┼────────────────────────────────┘
                          ▼
                ┌──────────────────┐
                │  Google Gemini   │
                │  gemini-2.0-flash│
                │  (free tier)     │
                └──────────────────┘
```

---

## Scoring-Aligned Design Decisions

### Code Quality (HIGH IMPACT)
- **Modular structure:** Each file has a single responsibility
- **Linting:** Ruff for Python, ESLint for JS — run before every commit
- **Docstrings:** Every function documented with purpose, params, returns
- **`__init__.py` files:** Proper Python packaging
- **Type hints:** FastAPI uses Pydantic models for request/response validation

### Security (MEDIUM IMPACT)
- **Dedicated `middleware/` directory** for security concerns
- **API key isolation:** `.env` only, never in code or frontend
- **Input sanitization:** Both client (`sanitize.js`) and server (`data_processor.py`)
- **Rate limiting:** Prevents AI endpoint abuse

### Efficiency (MEDIUM IMPACT)
- **IndexedDB indexes** for fast queries by date/mood
- **AI response caching** in gemini_client.py
- **Vanilla JS** — minimal bundle, no framework overhead
- **Lazy chart loading** — Chart.js only imported on dashboard tab

### Accessibility (LOW IMPACT)
- **Dedicated `a11y.css`** for focus indicators and skip links
- **ARIA labels** on every component
- **AI chart descriptions** — Gen-AI #6 generates natural-language summaries
- **Semantic HTML** throughout

### Testing (LOW IMPACT)
- **`tests/` directory** in backend with pytest
- **Smoke tests** for all routes
- **Prompt builder tests** to verify context serialization

---

## Deployment Strategy

| Service | Host | URL | Size |
|---|---|---|---|
| Frontend | Vercel | `vibecheck.vercel.app` | < 5MB build |
| Backend | Render | `vibecheck-api.onrender.com` | < 5MB |
| **Total repo** | GitHub | Public | **< 10MB** ✅ |

---

## File Naming Conventions

| Language | Convention | Example |
|---|---|---|
| Python files | `snake_case.py` | `gemini_client.py` |
| Python vars/funcs | `snake_case` | `build_context()` |
| JS files | `kebab-case.js` | `api-client.js` |
| JS vars/funcs | `camelCase` | `getMoodLogs()` |
| CSS files | `kebab-case.css` | `a11y.css` |
| CSS properties | `--vibe-{cat}-{name}` | `--vibe-color-accent` |
