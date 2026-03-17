# AI Log Analyzer

## Overview

This lab demonstrates a practical log analysis workflow for SRE scenarios.

The objective is to classify recurring operational patterns in logs and provide
a foundation for AI-assisted incident triage and root cause investigation.

---

## Problem

Production environments generate large volumes of logs.

During incidents, engineers often need to manually identify:

- repeated failures
- timeouts
- database issues
- dependency outages
- HTTP 5xx errors

This lab automates the first stage of that triage process.

---

## Current Capabilities

- classify predefined error patterns
- count recurring issues
- infer a possible root cause
- export structured JSON output
- support CLI execution with input file argument

---

## Files

- `analyzer.py` — main script
- `sample_logs.txt` — sample input logs
- `README.md` — lab documentation

---

## How to Run

Run with sample input:

```bash
python3 analyzer.py