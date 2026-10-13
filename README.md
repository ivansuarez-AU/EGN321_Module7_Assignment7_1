# EGN 321 — Module 7 Assignment 7.1
## Unattended Monitoring System

### How to Start the System
Install dependencies with:
`pip install -r requirements.txt`

Run directly:
`python app.py`

Run through the restart supervisor:
`python supervisor.py`

Open:
`http://127.0.0.1:5000`

### Automatic Restart / Startup
The provided `supervisor.py` restarts the Flask process if it exits.
A Linux systemd example is also included with `Restart=always`.
Students must document the method they actually use.

### Sensor / Input Source
`sensor_replay.csv` is a virtual temperature-sensor replay.

### Expected Sampling Interval
2 seconds.

### Stale-Data Definition
HEALTHY = valid/current data.
DEGRADED = missing/rejected input or more than 10 seconds since the last valid reading.
FAILED = more than 30 seconds since the last valid reading.
These are classroom thresholds.

### Threshold Rule
Trigger when accepted temperature is at or above 30.0 C.

### Alert-Control Method
Persistence: 3 consecutive valid high readings.
Hysteresis: alert clears only at or below 28.5 C.

### System-Health States
HEALTHY
DEGRADED
FAILED

A production implementation may add RECOVERING.

### Log Location
`module7_app.jsonl`
and exported `required_evidence/application_logs.csv`.

### Known Limitations
Colab is a teaching/demo environment, not a permanent unattended host.
Sensor data are simulated.
Flask test-client verification does not replace the student's own real browser screenshot.
The supervisor test proves process restart behavior, not OS-level boot behavior.

### Automatic Recovery
The demo automatically recovers from a controlled application process crash by restarting the process.

### Human Intervention Still Required
Examples:
- persistent database corruption;
- host/server outage;
- repeated crash loops;
- unresolved sensor-source failure;
- disk exhaustion;
- permission/security problems;
- invalid configuration.

### Required Evidence
See `required_evidence/` for:
dashboard running, current reading, historical view, alert active, alert cleared,
missing/degraded evidence, logs, restart/recovery, and final healthy state.

### GitHub Repository
Students must place the final project and evidence in their GitHub repository and submit the repository link.

### Course Rule
Students must be able to explain, modify, and defend all submitted code.
