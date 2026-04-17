import requests

class APIClient:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def authenticate(self):
        return {
            "Content-Type": "application/json"
        }

    def get_data(self, query="technology"):
        params = {
            "apikey": self.api_key,
            "q": query,
            "country": "in",
            "language": "en"
        }

        try:
            response = requests.get(
                self.base_url,
                headers=self.authenticate(),
                params=params
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 401:
                print("Invalid API key")
            else:
                print("Error:", response.status_code, response.text)

        except Exception as e:
            print("Request failed:", e)

        return None