# AI Incident Pipeline

## Overview

This example integrates multiple project components into a single incident workflow.

The pipeline combines:

- log analysis
- metric anomaly detection
- root cause analysis

The goal is to demonstrate how AI-assisted SRE components can work together.

---

## Pipeline Flow

```text
Metric Anomaly Detection
        ↓
AI Log Analyzer
        ↓
Incident Context
        ↓
Root Cause Analysis
        ↓
Incident Summary

How to Run

From the repository root:

cd examples/ai-incident-pipeline
python3 incident_pipeline.py

Output

The pipeline produces:

terminal summary

structured JSON file in output/incident_summary.json

Future Improvements

automatic correlation between anomaly windows and logs

remediation recommendation engine

incident timeline reconstruction

postmortem-style summary generation

## `Makefile`

```makefile
run-incident-pipeline:
	cd examples/ai-incident-pipeline && python3 incident_pipeline.py

## Action Recommendation

After generating the incident summary, run:

```bash
python3 incident_recommender.py