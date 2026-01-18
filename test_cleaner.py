from src.parser.log_cleaner import clean_log

sample_log = """
[2024-01-15 02:14:10] ERROR Task failed
java.lang.OutOfMemoryError: Java heap space
"""

print(clean_log(sample_log))

