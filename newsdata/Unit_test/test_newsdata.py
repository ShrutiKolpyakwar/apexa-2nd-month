import pytest
from client import APIClient

BASE_URL = "https://newsdata.io/api/1/news"
API_KEY = "test_key"

@pytest.fixture
def client():
    return APIClient(BASE_URL, API_KEY)

def test_authenticate(client):
    headers = client.authenticate()
    assert headers["Content-Type"] == "application/json"

def test_get_data_invalid_key(client):
    data = client.get_data("python")
    assert data is None