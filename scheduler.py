import json
from flask import Flask, jsonify
from playstore_email_scraper import collect_emails

app = Flask(__name__)


def pop_next_app_name(filename="app_names.json"):
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    if not data["app_names"]:
        return None
    app_name = data["app_names"].pop(0)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    return app_name


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
        app_name = pop_next_app_name()
        if not app_name:
            print("No more app names to process.")
            return jsonify({"status": "done", "message": "No more app names to process."})
        print(f"Processing: {app_name}")
        emails = collect_emails([app_name])
        print(f"Collected {len(emails)} emails")
        return jsonify({"status": "done", "app_name": app_name, "emails_collected": len(emails)})
    except Exception as e:
        print(f"Error in /run: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)