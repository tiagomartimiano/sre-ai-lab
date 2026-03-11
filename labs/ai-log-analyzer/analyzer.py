import re
from collections import Counter

patterns = {
    "database_issue": r"connection refused|database error",
    "timeout_issue": r"timeout",
    "http_error": r"HTTP 5\d\d"
}

def analyze_logs(file_path):

    with open(file_path, "r") as file:
        logs = file.readlines()

    error_patterns = []

    for log in logs:

        if "error" in log.lower():
            error_patterns.append("error")

        if "timeout" in log.lower():
            error_patterns.append("timeout")

        if "connection refused" in log.lower():
            error_patterns.append("connection_refused")

        if "500" in log:
            error_patterns.append("http_500")

    with open(file_path) as f:
        logs = f.readlines()

    results = []

    for log in logs:
        for category, pattern in patterns.items():
            if re.search(pattern, log, re.IGNORECASE):
                results.append(category)

    counter = Counter(error_patterns)


    print("Detected issues:\n")

    for issue, count in counter.items():
        print(f"{issue}: {count} occurrences")

if __name__ == "__main__":
    analyze_logs("sample_logs.txt")