def build_timeline(anomalies, logs):
    events = []

    for a in anomalies:
        events.append({"time": a, "type": "anomaly"})

    for log in logs:
        events.append({
            "time": log["timestamp"],
            "type": "log",
            "data": log
        })

    return sorted(events, key=lambda x: x["time"])