import json
import re


def extract_json(text: str) -> dict:
    """
    Extracts the first valid JSON object from text.
    Raises ValueError if none found.
    """

    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting JSON using regex
    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("No JSON object found in LLM response")

    try:
        return json.loads(match.group())
    except json.JSONDecodeError:
        raise ValueError("Extracted JSON is invalid")

