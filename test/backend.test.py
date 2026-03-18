import requests

def test_alerts_endpoint():
    response = requests.get("http://localhost:5000/alerts")
    assert response.status_code == 200
    data = response.json()
    assert "type" in data[0]
    assert "message" in data[0]