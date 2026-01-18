from src.parser.log_parser import parse_log
from src.llm.client import explain_error


def analyze_log_with_ai(raw_log: str) -> dict:
    """
    Full pipeline: raw log → structured parsing → AI explanation
    """

    parsed = parse_log(raw_log)

    ai_result = explain_error(
        error_type=parsed["error_type"],
        cleaned_log=parsed["cleaned_log"]
    )

    return {
        "error_type": parsed["error_type"],
        "explanation": ai_result["explanation"],
        "root_cause": ai_result["root_cause"],
        "resolution": ai_result["resolution"]
    }

