# VibeCheck — Project Log

> Chronological record of decisions, milestones, and learnings throughout the build.

---

## 2026-07-11 — Project Kickoff

### What happened
- Defined project idea: **VibeCheck** — local-first mood tracker with AI insights
- Created initial planning documents:
  - [PRD.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/PRD.md) — Full product requirements
  - [implementation-plan.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/implementation-plan.md) — 6-phase build plan
  - [project-structure.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/project-structure.md) — Folder layout
  - [memory.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/memory.md) — AI pair programming context

### Key Decisions
| Decision | Reasoning |
|---|---|
| Vanilla JS + Vite | Fastest setup for hackathon; no framework overhead |
| IndexedDB for storage | Structured data, async, better than LocalStorage for logs |
| Local-first, no auth | Privacy is a core value prop; simplifies MVP scope |
| Gemini API for AI | Hackathon is prompt engineering focused; Gemini aligns well |
| Prompts in separate directory | Makes prompt engineering work visible and iterable |

### Current Status
- **Phase:** Planning complete ✅
- **Next:** Phase 1 — Project scaffold and design system

---

## 2026-07-11 — Framework Exploration & User Preferences

### What happened
- Explored **9 framework alternatives** across Python-based, JS-based, and hybrid approaches
- Conducted structured Q&A to nail down user constraints and preferences

### Frameworks Evaluated
| Framework | Category | Verdict |
|---|---|---|
| Streamlit | Python | Fast but limited design customization |
| Reflex | Python → React | Promising but newer ecosystem |
| Flask + HTML/JS | Python hybrid | Full control but more work |
| FastAPI + HTML/JS | Python hybrid | Great API layer, same frontend situation |
| Gradio | Python | Too limited, looks like a demo |
| Taipy | Python | Smaller community |
| Vite + Vanilla JS | JS | Max control, original plan |
| Next.js (React) | JS | Heavy for hackathon timeline |
| Svelte/SvelteKit | JS | Interesting but smaller ecosystem |

### User Preferences (Q&A Results)
| Question | Answer |
|---|---|
| Visual design importance | **MUST look premium and polished** |
| JS comfort level | Somewhat comfortable — prefers Python where possible |
| Data storage strictness | Mostly local, but lightweight cloud DB is fine for demo |
| AI API preference | **Local/free model (Ollama, etc.) — zero cost** |
| Timeline | **4-6 hours (tight)** |
| Deployment | **Must be deployable — needs live URL** |

### Key Constraints Identified
1. ⏱️ Only 4-6 hours → must use the fastest path to polished result
2. 🎨 Premium design is non-negotiable → rules out plain Streamlit/Gradio
3. 🤖 Free/local AI model → need Ollama or free-tier API (changes architecture)
4. 🌐 Must deploy → needs to be web-deployable (Vercel/Netlify/etc.)
5. 🐍 Python preferred → lean toward Python backend where possible

### Current Status
- **Phase:** Framework decision pending ↻
- **Next:** Finalize framework choice based on constraints, update all planning docs

---

## 2026-07-11 — Framework Decision Finalized

### What happened
- Narrowed framework options down to 4 finalists based on constraints
- User selected **FastAPI backend + Vite frontend** (best of both worlds)
- Resolved AI API question: **Gemini API free tier** (not local Ollama — won't work when deployed)
- Deployment target: **Vercel** (free tier)

### Final Architecture Decisions
| Decision | Reasoning |
|---|---|
| **FastAPI** (backend) | Python-native; user's strongest language; handles AI calls and data logic |
| **Vite + Vanilla JS** (frontend) | Maximum design control for premium look; AI writes the JS |
| **Gemini API free tier** | Free quota (15 RPM on Flash); works when deployed; no API cost |
| **Vercel** (deploy) | Free tier; instant deploys; great for JS frontends |
| **Render** (backend deploy) | Vercel is frontend-only; FastAPI needs a backend host like Render free tier |

### Architecture Implications
- **Two services to deploy:** Frontend (Vercel) + Backend (Render)
- Frontend calls backend API for AI features
- Data storage: LocalStorage/IndexedDB on frontend (stays local to user's browser)
- AI calls routed through backend → Gemini API (API key stays server-side, secure)
- CORS configuration needed between Vercel frontend ↔ Render backend

### Alternatives Considered & Rejected
| Option | Why rejected |
|---|---|
| Streamlit | Design ceiling too low for "premium" requirement |
| Reflex | Newer ecosystem; deployment complexity |
| Vite-only (no backend) | Would expose API key in frontend; user prefers Python |
| Ollama (local) | Won't work when deployed — visitors can't access your local model |

### Current Status
- **Phase:** Architecture finalized ✅
- **Next:** Update all planning docs to reflect new architecture, then begin build

---

## 2026-07-11 — Hackathon Guidelines Integration & Major Restructure

### What happened
- Read full hackathon guidelines: evaluation framework, disqualification rules, submission requirements, special awards, schedule
- **Major restructuring** of ALL planning documents to align with scoring criteria
- Added **6 Gen-AI integration points** (up from 3) for maximum "AI tools/services" score
- Added scoring strategy per evaluation parameter (Code Quality, Security, Efficiency, Testing, Accessibility, Problem Alignment)
- Added disqualification prevention measures
- Added submission checklist
- Added special awards targeting strategy
- Created warm-up challenge subfolder: `warmup-cooking-app/`

### Key Decisions
| Decision | Reasoning |
|---|---|
| 6 Gen-AI integration points | Submission requires listing Gen-AI tools/services used — more genuine integrations = stronger entry |
| Security middleware directory | Dedicated CORS, CSP, rate limiting files → target Cyber Sentinel award |
| Accessibility layer (a11y.css + AI chart descriptions) | Target Inclusive Icon award; Gen-AI #6 generates chart descriptions for screen readers |
| pytest + ESLint from start | Testing + Code Quality scores; also helps prevent disqualification (broken features) |
| Warm-up as practice | Warm-up doesn't count for leaderboard, but builds muscle memory for 3-hour main sprint |
| Build fewer working features > more broken ones | Disqualification rule: every feature must work end-to-end |

### Gen-AI Integration Points Defined
| # | Feature | Where |
|---|---|---|
| 1 | Mood Pattern Analysis | `/api/insights` |
| 2 | Journal Theme Extraction | `/api/journal` |
| 3 | Activity Suggestions | `/api/suggestions` |
| 4 | Sentiment Auto-Tag | `/api/analyze-note` |
| 5 | AI Input Validation | Request processing |
| 6 | Chart Accessibility Descriptions | `/api/describe-chart` |
| 7 | AI-Assisted Development | Documented in this log |

### Documents Updated
- [PRD.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/PRD.md) — Added Gen-AI table, scoring strategy, disqualification rules, submission checklist
- [implementation-plan.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/implementation-plan.md) — Rewritten for 3-hour main challenge window + warm-up hour
- [project-structure.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/project-structure.md) — Added security middleware, tests, a11y, scoring annotations
- [memory.md](file:///c:/Users/dsouh/OneDrive/Documents/Projects/Hackathons/PromptWars%20Jul26/docs/memory.md) — Updated stack, Gen-AI map, scoring reference, data schema with sentiment

### Current Status
- **Phase:** Hackathon-aligned planning complete ✅
- **Next:** Build warm-up challenge structure, then prep for hackathon day

---

<!-- 
## TEMPLATE — Copy for new entries

## YYYY-MM-DD — [Title]

### What happened
- ...

### Key Decisions
| Decision | Reasoning |
|---|---|
| ... | ... |

### Issues / Blockers
- ...

### Current Status
- **Phase:** ...
- **Next:** ...

-->
