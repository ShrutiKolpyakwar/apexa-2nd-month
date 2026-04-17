import sys
import os
import pytest
from unittest.mock import patch
import requests

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from client import TMDBClient

BASE_URL = "https://api.themoviedb.org/3"
ACCESS_TOKEN = "test_token"

@pytest.fixture
def client():
    return TMDBClient(BASE_URL, ACCESS_TOKEN)

# Mock Response
class MockResponse:
    def __init__(self, data):
        self.data = data

    def json(self):
        return self.data

    def raise_for_status(self):
        pass

mock_data = {
    "id": 11,
    "title": "Star Wars",
    "genres": [{"id": 1, "name": "Action"}],
    "videos": {},
    "credits": {}
}

# TEST 1: get_headers()
def test_get_headers(client):
    headers = client.get_headers()

    assert headers["Authorization"] == f"Bearer {ACCESS_TOKEN}"
    assert headers["Content-Type"] == "application/json"

# TEST 2: fetch_movie_data SUCCESS

@patch("requests.Session.get")
def test_fetch_success(mock_get, client):
    mock_get.return_value = MockResponse(mock_data)

    data = client.fetch_movie_data(11)

    assert data["id"] == 11
    assert data["title"] == "Star Wars"

# TEST 3: fetch_movie_data FAILURE

@patch("requests.Session.get")
def test_fetch_failure(mock_get, client):
    mock_get.side_effect = requests.exceptions.RequestException("API Error")

    data = client.fetch_movie_data(11)
    assert data is None