import os
import requests
from dotenv import load_dotenv
from loguru import logger
from app.services.history_service import find_similar_changes

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    logger.error("Missing GEMINI_API_KEY")

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-latest:generateContent"


def generate_summary(description: str, similar_changes=None) -> str:
    try:
        history_context = ""

        if similar_changes:
            for i, change in enumerate(similar_changes, 1):
                history_context += f"""
{i}. {change['description']}
   Risk: {change['risk']}
   Issues: {change['issues']}
"""

        prompt = f"""
You are an expert Change Manager.

Current Change:
{description}

Similar Past Changes:
{history_context}

IMPORTANT:
- Use past changes for context-aware reasoning
- Highlight similarities
- Be specific (billing, invoice, API, UI etc.)

Provide:
1. Summary
2. Key Risks
3. Suggestions
"""

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": prompt}
                    ]
                }
            ]
        }

        headers = {
            "Content-Type": "application/json",
            "X-goog-api-key": GEMINI_API_KEY
        }

        response = requests.post(
            GEMINI_URL,
            headers=headers,
            json=payload,
            timeout=60,
            proxies={"http": None, "https": None}
        )

        data = response.json()

        if "candidates" not in data:
            logger.error(f"Invalid AI response: {data}")
            return "AI response invalid"

        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            logger.error(f"Unexpected AI response format: {data}")
            return "AI response parsing failed"

    except Exception as e:
        logger.exception(f"AI Error: {e}")
        return "AI summary unavailable."
    
