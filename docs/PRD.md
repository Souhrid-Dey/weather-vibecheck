# VibeCheck — Product Requirements Document (PRD)

> **Hackathon:** PromptWars Jul 26 — Prompt Engineering & Building with AI  
> **Scoring Focus:** Code Quality (HIGH) > Problem Alignment (HIGH) > Security (MED) > Efficiency (MED) > Testing (LOW) > Accessibility (LOW)

---

## 1. Project Overview

**App Name:** VibeCheck  
**Tagline:** *Log your vibe. Know yourself.*  
**Type:** AI-powered web application (Gen-AI focused)

VibeCheck is a **mood-tracking and journaling web app** where users log their emotional state with optional notes throughout the day. An **AI-powered mood analyzer** surfaces patterns, trends, and actionable insights via a clean dashboard. The app uses **6 distinct Gen-AI integration points** to demonstrate depth of AI utilization across the product.

### Core Value Proposition
- **For the user:** A dead-simple way to check in with yourself, backed by AI that genuinely helps you understand and improve your emotional health.
- **For the hackathon:** Demonstrates comprehensive Gen-AI usage across 6 integration points — not just one API call, but AI woven throughout the product experience.

### Gen-AI Tools & Services Used

| # | Gen-AI Integration | Where in Project | Purpose |
|---|---|---|---|
| 1 | **Gemini API — Mood Analysis** | `backend/prompts/mood_analyzer.py` → `/api/insights` | Analyzes mood log patterns, generates personalized trend summaries |
| 2 | **Gemini API — Journal Insights** | `backend/prompts/journal_insights.py` → `/api/journal` | Reads journal notes, extracts themes, stressors, positive triggers |
| 3 | **Gemini API — Activity Suggestions** | `backend/prompts/activity_suggest.py` → `/api/suggestions` | Recommends wellness activities grounded in user's actual mood data |
| 4 | **Gemini API — Sentiment Analysis** | `backend/services/sentiment.py` → `/api/analyze-note` | Auto-tags mood entries from note text, detects emotional tone |
| 5 | **Gemini API — Input Validation** | `backend/services/ai_validator.py` → input processing | AI-powered content validation and sanitization of user inputs |
| 6 | **Gemini API — Accessibility Descriptions** | `backend/routes/accessibility.py` → `/api/describe-chart` | Generates natural-language descriptions of charts for screen readers |
| 7 | **AI Coding Assistants** | Development workflow | Gemini / Copilot used to generate code, debug, and iterate (documented in project-log.md) |

---

## 2. Level & Type

| Attribute       | Value                                              |
| --------------- | -------------------------------------------------- |
| **Difficulty**  | Medium                                             |
| **Type**        | AI Web Application, Health & Wellness              |
| **Target User** | Anyone tracking moods — students, professionals, wellness enthusiasts |

---

## 3. Skills / Tools Required

| Category            | Technologies                                                       |
| ------------------- | ------------------------------------------------------------------ |
| **Backend**         | Python 3.11+ / FastAPI (AI logic, API endpoints, Gemini calls)     |
| **Frontend**        | HTML5, CSS3 (vanilla), JavaScript (ES6+)                           |
| **Frontend Bundler**| Vite (lightweight, fast dev server)                                |
| **Styling**         | Custom CSS — sporty/minimalist design system, dark mode            |
| **AI / LLM**        | Google Gemini API (gemini-2.0-flash) — 6 integration points       |
| **Data Storage**    | IndexedDB (frontend, all user data on-device)                      |
| **Charts**          | Chart.js (mood trend visualization)                                |
| **Testing**         | pytest (backend), basic JS tests (frontend)                        |
| **Linting**         | Ruff (Python), ESLint (JS)                                         |
| **Security**        | CORS, CSP headers, input sanitization, rate limiting               |
| **Accessibility**   | ARIA labels, keyboard navigation, contrast ratios, screen reader   |
| **Deploy (FE)**     | Vercel (free tier)                                                 |
| **Deploy (BE)**     | Render (free tier)                                                 |
| **Version Control** | Git + GitHub (public repo, < 10MB)                                 |

---

## 4. Key Features & Milestones

### Milestone 1: Core Mood Logging (MVP) — 🔴 MUST
> *The atomic unit — every feature must genuinely work end-to-end.*

- [ ] **Quick Vibe Log:** Tap to log mood from emoji set (😤 😟 😐 😊 🔥)
- [ ] **Optional Note:** Attach a short text note to any vibe log
- [ ] **AI Sentiment Auto-Tag:** *(Gen-AI #4)* Gemini analyzes note text, auto-detects emotional tone
- [ ] **Vibe History:** Scrollable timeline of all past logs
- [ ] **Local Storage:** All logs in IndexedDB — works offline
- [ ] **Input Validation:** *(Gen-AI #5)* AI validates and sanitizes user inputs

### Milestone 2: Dashboard & Analytics — 🟡 SHOULD
> *See the patterns your brain can't.*

- [ ] **Mood Trend Chart:** Line/area chart of mood over time (Chart.js)
- [ ] **Pattern Cards:** Average mood, streaks, best day, most common vibe
- [ ] **Chart Accessibility:** *(Gen-AI #6)* AI generates natural-language chart descriptions for screen readers
- [ ] **Filterable Views:** Filter by date range, mood level, keyword

### Milestone 3: AI-Powered Insights — 🔴 MUST (Hackathon Core)
> *The prompt engineering showcase — 3 distinct AI features.*

- [ ] **Mood Analyzer:** *(Gen-AI #1)* AI reads logs, generates personalized mood summary with patterns
- [ ] **Journal Insights:** *(Gen-AI #2)* AI reads notes, surfaces themes, stressors, positive triggers
- [ ] **Activity Suggestions:** *(Gen-AI #3)* AI recommends 3-5 concrete activities grounded in user data
- [ ] **Structured Prompts:** System prompts with role, context injection, output format, safety guardrails
- [ ] **Real API Calls:** Every AI feature makes genuine Gemini API calls (no mocking, no hardcoding)

### Milestone 4: Journal View — 🟡 SHOULD
> *Your notes, reframed as a journal.*

- [ ] **Journal Mode:** Chronological view of all notes as a clean journal
- [ ] **Search:** Search notes by keyword
- [ ] **AI Journal Summary:** Weekly summary generated by Gemini

---

## 5. Hackathon Scoring Strategy

### Code Quality (HIGH IMPACT) — Target: Clean Coder Award
- Well-structured, modular code with clear separation of concerns
- Meaningful comments and docstrings on all functions
- Consistent naming conventions (Python: snake_case, JS: camelCase)
- Proper error handling with try/except and user-friendly error messages
- No dead code, no commented-out code
- Linted: Ruff (Python), ESLint (JS)

### Problem Statement Alignment (HIGH IMPACT)
- Every feature addresses "AI-powered mood tracking and insights"
- 6 distinct Gen-AI integration points (documented in submission)
- Real working AI calls — no mocks, no hardcoded responses
- End-to-end functional: log → dashboard → AI insights → journal

### Security (MEDIUM IMPACT) — Target: Cyber Sentinel Award
- API key NEVER in frontend code — backend only, via `.env`
- CORS configured with explicit origin allowlist
- Content Security Policy (CSP) headers
- Input sanitization on both client and server
- Rate limiting on AI endpoints (prevent abuse)
- XSS prevention (escape all user-rendered content)
- `.env` in `.gitignore` — credentials never committed

### Efficiency (MEDIUM IMPACT) — Target: Algorithm Ace Award
- Lazy loading of dashboard charts (only load Chart.js when needed)
- AI response caching in IndexedDB (don't re-call for same data)
- Debounced input fields
- Minimal bundle size (vanilla JS, no heavy frameworks)
- Efficient IndexedDB queries with indexes
- Backend: async endpoints in FastAPI

### Testing (LOW IMPACT)
- pytest for backend routes and prompt builders
- Basic smoke tests for frontend (DOM renders, click handlers)
- End-to-end: manual test checklist

### Accessibility (LOW IMPACT) — Target: Inclusive Icon Award
- ARIA labels on all interactive elements
- Keyboard navigation support (tab through all controls)
- Color contrast ratios meeting WCAG AA (4.5:1 minimum)
- Screen reader support: AI-generated chart descriptions *(Gen-AI #6)*
- Focus indicators on all interactive elements
- Semantic HTML (`<main>`, `<nav>`, `<section>`, `<article>`)

---

## 6. Submission Checklist

- [ ] GitHub repo is **public** and **< 10MB**
- [ ] Deployed project link works (Vercel frontend + Render backend)
- [ ] Brief project description in README.md
- [ ] Gen-AI tools/services table in README.md (which AI, where, why)
- [ ] All features work end-to-end (no mocks, no hardcoding)
- [ ] Test credentials provided if auth is used
- [ ] Project log documents AI tools used in development process

---

## 7. Disqualification Prevention

> ⚠️ **Every feature must genuinely work. Build fewer features that work > more features that don't.**

| Rule | Our Mitigation |
|---|---|
| No static/hardcoded pages | Every page has real logic, real data, real AI calls |
| No mock/fake data | All AI responses come from live Gemini API calls |
| No hallucinated AI responses | Backend makes genuine API calls; error handling for failures |
| No false positives | Test every feature end-to-end before submission |

---

## 8. Out of Scope (for Hackathon)

- User authentication / cloud sync (adds complexity, risks disqualification if broken)
- Social features / sharing
- Push notifications
- Native mobile app (web-only)
- Medical-grade mood assessment
- Calendar / Fitbit integrations (stretch only if time permits)
