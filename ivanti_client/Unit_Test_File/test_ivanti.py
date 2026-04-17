import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from client import IvantiAPIClient

@pytest.fixture
def client():
    """
    Creates a reusable IvantiAPIClient instance for all tests
    """
    return IvantiAPIClient("https://mock-api.com", "test_key")

def test_headers(client):
    """
    Verify Authorization header is correctly formed
    """
    headers = client.get_headers()
    
    assert "Authorization" in headers
    assert headers["Authorization"] == "Bearer test_key"
    assert headers["Content-Type"] == "application/json"

def test_get_vulnerabilities(client):
    """
    Ensure vulnerabilities data is returned correctly
    """
    data = client.get_vulnerabilities()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0
    assert "device" in data[0]
    assert "severity" in data[0]
    assert "cve" in data[0]
    
def test_get_devices(client):
    """
    Ensure devices data is returned correctly
    """
    data = client.get_devices()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "status" in data[0]

def test_get_users(client):
    """
    Ensure users data is returned correctly
    """
    data = client.get_users()

    assert data is not None
    assert isinstance(data, list)
    assert len(data) > 0
    assert "id" in data[0]
    assert "name" in data[0]
    assert "role" in data[0]

def test_api_failure(monkeypatch, client):
    """
    Simulate API failure and verify handling
    """
    def mock_fail(*args, **kwargs):
        return None
    # Replace client's get method with failure mock
    monkeypatch.setattr(client, "get", mock_fail)
    data = client.get_users()
    assert data is None