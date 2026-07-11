# VibeCheck — Memory (AI Pair Programming Context)

> Persistent context for AI assistant. Updated as decisions are made.
> **Last updated:** 2026-07-11 (Hackathon guidelines integration)

---

## Project Identity

- **App Name:** VibeCheck
- **Purpose:** AI-powered mood tracking + journaling web app
- **Hackathon:** PromptWars Jul 26
- **Core Focus:** Gen-AI integration (6 distinct AI features) + high code quality
- **Timeline:** 1 hr warm-up + 3 hr main challenge

---

## Hackathon Scoring (must influence every decision)

| Parameter | Impact | Our Strategy |
|---|---|---|
| **Code Quality** | 🔴 HIGH | Linted, documented, modular from the start |
| **Problem Alignment** | 🔴 HIGH | 6 Gen-AI integration points, all working end-to-end |
| **Security** | 🟡 MEDIUM | CORS, CSP, rate limiting, input sanitization, .env |
| **Efficiency** | 🟡 MEDIUM | Caching, lazy loading, async, minimal bundle |
| **Testing** | 🟢 LOW | pytest smoke tests, manual e2e checklist |
| **Accessibility** | 🟢 LOW | ARIA, keyboard nav, contrast, AI chart descriptions |

### Disqualification Rules (CRITICAL)
- ❌ No static/hardcoded pages
- ❌ No mock/fake data
- ❌ No hallucinated AI responses — must be real Gemini calls
- ❌ No false positives — every feature must actually work
- ✅ Build fewer working features > more broken ones

---

## Technical Stack

| Layer            | Choice                    | Why (scoring reason)                        |
| ---------------- | ------------------------- | ------------------------------------------- |
| **Backend**      | Python + FastAPI          | User's strongest language; type hints for code quality |
| **Frontend**     | Vite + Vanilla JS         | Minimal bundle (efficiency); full design control |
| **Styling**      | Vanilla CSS               | Dark sporty theme; WCAG AA contrast ratios |
| **AI API**       | Gemini API (free tier)    | gemini-2.0-flash, 15 RPM                   |
| **Storage**      | IndexedDB (frontend)      | Local data; indexed queries (efficiency)    |
| **Charts**       | Chart.js                  | Lazy-loaded (efficiency)                    |
| **Font**         | Inter (Google Fonts)      | Clean, accessible                           |
| **Linting**      | Ruff (Python) + ESLint    | Code quality score                          |
| **Testing**      | pytest                    | Testing score                               |
| **Security**     | CORS + CSP + Rate Limit   | Security score                              |
| **Deploy (FE)**  | Vercel                    | Free tier; instant deploy                   |
| **Deploy (BE)**  | Render                    | Free tier; Python support                   |

---

## Gen-AI Integration Points (6 total)

| # | Feature | Endpoint | Prompt File |
|---|---|---|---|
| 1 | Mood Pattern Analysis | POST `/api/insights` | `mood_analyzer.py` |
| 2 | Journal Theme Extraction | POST `/api/journal` | `journal_insights.py` |
| 3 | Activity Suggestions | POST `/api/suggestions` | `activity_suggest.py` |
| 4 | Sentiment Auto-Tag | POST `/api/analyze-note` | `sentiment.py` |
| 5 | AI Input Validation | Request processing | `ai_validator.py` |
| 6 | Chart Accessibility Desc | POST `/api/describe-chart` | `chart_describer.py` |
| 7 | AI-Assisted Development | Build process | Documented in project-log.md |

---

## User Profile

- **Languages:** Python (strong), SQL (strong), JavaScript (learning with AI)
- **Design preference:** Premium, polished, sporty-minimalist
- **Privacy stance:** Data stays local; cloud DB okay for demo
- **API key:** Needs to get Gemini key from aistudio.google.com

---

## Mood Scale

| Score | Emoji | Label       | Accent Color         |
| ----- | ----- | ----------- | -------------------- |
| 1     | 😤    | Frustrated  | `hsl(0, 80%, 60%)`  |
| 2     | 😟    | Anxious     | `hsl(30, 80%, 55%)` |
| 3     | 😐    | Neutral     | `hsl(210, 15%, 55%)`|
| 4     | 😊    | Good        | `hsl(150, 70%, 50%)`|
| 5     | 🔥    | On Fire     | `hsl(45, 95%, 55%)` |

---

## Data Schema

```javascript
// MoodLog — IndexedDB
{
  id: crypto.randomUUID(),
  timestamp: Date.now(),
  moodScore: 4,
  moodEmoji: "😊",
  note: "Had a great study session",
  tags: ["study", "productive"],
  sentiment: "positive",        // Gen-AI #4 auto-tagged
  sentimentScore: 0.85          // Gen-AI #4 confidence
}
```

---

## Code Conventions (affects Code Quality score)

- **Every function** must have a docstring/comment explaining purpose
- **Python:** snake_case, type hints, Pydantic models
- **JS:** camelCase, JSDoc comments on exports
- **CSS:** `--vibe-{category}-{name}` custom properties
- **No inline styles.** No dead code. No console.logs in production.
- **Error handling:** try/except everywhere, user-friendly messages
- **Lint before commit:** `ruff check .` (Python), `npx eslint .` (JS)

---

## Submission Requirements

- [ ] GitHub repo: **public**, **< 10MB**
- [ ] README.md with: project description, Gen-AI table, setup instructions
- [ ] Deployed link that works (both frontend and backend)
- [ ] Every feature functional end-to-end
- [ ] No test credentials needed (no auth in MVP)

---

## Key Reference Docs

- [PRD.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/PRD.md)
- [implementation-plan.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/implementation-plan.md)
- [project-structure.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/project-structure.md)
- [project-log.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/project-log.md)
- [Hackathon guidelines.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/Hackathon%20guidelines.md)

---

## Session Notes

- *2026-07-11 09:48:* Project initialized. Planning docs created.
- *2026-07-11 09:55:* Explored 9 frameworks. Decided FastAPI + Vite. Gemini free tier.
- *2026-07-11 10:58:* Integrated hackathon guidelines. Restructured all docs for scoring optimization. Added 6 Gen-AI integration points. Created warm-up subfolder.
