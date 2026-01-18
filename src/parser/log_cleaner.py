def clean_log(log_text: str) -> str:
    """
    Cleans raw log text by removing unnecessary whitespace
    and keeping only meaningful lines.
    """

    cleaned_lines = []

    for line in log_text.splitlines():
        line = line.strip()

        if not line:
            continue

        # Remove timestamp-like patterns (simple version)
        if line.startswith("[") and "]" in line:
            line = line.split("]", 1)[1].strip()

        cleaned_lines.append(line)

    return "\n".join(cleaned_lines)
