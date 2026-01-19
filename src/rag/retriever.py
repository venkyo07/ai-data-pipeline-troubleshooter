def retrieve_context(error_type: str, known_issues: list) -> str:
    """
    Retrieves relevant known issue context based on error type.
    """

    for issue in known_issues:
        if issue["error_type"] == error_type:
            return (
                f"Known issue:\n"
                f"Description: {issue['description']}\n"
                f"Root cause: {issue['root_cause']}\n"
                f"Resolution: {issue['resolution']}\n"
            )

    return "No known issues found."

