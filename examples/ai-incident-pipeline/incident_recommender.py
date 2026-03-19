import json
from pathlib import Path


def load_summary(file_path: str) -> dict:
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def recommend_actions(summary: dict) -> list[str]:
    recommendations = []

    incident = summary.get("incident_summary", {})
    log_root_cause = incident.get("log_analysis", {}).get("possible_root_cause", "")
    top_hypothesis = incident.get("root_cause_analysis", {}).get("top_hypothesis", "")
    anomaly_count = incident.get("metric_analysis", {}).get("anomaly_count", 0)

    if "database" in log_root_cause or "database" in top_hypothesis:
        recommendations.append("Inspect database connectivity and connection pool usage.")
        recommendations.append("Check recent configuration changes affecting database access.")

    if "deployment" in top_hypothesis:
        recommendations.append("Review the most recent deployment and configuration changes.")
        recommendations.append("Consider rollback if the incident started immediately after release.")

    if anomaly_count >= 3:
        recommendations.append("Inspect anomaly window timestamps in dashboards and traces.")
        recommendations.append("Correlate anomaly windows with logs and deployment events.")

    if not recommendations:
        recommendations.append("Continue manual investigation with logs, metrics, and traces.")

    return recommendations


def main() -> None:
    summary_path = Path("output/incident_summary.json")
    summary = load_summary(str(summary_path))
    recommendations = recommend_actions(summary)

    print("\nRecommended Actions\n")
    for action in recommendations:
        print(f"- {action}")


if __name__ == "__main__":
    main()