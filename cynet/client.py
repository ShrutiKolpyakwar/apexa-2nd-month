import requests
from config import BASE_URL, API_KEY, USE_MOCK, TIMEOUT
from utils import get_mock_data

class CynetAPIClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.api_key = API_KEY

    def _headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}" if self.api_key else "",
            "Content-Type": "application/json"
        }

    def get_devices(self):
        if USE_MOCK:
            return get_mock_data()["devices"]

        url = f"{self.base_url}/devices"
        response = requests.get(url, headers=self._headers(), timeout=TIMEOUT)
        return response.json()

    def get_alerts(self):
        if USE_MOCK:
            return get_mock_data()["alerts"]

        url = f"{self.base_url}/alerts"
        response = requests.get(url, headers=self._headers(), timeout=TIMEOUT)
        return response.json()

    def get_threats(self):
        if USE_MOCK:
            return get_mock_data()["threats"]

        url = f"{self.base_url}/threats"
        response = requests.get(url, headers=self._headers(), timeout=TIMEOUT)
        return response.json()