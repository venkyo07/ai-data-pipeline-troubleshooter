from src.llm.pipeline import analyze_log_with_ai

with open("data/sample_logs/spark_oom.log") as f:
    raw_log = f.read()

result = analyze_log_with_ai(raw_log)

print("Error Type:", result["error_type"])
print("\nExplanation:", result["explanation"])
print("\nRoot Cause:", result["root_cause"])
print("\nResolution:", result["resolution"])

