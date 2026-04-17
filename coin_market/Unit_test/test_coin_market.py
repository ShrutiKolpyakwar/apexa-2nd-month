import pytest
import sys
import os

# Fix import path to access project files
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from client import APIClient   # updated import

# Fixture (common test object)
@pytest.fixture
def client():
    return APIClient(
        "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",
        "test_key",
        max_retries=3
    )

# 1. Test Authentication
def test_authenticate(client):
    headers = client.authenticate()

    assert headers["X-CMC_PRO_API_KEY"] == "test_key"
    assert headers["Accept"] == "application/json"

# 2. Test Token Refresh
def test_refresh_token(client):
    new_key = client.refresh_token()

    assert new_key == "NEW_API_KEY"

# 3. Test Successful API Call
def test_get_data_success(client, monkeypatch):

    # Mock response (simulate API success)
    class MockResponse:
        status_code = 200

        def json(self):
            return {"status": "success"}

    # Replace actual API call
    monkeypatch.setattr(client.session, "get", lambda *a, **k: MockResponse())

    result = client.get_data()

    assert result == {"status": "success"}

# 4. Test 401 → Retry → Success
def test_get_data_401(client, monkeypatch):

    responses = [401, 200]  # first fails, then succeeds

    class MockResponse:
        def __init__(self, status):
            self.status_code = status

        def json(self):
            return {"ok": True}

    def mock_get(*args, **kwargs):
        status = responses.pop(0)
        return MockResponse(status)

    # Mock API
    monkeypatch.setattr(client.session, "get", mock_get)

    result = client.get_data()

    assert result == {"ok": True}