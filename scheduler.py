import json
from flask import Flask, jsonify
from playstore_email_scraper import collect_emails

app = Flask(__name__)

def load_app_names_from_file(filename="app_names.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["app_names"]

@app.route("/", methods=["GET"])
def index():
    return jsonify({"status": "ok", "message": "Service is running."})

@app.route("/run", methods=["POST"])
def run_scraper():
    print("Received /run request")
    try:
        app_names = load_app_names_from_file()
        print(f"Loaded {len(app_names)} app names")
        emails = collect_emails(app_names)
        print(f"Collected {len(emails)} emails")
        return jsonify({"status": "done", "emails_collected": len(emails)})
    except Exception as e:
        print(f"Error in /run: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)