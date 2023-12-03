from fastapi.testclient import TestClient
from app.__main__ import app

client = TestClient(app)

def test_ip_api_geo_resolver():
    response = client.post("/location", json={"reqId": "reqId-test", "ip": "8.8.8.8"})
    assert response.status_code == 200
    response_data = response.json()
    assert response_data["countryCode"] == "US"
    assert response_data["lat"] == 39.03
    assert response_data["lon"] == -77.5
