from datetime import datetime, timedelta


def parse_time(ts):
    return datetime.strptime(ts, "%Y-%m-%d %H:%M:%S")


def correlate(anomaly_timestamps, logs, window_seconds=120):
    correlated = []

    for ts in anomaly_timestamps:
        anomaly_time = parse_time(ts)

        for log in logs:
            log_time = parse_time(log["timestamp"])

            delta = abs((log_time - anomaly_time).total_seconds())

            if delta <= window_seconds:
                correlated.append(log)

    return correlated
