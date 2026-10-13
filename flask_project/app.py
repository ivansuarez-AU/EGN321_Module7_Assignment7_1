from flask import Flask, jsonify
import sqlite3, os

DB_PATH = os.environ.get("MODULE7_DB","module7_monitor.db")
app = Flask(__name__)

@app.get("/")
def dashboard():
    conn = sqlite3.connect(DB_PATH)
    latest = conn.execute("SELECT sample_number,timestamp,accepted_value,sensor_status,health_state,alert_state FROM readings ORDER BY id DESC LIMIT 1").fetchone()
    count = conn.execute("SELECT COUNT(*) FROM readings").fetchone()[0]
    recent = conn.execute("SELECT sample_number,timestamp,accepted_value,sensor_status,health_state,alert_state FROM readings ORDER BY id DESC LIMIT 20").fetchall()
    conn.close()
    return {"latest":latest,"history_count":count,"recent":recent}

@app.get("/health")
def health():
    conn = sqlite3.connect(DB_PATH)
    row = conn.execute("SELECT health_state FROM readings ORDER BY id DESC LIMIT 1").fetchone()
    conn.close()
    return jsonify({"health_state": row[0] if row else "UNKNOWN"})

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)