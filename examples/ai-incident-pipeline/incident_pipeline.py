import json
import subprocess
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = BASE_DIR.parent.parent

LOG_ANALYZER_DIR = PROJECT_ROOT / "labs" / "ai-log-analyzer"
METRIC_DETECTION_DIR = PROJECT_ROOT / "labs" / "anomaly-detection"
RCA_DIR = PROJECT_ROOT / "examples" / "ai-root-cause-analysis"

LOG_FILE = LOG_ANALYZER_DIR / "sample_logs.txt"
METRIC_FILE = METRIC_DETECTION_DIR / "sample_metrics.csv"
INCIDENT_FILE = RCA_DIR / "sample_incident.json"


def run_json_command(command: list[str], cwd: Path) -> dict:
    result = subprocess.run(
        command,
        cwd=str(cwd),
        capture_output=True,
        text=True,
        check=True,
    )

    if not result.stdout.strip():
        raise RuntimeError(f"Command returned empty output: {' '.join(command)}")

    return json.loads(result.stdout)


def run_log_analyzer() -> dict:
    return run_json_command(
        ["python3", "analyzer.py", "--file", str(LOG_FILE), "--format", "json"],
        LOG_ANALYZER_DIR,
    )


def run_metric_detector() -> dict:
    return run_json_command(
        ["python3", "detect_anomalies.py", "--file", str(METRIC_FILE), "--format", "json"],
        METRIC_DETECTION_DIR,
    )


def run_rca() -> dict:
    return run_json_command(
        ["python3", "rca_engine.py", "--file", str(INCIDENT_FILE), "--format", "json"],
        RCA_DIR,
    )


def build_incident_summary(log_result: dict, metric_result: dict, rca_result: dict) -> dict:
    return {
        "incident_summary": {
            "log_analysis": {
                "summary": log_result.get("summary", {}),
                "possible_root_cause": log_result.get("possible_root_cause"),
            },
            "metric_analysis": {
                "anomaly_count": metric_result.get("anomaly_count", 0),
                "anomaly_timestamps": metric_result.get("anomaly_timestamps", []),
                "anomaly_samples": metric_result.get("anomaly_samples", []),
            },
            "root_cause_analysis": {
                "top_hypothesis": rca_result.get("top_hypothesis"),
                "ranked_hypotheses": rca_result.get("ranked_hypotheses", []),
            },
        }
    }


def print_human_readable(summary: dict) -> None:
    incident = summary["incident_summary"]

    print("\nAI Incident Pipeline Result\n")

    print("Log Analysis")
    print(f"  Summary: {incident['log_analysis']['summary']}")
    print(f"  Possible root cause: {incident['log_analysis']['possible_root_cause']}")

    print("\nMetric Analysis")
    print(f"  Anomaly count: {incident['metric_analysis']['anomaly_count']}")
    print(f"  Anomaly timestamps: {incident['metric_analysis']['anomaly_timestamps']}")

    print("\nRoot Cause Analysis")
    print(f"  Top hypothesis: {incident['root_cause_analysis']['top_hypothesis']}")
    print("  Ranked hypotheses:")
    for item in incident["root_cause_analysis"]["ranked_hypotheses"]:
        print(f"    - {item['hypothesis']}: {item['score']}")


def save_output(summary: dict) -> Path:
    output_dir = BASE_DIR / "output"
    output_dir.mkdir(exist_ok=True)

    output_file = output_dir / "incident_summary.json"
    output_file.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return output_file


def main() -> None:
    log_result = run_log_analyzer()
    metric_result = run_metric_detector()
    rca_result = run_rca()

    summary = build_incident_summary(log_result, metric_result, rca_result)
    print_human_readable(summary)

    output_file = save_output(summary)
    print(f"\nStructured output saved to: {output_file}")


if __name__ == "__main__":
    main()