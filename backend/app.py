from flask import Flask, jsonify
import datetime

app = Flask(__name__)

alerts = [
    {
        "type": "Ransomware Activity",
        "message": "Suspicious encryption detected in user files.",
        "timestamp": str(datetime.datetime.now())
    },
    {
        "type": "Data Leak",
        "message": "Sensitive file accessed from unknown IP.",
        "timestamp": str(datetime.datetime.now())
    }
]

@app.route("/alerts", methods=["GET"])
def get_alerts():
    return jsonify(alerts)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
