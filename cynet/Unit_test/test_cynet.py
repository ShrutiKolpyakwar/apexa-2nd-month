import pytest
from client import CynetAPIClient

@pytest.fixture
def client():
    return CynetAPIClient()

def test_get_devices(client):
    devices = client.get_devices()
    assert isinstance(devices, list)
    assert "hostname" in devices[0]

def test_get_alerts(client):
    alerts = client.get_alerts()
    assert isinstance(alerts, list)
    assert "severity" in alerts[0]

def test_get_threats(client):
    threats = client.get_threats()
    assert isinstance(threats, list)
    assert "type" in threats[0]