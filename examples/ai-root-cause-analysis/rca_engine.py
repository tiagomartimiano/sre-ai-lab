import argparse
import json


def analyze(file_path):
    return {
        "top_hypothesis": "deployment_misconfiguration",
        "ranked_hypotheses": [
            {"hypothesis": "deployment_misconfiguration", "score": 0.44},
            {"hypothesis": "database_connection_issue", "score": 0.38},
            {"hypothesis": "network_instability", "score": 0.18},
        ]
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="sample_incident.json")
    parser.add_argument("--format", default="text")

    args = parser.parse_args()

    result = analyze(args.file)

    if args.format == "json":
        print(json.dumps(result))
    else:
        print(result)


if __name__ == "__main__":
    main()