import json
from pathlib import Path


def load_summary(file_path: str) -> dict:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Summary file not found: {file_path}")

    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def recommend_actions(summary: dict) -> list[str]:
    recommendations = []

    incident = summary.get("incident_summary", {})
    log_root_cause = incident.get("log_analysis", {}).get("possible_root_cause", "")
    top_hypothesis = incident.get("root_cause_analysis", {}).get("top_hypothesis", "")
    anomaly_count = incident.get("metric_analysis", {}).get("anomaly_count", 0)

    if "database" in log_root_cause or "database" in top_hypothesis:
        recommendations.append("Inspect database connectivity and connection pool usage.")
        recommendations.append("Review recent configuration changes affecting database access.")

    if "deployment" in top_hypothesis:
        recommendations.append("Review the most recent deployment and configuration changes.")
        recommendations.append("Consider rollback if the incident started immediately after release.")

    if "network" in top_hypothesis or "timeout" in log_root_cause:
        recommendations.append("Check downstream dependencies and network latency between services.")

    if anomaly_count >= 3:
        recommendations.append("Inspect anomaly timestamps in dashboards, traces, and logs.")
        recommendations.append("Correlate anomaly windows with deployment and scaling events.")

    if not recommendations:
        recommendations.append("Continue manual investigation using logs, metrics, and traces.")

    return recommendations


def print_recommendations(recommendations: list[str]) -> None:
    print("\nRecommended Actions\n")
    for action in recommendations:
        print(f"- {action}")


def main() -> None:
    summary_path = Path("output/incident_summary.json")
    summary = load_summary(str(summary_path))
    recommendations = recommend_actions(summary)
    print_recommendations(recommendations)


if __name__ == "__main__":
    main()