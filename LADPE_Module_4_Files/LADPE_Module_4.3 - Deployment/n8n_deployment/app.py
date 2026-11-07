"""
Barbenheimer Q&A - a tiny web app that talks to an n8n webhook.

How it works:
  Browser (index.html)  --->  this Flask server (/api/ask)  --->  n8n webhook
  The Flask server forwards your question to n8n and sends the answer back.
  (Going through our own server avoids browser CORS errors and keeps the
   webhook URL out of the page source.)
"""
import os

import requests
from flask import Flask, jsonify, request, send_from_directory

# ---------------------------------------------------------------------------
# STEP 1: PASTE YOUR n8n PRODUCTION WEBHOOK URL BETWEEN THE QUOTES BELOW
# (On Cloud Run you can also override it with the N8N_WEBHOOK_URL env variable.)
# ---------------------------------------------------------------------------
WEBHOOK_URL = os.environ.get(
    "N8N_WEBHOOK_URL",
    "https://ladpessentials2026.app.n8n.cloud/webhook/0388661e-c222-48d8-9509-ed0eede8a513",
)

app = Flask(__name__, static_folder="static")


@app.get("/")
def home():
    return send_from_directory("static", "index.html")


@app.post("/api/ask")
def ask():
    question = (request.get_json(silent=True) or {}).get("question", "").strip()
    if not question:
        return jsonify(error="Please type a question."), 400

    try:
        r = requests.post(WEBHOOK_URL, json={"question": question}, timeout=90)
        r.raise_for_status()
        return jsonify(r.json())
    except requests.exceptions.Timeout:
        return jsonify(error="n8n took too long to respond. Try again."), 504
    except Exception as e:
        return jsonify(error=f"Could not reach n8n: {e}"), 502


if __name__ == "__main__":
    # Cloud Run tells us which port to use via the PORT env variable.
    port = int(os.environ.get("PORT", 8080))
    print(f"\n  App running at  http://localhost:{port}\n")
    app.run(host="0.0.0.0", port=port, debug=True)
