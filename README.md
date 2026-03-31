# AI for SRE Engineering

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![SRE](https://img.shields.io/badge/SRE-AI%20Engineering-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

An **AI-powered incident analysis engine** for modern SRE and DevOps environments.

---

# Why AI for SRE?

Modern distributed systems generate massive volumes of telemetry:

- logs  
- metrics  
- traces  
- alerts  
- deployment events  

Traditional monitoring relies on **static thresholds**, which often results in:

- delayed incident detection  
- alert fatigue  
- slow root cause analysis  
- fragmented visibility  

AI can help SRE teams:

- detect anomalies earlier  
- correlate signals across systems  
- accelerate incident investigation  
- reduce operational noise  
- improve reliability  

---

# Architecture Vision

The project is based on an **AI-assisted observability architecture**:

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

````
---

# Project Structure

````
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
│   ├── ai-log-analyzer
│   │   ├── analyzer.py
│   │   ├── sample_logs.txt
│   │   └── requirements.txt
│   │
│   └── anomaly-detection
│       ├── detect_anomalies.py
│       ├── sample_metrics.csv
│       └── requirements.txt
│
├── examples
│   ├── ai-root-cause-analysis
│   │   ├── rca_engine.py
│   │   ├── sample_incident.json
│   │   └── README.md
│   │
│   └── ai-incident-pipeline
│       ├── incident_pipeline.py
│       ├── incident_recommender.py
│       └── README.md
│
├── diagrams
├── .github/workflows
├── LICENSE
├── CONTRIBUTING.md
├── requirements.txt
└── README.md

````

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
AI Log Analyzer (log classification + pattern detection)
Metric Anomaly Detection (Isolation Forest)
Root Cause Analysis (RCA) engine
AI Observability Architecture documentation

In Progress
Integrated AI Incident Pipeline
Action recommendation engine

Planned
Predictive capacity planning
AI-assisted incident response workflows
alert correlation
automated remediation

Getting Started
1. Clone the repository
````
git clone https://github.com/tiagomartimiano/sre-ai-lab.git
cd sre-ai-lab
````
2. Setup environment
````
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
````
3. Run AI Log Analyzer
````
cd labs/ai-log-analyzer
python3 analyzer.py
````
4. Run Metric Anomaly Detection
````
cd labs/anomaly-detection
python3 detect_anomalies.py
````
5. Run Root Cause Analysis
````
cd examples/ai-root-cause-analysis
python3 rca_engine.py
````
6. Run AI Incident Pipeline
````
cd examples/ai-incident-pipeline
python3 incident_pipeline.py
python3 incident_recommender.py
````
AI Incident Pipeline

This project includes an integrated incident analysis pipeline that combines:

log analysis
metric anomaly detection
root cause analysis
action recommendation

Pipeline Flow

Metrics → Logs → Correlation → RCA → Recommended Actions

Example Output

AI Incident Pipeline Result

Log Analysis
  Possible root cause: database connectivity instability

Metric Analysis
  Anomaly count: 3

Root Cause Analysis
  Top hypothesis: deployment_misconfiguration

Recommended Actions

- Inspect database connectivity
- Review recent deployment
- Correlate anomaly timestamps with logs

Engineering Focus

This repository explores key SRE questions:

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
anomaly detection improvements
RCA enhancements
documentation improvements

See CONTRIBUTING.md for details.

License

This project is licensed under the MIT License.

Author

Tiago Martimiano
SRE | DevOps Engineer | Cloud | Kubernetes
