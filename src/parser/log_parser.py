from src.parser.log_cleaner import clean_log
from src.parser.error_classifier import classify_error


def parse_log(raw_log: str) -> dict:
    """
    Converts raw log text into structured data.
    """

    cleaned = clean_log(raw_log)
    error_type = classify_error(cleaned)

    return {
        "cleaned_log": cleaned,
        "error_type": error_type
    }

