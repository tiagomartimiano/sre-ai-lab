import argparse
import json
import pandas as pd
from sklearn.ensemble import IsolationForest


def analyze(file_path):
    df = pd.read_csv(file_path)

    features = df[["cpu_usage", "latency_ms", "error_rate", "request_volume"]]

    model = IsolationForest(contamination=0.1, random_state=42)
    df["anomaly"] = model.fit_predict(features)

    anomalies = df[df["anomaly"] == -1]

    return {
        "anomaly_count": len(anomalies),
        "anomaly_timestamps": anomalies["timestamp"].tolist()
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="sample_metrics.csv")
    parser.add_argument("--format", default="text")

    args = parser.parse_args()

    result = analyze(args.file)

    if args.format == "json":
        print(json.dumps(result))
        return

    print(result)


if __name__ == "__main__":
    main()
