<div align="center">
  <h1>⛈️ Weather VibeCheck</h1>
  <p><strong>Intelligent Monsoon Preparedness & Citizen Assistance App</strong></p>
  <p><em>A submission for the PromptWars Jul26 Hackathon</em></p>
</div>

---

## 🚀 Quick Links
- **Live Application:** [https://weather-vibecheck.vercel.app](https://weather-vibecheck.vercel.app)
- **GitHub Repository:** [https://github.com/Souhrid-Dey/weather-vibecheck](https://github.com/Souhrid-Dey/weather-vibecheck)

---

## 📖 Brief Description
**Weather VibeCheck** is a Gen-AI-powered survival application designed to help citizens navigate severe monsoon weather, urban flooding, and infrastructure failures. 

Instead of relying on static, generic weather alerts, our app dynamically queries live weather conditions and uses Gen-AI to generate **anxiety-aware preparedness checklists**, **offline-capable rationing plans**, **commute risk assessments**, and **multilingual emergency SOS broadcasts**.

---

## 🎯 Problem Statement Alignment
During severe monsoons, citizens face power outages, flooded roads, and high anxiety. Existing weather apps just show raw data (e.g., "50mm rain"), leaving the user to figure out what to do. 

Weather VibeCheck solves this by turning weather data into actionable intelligence. Every feature has been built end-to-end without any mock data or hardcoded responses. If you input your location and pantry items, a live API fetches current weather, calculates distances, and pings an LLM to generate real-time, context-aware survival strategies.

---

## 🧠 Gen-AI Integration & Services Used
This project strictly adheres to the hackathon's mandate of real, functioning AI integrations. We are using **Llama-3.3-70b-versatile** accessed via the **Groq SDK** for lightning-fast inference.

| Feature Area | Where AI is Used | Gen-AI Prompt Strategy |
|--------------|------------------|------------------------|
| **Preparedness Plan** | `backend/routes/monsoon.py` | Takes live weather data and the user's *anxiety level*. If anxiety is "High", the AI outputs empathetic language and breaks tasks into micro-steps to prevent panic. |
| **Pantry Survival** | `backend/prompts/monsoon.py` | Takes a raw string of fridge contents and outputs a 3-day no-cook/low-cook meal plan, prioritizing perishables and generating an immediate shopping list. |
| **Commute Risk** | `backend/routes/monsoon.py` | Ingests the *Haversine distance* between two points and live weather data to give a definitive "Go / No-Go" decision and alternative suggestions. |
| **SOS Broadcaster** | `backend/services/llm_client.py` | Acts as a crisis translator. Condenses complex distress inputs into hyper-efficient (under 160 chars) SMS templates in **English, Hindi, and Marathi**. |

**Technical Note on AI Implementation:** 
All LLM outputs are forced into strict JSON using Groq's `response_format={"type": "json_object"}`. This guarantees that our frontend receives perfectly structured data rather than unpredictable markdown blobs.

---

## 🏆 Hackathon Evaluation & Award Targeting

We have engineered this project specifically around the Hackathon Evaluation Framework:

### 🛡️ Cyber Sentinel (Security)
- **XSS Prevention:** All AI-generated text is passed through a strict `escapeHTML` sanitizer before DOM injection to prevent Cross-Site Scripting via LLM hallucinations.
- **Rate Limiting:** Integrated `SlowAPI` to enforce a strict `5 requests/minute` limit on all LLM endpoints to prevent API abuse.
- **Security Headers:** Added custom middleware in FastAPI to enforce strict `Content-Security-Policy`, `X-Frame-Options: DENY`, and `X-Content-Type-Options: nosniff`.
- **Startup Validation:** Hard fails on deployment if API keys are missing, preventing obscure runtime crashes.

### ⚡ Algorithm Ace (Efficiency)
- **Zero-Latency Fallback (Offline Mode):** Implemented client-side caching using **IndexedDB**. If a user loses internet connectivity during a storm, their last generated preparedness plan remains fully accessible.
- **Lightning Inference:** Swapped from standard models to Groq's Llama 3.3 for sub-second text generation, massively improving UX.

### 💎 Clean Coder (Code Quality & Testing)
- **Modular Architecture:** Separated concerns strictly across `/routes`, `/services`, and `/prompts`.
- **Resilient Fallbacks:** The weather API integration (`weather_client.py`) catches network timeouts and gracefully falls back, explicitly informing the LLM if context is unavailable rather than silently failing.
- **Strict Validation:** Native HTML5 regex patterns (`pattern=".*\S+.*"`) and `minlength` checks block empty space-bar submissions, saving compute.

### 🌍 Inclusive Icon (Accessibility)
- **High Contrast Theme:** Swapped default palettes for a commercial-grade Slate/Navy dark mode with vibrant semantic accents (Emerald for safe, Amber for warnings).
- **Aria/Focus Visibility:** Added high-visibility focus rings (`outline: 2px solid var(--accent-info)`) to ensure complete keyboard navigability.
- **Multilingual Support:** Deliberately designed the SOS feature to serve non-English speakers during critical emergencies.

---

## 🛠️ Tech Stack
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, Vite
- **Backend:** Python 3.12, FastAPI, SlowAPI
- **APIs:** Groq (Llama 3.3 70B), Open-Meteo (Live Weather & Geocoding)
- **Deployment:** Vercel (Unified Monorepo Deployment)

---

## 🏃 Running Locally

To evaluate this project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/Souhrid-Dey/weather-vibecheck.git
   cd weather-vibecheck
   ```

2. **Setup the Backend:**
   ```bash
   cd backend
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
   *Create a `.env` file in the `backend` directory and add your Groq API key:*
   ```env
   GROQ_API_KEY=your_real_key_here
   ```
   *Run the server:*
   ```bash
   uvicorn main:app --reload --port 8000
   ```

3. **Setup the Frontend:**
   ```bash
   cd ../frontend
   npm install
   npm run dev
   ```

*Note: No dummy credentials are required as the app does not feature user authentication (to minimize friction during emergency use).*
