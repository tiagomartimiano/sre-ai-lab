# AI for SRE Engineering

This repository explores how **Artificial Intelligence can enhance Site Reliability Engineering (SRE) and DevOps practices**.

The goal is to demonstrate **practical implementations of AI applied to reliability engineering problems**, combining:

- real use cases
- executable labs
- architecture design
- engineering concepts

---

# Why AI for SRE?

Modern distributed systems generate massive volumes of telemetry data:

- logs  
- metrics  
- traces  
- alerts  
- deployment events  

Traditional monitoring tools rely on **static thresholds**, which often lead to:

- delayed incident detection  
- alert fatigue  
- slow root cause analysis  
- fragmented observability  

AI can help SRE teams:

- detect anomalies earlier  
- correlate signals across systems  
- accelerate incident investigation  
- automate operational insights  
- improve system reliability  

---

# Architecture Vision

The core idea of this project is an **AI-assisted observability platform**.

```text
Applications / Services
        ↓
Telemetry Collection
(Metrics / Logs / Traces / Events)
        ↓
Observability Platform
(Prometheus / Grafana / Dynatrace / OpenTelemetry)
        ↓
AI Processing Layer
        ↓
Anomaly Detection / Correlation / RCA
        ↓
SRE Decision Support

This architecture aims to augment human decision-making during incidents.

Project Structure
sre-ai-lab
│
├── docs
│   ├── architectures
│   │   └── ai-observability-platform.md
│   │
│   └── sre-concepts
│       └── ai-assisted-incident-response.md
│
├── labs
│   ├── 01-ai-log-analyzer
│   └── 02-metric-anomaly-detection
│
├── examples
│   └── ai-root-cause-analysis
│
├── diagrams
│
├── .github/workflows
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
└── README.md
Technologies Used
Infrastructure

Kubernetes

Terraform

Docker

Observability

Prometheus

Grafana

Dynatrace

OpenTelemetry

AI / Data

Python

Scikit-learn

Pandas

NumPy

Current Status
Implemented

AI Log Analyzer (log classification + root cause hint)

Metric Anomaly Detection (Isolation Forest)

AI Observability Architecture documentation

In Progress

AI Root Cause Analysis (scoring improvements and integration)

Planned

Predictive capacity planning

AI-assisted incident response workflows

alert correlation

automated remediation

Getting Started
1. Clone the repository
git clone https://github.com/tiagomartimiano/sre-ai-lab.git
cd sre-ai-lab
2. Setup environment
./setup.sh
source .venv/bin/activate
3. Run AI Log Analyzer
make run-log-analyzer

or manually:

cd labs/01-ai-log-analyzer
python3 analyzer.py
4. Run Metric Anomaly Detection
make run-metric-anomaly-detection

or:

cd labs/02-metric-anomaly-detection
python3 detect_anomalies.py
5. Run Root Cause Analysis Example
make run-rca

or:

cd examples/ai-root-cause-analysis
python3 rca_engine.py
Case Studies
1. AI Log Analyzer

Detects recurring failure patterns in logs.

Capabilities:

classify log errors

detect repeated issues

infer possible root causes

📁 Location:

labs/01-ai-log-analyzer
2. Metric Anomaly Detection

Uses machine learning (Isolation Forest) to detect abnormal behavior in telemetry.

Signals analyzed:

CPU usage

latency

error rate

request volume

📁 Location:

labs/02-metric-anomaly-detection
Examples
AI Root Cause Analysis

Simulates how incident signals can be correlated to rank possible causes.

Signals considered:

latency spikes

HTTP errors

pod restarts

deployment events

📁 Location:

examples/ai-root-cause-analysis
Engineering Focus

This project explores key SRE questions:

Can AI reduce MTTR?

Can anomaly detection reduce alert fatigue?

Can telemetry correlation improve incident triage?

How far can automation go without removing human control?

Future Experiments

predictive incident detection

topology-aware root cause analysis

automated remediation with guardrails

LLM-assisted incident summaries

AI incident copilots

Contributing

Contributions are welcome.

You can contribute with:

new AI experiments for SRE

improvements in anomaly detection

RCA enhancements

documentation improvements

See CONTRIBUTING.md for guidelines.

License

This project is licensed under the MIT License.

Author

Tiago Martimiano
SRE | DevOps Engineer | Cloud | Kubernetes