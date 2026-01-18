from src.parser.log_parser import parse_log
from src.parser.log_cleaner import clean_log

with open("data/sample_logs/spark_oom.log") as f:
    raw_log = f.read()

result = parse_log(raw_log)

print("Error Type:", result["error_type"])
