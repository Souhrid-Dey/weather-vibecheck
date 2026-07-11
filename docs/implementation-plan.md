# VibeCheck — Implementation Plan

> **Aligned to PromptWars Scoring:** Code Quality (HIGH) > Problem Alignment (HIGH) > Security (MED) > Efficiency (MED) > Testing (LOW) > Accessibility (LOW)

## Goal

Build VibeCheck for the PromptWars hackathon: an AI-powered mood tracking web app with **6 Gen-AI integration points**, optimized to score maximum points across all 6 evaluation parameters and contend for special awards.

**Architecture:** FastAPI (Python) + Vite (Vanilla JS/CSS)  
**AI:** Google Gemini API (gemini-2.0-flash, free tier)  
**Deploy:** Vercel (frontend) + Render (backend)  
**Main Challenge Window:** 11:30 AM – 2:30 PM (3 hours)

---

## HACKATHON DAY TIMELINE

```
09:00–10:00  Registration
10:00–10:30  Kickoff & Introduction
10:30–11:30  WARM-UP CHALLENGE (cooking to-do list) ← separate subfolder
11:30–14:30  MAIN CHALLENGE (VibeCheck) ← 3 hours
12:30–13:00  ⭐ Bonus: +2 points if submitted in this window
14:30–15:30  Lunch + Functional Checks
15:30–15:40  Top 10 Announcement
15:40–17:30  Pitching (if Top 10)
17:30–17:45  Winners Announcement
```

---

## PRE-HACKATHON PREP (Do Before Day-Of)

### ✅ Ready before you arrive:
- [ ] Gemini API key obtained from [aistudio.google.com](https://aistudio.google.com)
- [ ] GitHub account logged in, SSH keys configured
- [ ] Node.js + npm installed
- [ ] Python 3.11+ installed, pip working
- [ ] Vite and FastAPI templates tested locally
- [ ] This planning docs folder ready for reference
- [ ] Warm-up challenge subfolder created with structure

---

## WARM-UP CHALLENGE (10:30–11:30, 1 hour)

**Challenge:** AI Cooking To-Do List  
**Location:** `warmup-cooking-app/` subfolder  
**Purpose:** Practice with tools, get environment working, earn Social Node award

See [warmup-cooking-app/docs/](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/warmup-cooking-app/docs/) for the warm-up specific plan.

---

## MAIN CHALLENGE: VibeCheck (11:30–14:30, 3 hours)

### Phase 1: Scaffold + Security Foundation (30 min) — 11:30–12:00

> **Why first:** Code Quality + Security are HIGH/MEDIUM impact. Lay the foundation right.

#### 1.1 — Project Scaffold
- Create `backend/` and `frontend/` directories
- **Backend:** `main.py`, `requirements.txt`, `.env`, `.env.example`
- **Frontend:** `npx -y create-vite@latest ./ --template vanilla` in `frontend/`
- `.gitignore`: node_modules, .env, __pycache__, .venv, dist
- Git init + first commit: `"chore: scaffold project"`
- **Checkpoint:** Both servers start locally

#### 1.2 — Security Setup (Score: Cyber Sentinel)
- CORS middleware in FastAPI (explicit origin allowlist)
- CSP headers middleware
- Rate limiting middleware (slowapi or custom)
- Input sanitization utility (backend)
- `.env` for all secrets — never committed
- **Checkpoint:** Security headers visible in browser dev tools

#### 1.3 — Design System (Score: Code Quality + Accessibility)
- `index.css` with CSS custom properties (design tokens)
- Dark sporty theme with WCAG AA contrast ratios (4.5:1+)
- Import Inter font from Google Fonts
- Semantic HTML template in `index.html` (`<main>`, `<nav>`, `<section>`)
- ARIA landmark roles on all sections
- Focus-visible styles for keyboard navigation
- **Checkpoint:** Design system renders; Lighthouse accessibility check passes

---

### Phase 2: Core Features + Gen-AI Integration (1.5 hrs) — 12:00–13:30

> **Build features that WORK. No faking. Every AI call must be real.**

#### 2.1 — Data Layer + Quick Mood Logger (30 min)
- IndexedDB wrapper with CRUD in `frontend/src/services/db.js`
- Mood emoji selector UI (😤 😟 😐 😊 🔥)
- Optional note input with client-side sanitization
- "Log it" button with animation feedback
- Today's log history below input
- **Checkpoint:** Can log mood, see it, refresh page, data persists

#### 2.2 — FastAPI AI Endpoints (30 min)
- Gemini client wrapper: `backend/services/gemini_client.py`
- **Gen-AI #1:** POST `/api/insights` — mood pattern analysis
- **Gen-AI #2:** POST `/api/journal` — journal note theme extraction  
- **Gen-AI #3:** POST `/api/suggestions` — activity recommendations
- **Gen-AI #4:** POST `/api/analyze-note` — sentiment analysis (auto-tag)
- **Gen-AI #5:** Input validation via AI in request processing
- GET `/api/health` — health check
- All endpoints with proper error handling, docstrings, type hints
- **Checkpoint:** curl/Postman hits each endpoint, gets real Gemini response

#### 2.3 — Frontend AI Integration (30 min)
- API client service: `frontend/src/services/api-client.js`
- Insights tab: "Generate Insights" button → loading animation → display AI response
- Auto-sentiment tagging when user submits a note
- **Gen-AI #6:** Chart description endpoint for screen readers
- Cache AI responses in IndexedDB (efficiency)
- **Checkpoint:** Full flow works: log mood → get AI insights → see results in UI

---

### ⭐ BONUS WINDOW: Submit between 12:30–13:00 for +2 points
> If Phase 2.2 is done by 12:30, do a quick deploy and submit for bonus points.
> You can update the submission after with the final version.

---

### Phase 3: Dashboard + Polish (45 min) — 13:30–14:15

#### 3.1 — Dashboard (30 min)
- Mood trend chart (Chart.js) — line/area chart
- Pattern summary cards (average mood, streak, best day)
- AI-generated chart descriptions for accessibility
- **Checkpoint:** Dashboard shows real data from IndexedDB

#### 3.2 — Code Quality Polish (15 min) — Score: Clean Coder
- Add/review docstrings and comments on all functions
- Run Ruff (Python) and fix any lint issues
- Run ESLint (JS) and fix any lint issues
- Remove any dead code or console.logs
- Verify consistent naming conventions
- **Checkpoint:** Clean lint output on both codebases

---

### Phase 4: Deploy + Submit (15 min) — 14:15–14:30

#### 4.1 — Deploy Backend to Render
- Push to GitHub (public repo, < 10MB)
- Connect Render → GitHub → auto-deploy
- Set `GEMINI_API_KEY` in Render env vars
- Verify `/api/health` returns 200

#### 4.2 — Deploy Frontend to Vercel
- Set `VITE_API_URL` env var → Render backend URL
- `npm run build` + deploy to Vercel
- Verify full flow works on deployed URL

#### 4.3 — Submission
- [ ] README.md with:
  - Brief project description
  - Gen-AI tools/services table (which AI, where in code, purpose)
  - Setup instructions
  - Deployed link
- [ ] GitHub repo: public, < 10MB
- [ ] Deployed link: working
- [ ] End-to-end test: every feature works on deployed version

---

## TIME BUDGET (3-hour main challenge)

| Phase | Time | Clock | Priority |
|---|---|---|---|
| 1: Scaffold + Security | 30 min | 11:30–12:00 | 🔴 Must |
| 2: Core + Gen-AI | 1.5 hrs | 12:00–13:30 | 🔴 Must |
| 3: Dashboard + Polish | 45 min | 13:30–14:15 | 🟡 Should |
| 4: Deploy + Submit | 15 min | 14:15–14:30 | 🔴 Must |
| **Total** | **3 hours** | | |

> ⚠️ **If behind schedule:** Skip Phase 3 dashboard. The AI insights (Phase 2) and clean deployment (Phase 4) are worth more than a chart.

---

## SPECIAL AWARDS STRATEGY

| Award | How to Win | Our Approach |
|---|---|---|
| **Clean Coder** | Highest Code Quality | Linted, documented, modular code from the start |
| **Cyber Sentinel** | Highest Security | CORS, CSP, rate limiting, input sanitization, .env for secrets |
| **Inclusive Icon** | Highest Accessibility | ARIA labels, keyboard nav, contrast, AI chart descriptions |
| **Algorithm Ace** | Highest Efficiency | Caching, lazy loading, async endpoints, minimal bundle |
| **Social Node** | Best "Live Build" thread | Post progress on social media during build |
| **The Human FAQ** | Most questions asked | Ask questions to organizers during the event |

---

## GEN-AI INTEGRATION MAP (for submission)

```
┌─────────────────────────────────────────────────┐
│               VIBECHECK APP                      │
│                                                  │
│  User logs mood + note                           │
│       │                                          │
│       ├──→ Gen-AI #4: Sentiment Analysis         │
│       │    (auto-tag mood from note text)         │
│       │                                          │
│       ├──→ Gen-AI #5: Input Validation           │
│       │    (AI validates/sanitizes input)         │
│       │                                          │
│       └──→ Stored in IndexedDB                   │
│                                                  │
│  User clicks "Get Insights"                      │
│       │                                          │
│       ├──→ Gen-AI #1: Mood Analyzer              │
│       │    (pattern detection, trend summary)     │
│       │                                          │
│       ├──→ Gen-AI #2: Journal Insights           │
│       │    (themes, stressors, triggers)          │
│       │                                          │
│       ├──→ Gen-AI #3: Activity Suggestions       │
│       │    (personalized wellness activities)     │
│       │                                          │
│       └──→ Gen-AI #6: Chart Descriptions         │
│            (accessibility for screen readers)     │
│                                                  │
│  Gen-AI #7: Development Process                  │
│  (Gemini/Copilot used to write & debug code)     │
└─────────────────────────────────────────────────┘
```

---

## RISK MITIGATION

| Risk | Mitigation |
|---|---|
| 3-hour window too tight | Pre-build scaffold + design system; have templates ready |
| Gemini rate limits | Cache responses; throttle; show user-friendly "try again" |
| Render cold start | Health check ping on app load; loading indicator |
| Feature doesn't work | Don't demo it. Build fewer working features > more broken ones |
| Repo > 10MB | No large assets; compress images; .gitignore node_modules/dist |
| Disqualification | Every AI feature makes real API call; test end-to-end before submit |
