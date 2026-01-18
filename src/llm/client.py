import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "mistral"


def explain_error(error_type: str, cleaned_log: str) -> dict:
    """
    Uses a local Ollama LLM to explain the error, root cause, and resolution.
    """

    prompt = f"""
You are a senior data engineer.

Error type detected: {error_type}

Log excerpt:
{cleaned_log}

Tasks:
1. Explain the error in simple terms
2. Identify the most likely root cause
3. Suggest clear remediation steps

Return the response strictly in JSON with keys:
- explanation
- root_cause
- resolution
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    raw_output = response.json()["response"]
    return json.loads(raw_output)

