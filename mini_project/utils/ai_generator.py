"""
utils/ai_generator.py
Calls Ollama (local AI) to generate flashcards from a topic (Day 4 - APIs & AI Tooling)

Ollama runs 100% on your machine — no API key needed, no internet required.
Install: https://ollama.com
Pull a model: ollama pull llama3.2
Run server:   ollama serve  (usually auto-starts)
"""

import json
import logging
import requests  # Day 4: REST API with requests library

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

# Ollama runs locally on port 11434 by default
OLLAMA_URL = "http://localhost:11434/api/chat"
OLLAMA_MODEL = "llama3.2"  # Change to any model you've pulled e.g. mistral, gemma2


def check_ollama_running():
    """Ping Ollama to make sure the server is up."""
    try:
        resp = requests.get("http://localhost:11434", timeout=3)
        return resp.status_code == 200
    except requests.exceptions.ConnectionError:
        return False


def generate_flashcards(topic: str, count: int = 5) -> list[dict]:
    """
    Calls Ollama locally to generate `count` Q&A flashcards on `topic`.
    Returns a list of dicts: [{"question": ..., "answer": ...}, ...]
    """

    # Check Ollama is running before sending request (Day 1: debugging mindset)
    if not check_ollama_running():
        raise ConnectionError(
            "\n  ❌ Ollama is not running.\n"
            "  Start it with: ollama serve\n"
            "  Install from:  https://ollama.com\n"
            f"  Then pull a model: ollama pull {OLLAMA_MODEL}"
        )

    prompt = f"""Generate exactly {count} flashcard question-and-answer pairs about: "{topic}".

Rules:
- Questions should test real understanding, not just definitions
- Answers should be concise (1-3 sentences max)
- Vary difficulty: mix easy, medium, hard questions
- Do NOT number the questions

Respond ONLY with a valid JSON array. No explanation, no markdown fences.
Example format:
[
  {{"question": "What is X?", "answer": "X is ..."}},
  {{"question": "How does Y work?", "answer": "Y works by ..."}}
]"""

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,       # get full response at once, not streamed
        "options": {
            "temperature": 0.7
        },
    }

    logger.info(f"Generating {count} flashcards for '{topic}' using {OLLAMA_MODEL}...")

    try:
        response = requests.post(OLLAMA_URL, json=payload, timeout=120)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        raise ConnectionError(
            "  ❌ Ollama timed out. The model may be loading — try again in a moment."
        )
    except requests.exceptions.HTTPError as e:
        status = e.response.status_code
        if status == 404:
            raise RuntimeError(
                f"  ❌ Model '{OLLAMA_MODEL}' not found.\n"
                f"  Pull it first: ollama pull {OLLAMA_MODEL}"
            )
        raise RuntimeError(f"  ❌ Ollama error {status}: {e.response.text}")
    except requests.exceptions.ConnectionError:
        raise ConnectionError(
            "  ❌ Cannot connect to Ollama.\n"
            "  Make sure it's running: ollama serve"
        )

    data = response.json()
    raw_text = data["message"]["content"].strip()

    # Strip accidental markdown fences if model adds them anyway
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    # Defensive JSON parsing (Day 1: debugging mindset)
    try:
        cards = json.loads(raw_text)
        if not isinstance(cards, list):
            raise ValueError("Expected a JSON array")
        return cards
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse AI response: {raw_text[:200]}")
        raise ValueError(f"AI returned invalid JSON: {e}")
