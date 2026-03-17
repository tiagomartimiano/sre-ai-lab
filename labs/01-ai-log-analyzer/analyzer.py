import argparse
import json
import re
from collections import Counter
from pathlib import Path


PATTERNS = {
    "database_issue": r"connection refused|database error|connection pool exhausted",
    "timeout_issue": r"timeout|timed out",
    "http_error": r"http 5\d\d|\b5\d\d\b",
    "dependency_failure": r"downstream service unavailable|dependency failure|upstream error",
}


ROOT_CAUSE_HINTS = {
    "database_issue": "database connectivity instability",
    "timeout_issue": "network latency or slow downstream dependency",
    "http_error": "application instability or downstream failure",
    "dependency_failure": "downstream dependency outage",
}


def load_logs(file_path: str) -> list[str]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Log file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip()]


def classify_log(log: str, patterns: dict[str, str]) -> list[str]:
    matches = []

    for category, pattern in patterns.items():
        if re.search(pattern, log, re.IGNORECASE):
            matches.append(category)

    return matches


def aggregate_results(logs: list[str], patterns: dict[str, str]) -> tuple[Counter, list[dict]]:
    counter: Counter = Counter()
    classified_logs: list[dict] = []

    for log in logs:
        categories = classify_log(log, patterns)

        if categories:
            counter.update(categories)
            classified_logs.append({"log": log, "categories": categories})
        else:
            classified_logs.append({"log": log, "categories": ["unclassified"]})

    return counter, classified_logs


def infer_possible_root_cause(counter: Counter) -> str:
    if not counter:
        return "no clear root cause identified"

    most_common = counter.most_common(1)[0][0]
    return ROOT_CAUSE_HINTS.get(most_common, "no clear root cause identified")


def build_summary(counter: Counter, classified_logs: list[dict]) -> dict:
    return {
        "summary": dict(counter),
        "possible_root_cause": infer_possible_root_cause(counter),
        "classified_logs": classified_logs,
    }


def print_human_readable(result: dict) -> None:
    print("\nDetected issues:\n")

    summary = result.get("summary", {})
    if not summary:
        print("No known issues detected.")
    else:
        for issue, count in summary.items():
            print(f"{issue}: {count} occurrences")

    print(f"\nPossible root cause: {result['possible_root_cause']}")


def export_json(result: dict, output_file: str | None) -> None:
    payload = json.dumps(result, indent=2, ensure_ascii=False)

    if output_file:
        Path(output_file).write_text(payload, encoding="utf-8")
    else:
        print(payload)


def analyze_logs(file_path: str) -> dict:
    logs = load_logs(file_path)
    counter, classified_logs = aggregate_results(logs, PATTERNS)
    return build_summary(counter, classified_logs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Analyze logs for common SRE incident patterns.")
    parser.add_argument(
        "--file",
        default="sample_logs.txt",
        help="Path to the log file to analyze.",
    )
    parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        help="Output format.",
    )
    parser.add_argument(
        "--output",
        help="Optional file path to save JSON output.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    result = analyze_logs(args.file)

    if args.format == "json":
        export_json(result, args.output)
    else:
        print_human_readable(result)


if __name__ == "__main__":
    main()