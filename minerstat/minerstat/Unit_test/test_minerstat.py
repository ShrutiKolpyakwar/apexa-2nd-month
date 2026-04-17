import pytest
import sys
import os
# Fix import path to access parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from client import APIClient   # updated import (your new file)

# Mock Response Clas
class MockResponse:
    def __init__(self, status_code, json_data=None, text="error"):
        self.status_code = status_code
        self._json_data = json_data
        self.text = text

    def json(self):
        return self._json_data

# Test 1: SUCCESS (200)
def test_get_data_success(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(200, {"coins": ["BTC", "ETH"]})

    client = APIClient("dummy_url", "dummy_key")
    monkeypatch.setattr(client.session, "get", mock_get)

    data = client.get_data()
    assert data == {"coins": ["BTC", "ETH"]}

# Test 2: UNAUTHORIZED (401)
def test_get_data_unauthorized(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(401, text="Unauthorized")

    client = APIClient("dummy_url", "dummy_key")
    monkeypatch.setattr(client.session, "get", mock_get)

    data = client.get_data()
    assert data is None

# Test 3: RATE LIMIT (429)
def test_get_data_rate_limit(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(429)

    client = APIClient("dummy_url", "dummy_key", max_retries=2)
    monkeypatch.setattr(client.session, "get", mock_get)

    data = client.get_data()
    assert data is None

# Test 4: SERVER ERROR (500)
def test_get_data_server_error(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse(500)

    client = APIClient("dummy_url", "dummy_key", max_retries=2)
    monkeypatch.setattr(client.session, "get", mock_get)

    data = client.get_data()
    assert data is None

# Test 5: EXCEPTION CASE
def test_get_data_exception(monkeypatch):
    def mock_get(*args, **kwargs):
        raise Exception("Network error")

    client = APIClient("dummy_url", "dummy_key", max_retries=2)
    monkeypatch.setattr(client.session, "get", mock_get)

    data = client.get_data()
    assert data is None