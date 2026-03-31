# AI for SRE Engineering

![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![SRE](https://img.shields.io/badge/SRE-AI%20Engineering-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

This repository explores how **Artificial Intelligence can enhance Site Reliability Engineering (SRE) and DevOps practices**.

---

# Why AI for SRE?

Modern distributed systems generate massive volumes of telemetry:

- logs
- metrics
- traces
- alerts
- deployment events

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
Project Structure
sre-ai-lab
│
├── docs
├── labs
├── examples
├── diagrams
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
Getting Started
git clone https://github.com/tiagomartimiano/sre-ai-lab.git
cd sre-ai-lab
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
AI Incident Pipeline
Metrics → Logs → Correlation → RCA → Recommended Actions
Author

Tiago Martimiano
SRE | DevOps Engineer | Cloud | Kubernetes
