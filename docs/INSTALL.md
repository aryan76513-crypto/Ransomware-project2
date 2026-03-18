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

    import React, { useEffect, useState } from "react";

function App() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("http://localhost:5000/alerts")
      .then(res => res.json())
      .then(data => setAlerts(data));
  }, []);

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-2xl font-bold mb-4">Ransomware & Data Leak Dashboard</h1>
      {alerts.map((alert, i) => (
        <div key={i} className="p-4 bg-red-200 rounded shadow mb-2">
          <h2 className="font-semibold">{alert.type}</h2>
          <p>{alert.message}</p>
          <p className="text-sm text-gray-600">Detected at: {alert.timestamp}</p>
        </div>
      ))}
    </div>
  );
}

export default App;

def detect_ransomware(file_content):
    if "encrypt" in file_content.lower():
        return True
    return False

    from model import detect_ransomware

sample = "User files are being encrypted..."
print("Ransomware Detected:", detect_ransomware(sample))