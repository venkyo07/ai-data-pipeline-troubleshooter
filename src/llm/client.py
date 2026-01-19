# LLM responses are non deterministic; retries and validation are mandatory
import requests
from src.utils.json_utils import extract_json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"
MAX_RETRIES = 2

def explain_error(error_type: str, cleaned_log: str, context: str) -> dict:
    prompt = f"""
You are a senior data engineer.

Error type detected: {error_type}

Known historical context:
{context}

Log excerpt:
{cleaned_log}

Tasks:
1. Explain the error using the historical context if relevant
2. Identify the most likely root cause
3. Suggest clear remediation steps

IMPORTANT:
Return ONLY valid JSON with keys:
- explanation
- root_cause
- resolution
"""
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    last_error = None

    for attempt in range(1, MAX_RETRIES + 1):
        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=60)
            response.raise_for_status()

            raw_output = response.json()["response"]
            return extract_json(raw_output)

        except Exception as e:
            last_error = e
            print(f"[WARN] LLM attempt {attempt} failed: {e}")

    raise RuntimeError(f"LLM failed after {MAX_RETRIES} attempts") from last_error

