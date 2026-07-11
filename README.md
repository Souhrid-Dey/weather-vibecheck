# Weather VibeCheck ⛈️

*Monsoon Preparedness & Citizen Assistance — PromptWars Jul26 Hackathon Submission*

**Weather VibeCheck** is a Gen-AI-powered web application that helps citizens survive and navigate severe monsoon weather. Rather than just giving generic checklists, the app uniquely adapts its guidance based on the user's **anxiety level**, generates offline-capable **pantry survival meal plans**, translates **SOS emergency alerts** into multiple local languages (Hindi, Marathi), and provides **commute risk analysis**.

## 🚀 Live Links
- **Unified Vercel Deployment:** Configured via `vercel.json`
- **App URL:** [https://weather-vibecheck.vercel.app](https://weather-vibecheck.vercel.app)
- **GitHub Repo:** `[Remember to add your public repo URL here]`

## 🤖 Gen-AI Integration Points (Hackathon Requirement)
We leveraged Google's Gemini 2.0 Flash (`gemini-2.0-flash`) via the `google-generativeai` SDK, forcing strict JSON structural outputs for robust frontend integration.

| Feature Area | AI Prompt Strategy | Purpose |
|--------------|--------------------|---------|
| **1. Preparedness Plan** | Anxiety-Aware Tone Modifier | Generates a custom checklist. If the user marks anxiety as "High", the AI uses empathetic language and breaks tasks into micro-steps to prevent panic. |
| **2. Pantry Survival** | Constraint-based Meal Planning | User inputs fridge contents; AI outputs a 3-day no-cook/low-cook meal plan with rationing tips for power outages. |
| **3. Commute Risk** | Route Hazard Analysis | Assesses flood risks between Point A and B, giving a definitive "Go / No-Go" decision. |
| **4. SOS Broadcaster** | Multilingual SMS Condensation | Converts complex distress situations into under-160-character SMS templates in English, Hindi, and Marathi. |

## 🛠️ Architecture & Offline Capabilities
- **Frontend:** Vite + Vanilla JS + CSS (Emergency High-Contrast Theme).
- **Backend:** FastAPI (Python).
- **Security:** SlowAPI rate limiting (5 req/min on endpoints) + CSP Headers (Targeting **Cyber Sentinel** Award).
- **Offline Mode:** Uses browser **IndexedDB** to silently cache AI responses. If the user loses internet during a storm, their generated preparedness plan remains accessible. (Targeting **Algorithm Ace** Award).

## 🏃 Running Locally
1. Clone the repo and `cd` into the project.
2. **Backend:**
   ```bash
   cd backend
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   # Ensure .env has GEMINI_API_KEY
   uvicorn main:app --reload --port 8000
   ```
3. **Frontend:**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
