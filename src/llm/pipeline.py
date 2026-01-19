from src.parser.log_parser import parse_log
from src.llm.client import explain_error
from src.rag.knowledge_base import load_known_issues
from src.rag.retriever import retrieve_context


def analyze_log_with_ai(raw_log: str) -> dict:
    parsed = parse_log(raw_log)

    known_issues = load_known_issues()
    context = retrieve_context(parsed["error_type"], known_issues)

    try:
        ai_result = explain_error(
            error_type=parsed["error_type"],
            cleaned_log=parsed["cleaned_log"],
            context=context
        )

        return {
            "error_type": parsed["error_type"],
            "explanation": ai_result["explanation"],
            "root_cause": ai_result["root_cause"],
            "resolution": ai_result["resolution"]
        }

    except Exception as e:
        return {
            "error_type": parsed["error_type"],
            "explanation": "AI analysis failed",
            "root_cause": "Unable to determine due to AI error",
            "resolution": "Retry analysis or check system logs",
            "error": str(e)
        }

