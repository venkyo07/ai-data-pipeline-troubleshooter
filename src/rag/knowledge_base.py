import json


def load_known_issues(path: str = "data/known_issues.json") -> list:
    with open(path, "r") as f:
        return json.load(f)

