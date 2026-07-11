"""
Groq API client wrapper for Weather VibeCheck.

Handles communication with Groq's fast Llama models, forcing strict JSON
output formats and handling basic errors.
"""
import os
import json
import re
from groq import Groq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure the SDK with the key
client = Groq(api_key=os.environ.get("GROQ_API_KEY", ""))

# Llama 3.3 70B is incredible at formatting JSON and very fast on Groq
MODEL_NAME = "llama-3.3-70b-versatile"

def ask_llm(system_prompt: str, user_message: str) -> dict:
    """
    Sends a prompt to Groq and parses the structured JSON response.

    Args:
        system_prompt: Core instruction set for LLM (persona, rules, output schema).
        user_message: User inputs formatted into a readable string.

    Returns:
        dict: Parsed JSON response.
        
    Raises:
        ValueError: If JSON decoding fails.
        RuntimeError: If the API call fails (rate limit, network issue).
    """
    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": system_prompt + "\n\nIMPORTANT: You must return valid JSON."},
                {"role": "user", "content": user_message}
            ],
            model=MODEL_NAME,
            temperature=0.7,
            response_format={"type": "json_object"},
        )
        
        raw = response.choices[0].message.content.strip()

        # Clean any potential markdown code blocks (```json) returned by accident
        raw = re.sub(r"^```(?:json)?\s*", "", raw)
        raw = re.sub(r"\s*```$", "", raw)

        return json.loads(raw)
    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse AI response into JSON: {e}\nRaw output: {raw}") from e
    except Exception as e:
        raise RuntimeError(f"LLM API failure: {e}") from e
