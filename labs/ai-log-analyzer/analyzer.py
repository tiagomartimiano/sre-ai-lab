import argparse
import json
from collections import Counter


def analyze_logs(file_path):
    error_patterns = ["error", "timeout", "connection_refused", "http_500"]

    # exemplo simples (ajusta depois)
    results = ["error", "timeout", "connection_refused"]

    counter = Counter(results)

    return {
        "summary": dict(counter),
        "possible_root_cause": "database connectivity instability"
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="sample_logs.txt")
    parser.add_argument("--format", default="text")

    args = parser.parse_args()

    result = analyze_logs(args.file)

    if args.format == "json":
        print(json.dumps(result))
        return

    print("\nDetected issues:\n")
    for issue, count in result["summary"].items():
        print(f"{issue}: {count}")

    print(f"\nPossible root cause: {result['possible_root_cause']}")


if __name__ == "__main__":
    main()