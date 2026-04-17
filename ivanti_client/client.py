import requests
from utils import get_mock_data, save_to_json

class IvantiAPIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()

    # Headers 
    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    # MOCK GET METHOD
    def get(self, endpoint, params=None):
        print(f"[MOCK] API called: {endpoint}")
        data = get_mock_data()

        if "vulnerability" in endpoint:
            return data["vulnerabilities"]
        elif "machines" in endpoint:
            return data["devices"]
        elif "users" in endpoint:
            return data["users"]
        return None

    # API METHODS
    def get_vulnerabilities(self, save=True):
        endpoint = "/api/patch/content/v1/endpoint-vulnerability"
        data = self.get(endpoint)

        if save and data:
            save_to_json(data, "vulnerabilities.json")
        return data

    def get_devices(self, save=True):
        endpoint = "/st/console/api/v1.0/patch/machines"
        data = self.get(endpoint)

        if save and data:
            save_to_json(data, "devices.json")
        return data

    def get_users(self, save=True):
        endpoint = "/api/v1/configuration/users"
        data = self.get(endpoint)

        if save and data:
            save_to_json(data, "users.json")
        return data