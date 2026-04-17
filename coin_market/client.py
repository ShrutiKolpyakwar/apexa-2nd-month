import requests
import time

class APIClient:
    def __init__(self, base_url, api_key, max_retries=3):
        self.base_url = base_url
        self.api_key = api_key
        self.max_retries = max_retries
        self.session = requests.Session()

    def authenticate(self):
        return {
            "X-CMC_PRO_API_KEY": self.api_key,
            "Accept": "application/json"
        }

    def refresh_token(self):
        print("Refreshing API key...")
        return "NEW_API_KEY"

    def get_data(self):
        headers = self.authenticate()
        params = {
            "start": "1",
            "limit": "10",
            "convert": "USD"
        }

        retries = 0
        wait_time = 2

        while retries < self.max_retries:
            try:
                response = self.session.get(
                    self.base_url,
                    headers=headers,
                    params=params
                )

                if response.status_code == 200:
                    print("Data fetched successfully")
                    return response.json()

                elif response.status_code == 401:
                    raise Exception("401 Unauthorized")

                elif response.status_code == 429:
                    print(f"Rate limit. Retrying in {wait_time}s...")
                    time.sleep(wait_time)

                elif response.status_code >= 500:
                    print(f"Server error {response.status_code}")
                    time.sleep(wait_time)

                else:
                    print(f"Error: {response.status_code}")
                    return None

                retries += 1
                wait_time *= 2

            except Exception as e:
                print("Exception:", e)

                if "401" in str(e):
                    print("Token expired. Refreshing...")
                    self.api_key = self.refresh_token()
                    headers = self.authenticate()
                    continue

                retries += 1
                time.sleep(wait_time)

        print("Max retries exceeded")
        return None