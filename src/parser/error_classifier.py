def classify_error(cleaned_log: str) -> str:
    """
    Classifies log text into known error categories.
    """

    log = cleaned_log.lower()

    if "outofmemoryerror" in log or "java heap space" in log:
        return "OOM_ERROR"

    if "executorlost" in log or "executor lost" in log:
        return "EXECUTOR_FAILURE"

    if "dag run failed" in log or "airflowexception" in log:
        return "DAG_FAILURE"

    if "container killed" in log or "yarn" in log:
        return "RESOURCE_LIMIT"

    return "UNKNOWN"

