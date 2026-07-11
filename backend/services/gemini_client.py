"""
Gemini API client wrapper for Weather VibeCheck.

Handles communication with Google's Gemini AI, forcing strict JSON
output formats and handling basic errors.
"""
import os
import json
import re
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables (API Key)
load_dotenv()

# Configure the SDK with the key
genai.configure(api_key=os.environ.get("GEMINI_API_KEY", ""))

# Using gemini-2.0-flash as it's fast and supports structured JSON outputs well
MODEL_NAME = "gemini-2.0-flash"

def ask_gemini(system_prompt: str, user_message: str) -> dict:
    """
    Sends a prompt to Gemini and parses the structured JSON response.

    Args:
        system_prompt: Core instruction set for Gemini (persona, rules, output schema).
        user_message: User inputs formatted into a readable string.

    Returns:
        dict: Parsed JSON response.
        
    Raises:
        ValueError: If JSON decoding fails.
        RuntimeError: If the API call fails (rate limit, network issue).
    """
    model = genai.GenerativeModel(
        model_name=MODEL_NAME,
        system_instruction=system_prompt,
        generation_config=genai.GenerationConfig(
            temperature=0.7,
            # Forcing JSON response guarantees the frontend can reliably parse the output
            response_mime_type="application/json", 
        ),
    )

    try:
        response = model.generate_content(user_message)
        raw = response.text.strip()

        # Clean any potential markdown code blocks (```json) returned by accident
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse AI response into JSON: {e}\nRaw output: {raw}") from e
    except Exception as e:
        raise RuntimeError(f"Gemini API failure: {e}") from e
