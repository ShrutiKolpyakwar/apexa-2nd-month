import requests
import time
import json

class APIClient:
    def __init__(self, base_url, api_key, max_retries=3):
        self.base_url = base_url
        self.api_key = api_key
        self.max_retries = max_retries
        self.session = requests.Session()

    # Authentication Header
    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.api_key}"
        }

    # GET Request
    def get_data(self):
        retries = 0
        wait_time = 2

        while retries < self.max_retries:
            try:
                response = self.session.get(
                    self.base_url,
                    headers=self.get_headers()
                )

                print("Status Code:", response.status_code)

                if response.status_code == 200:
                    print("Data fetched successfully")
                    return response.json()

                elif response.status_code == 401:
                    print("Unauthorized - Check API key")
                    print("Response:", response.text)
                    return None

                elif response.status_code == 429:
                    print(f"Rate limit hit. Retrying in {wait_time}s...")

                elif response.status_code >= 500:
                    print(f"Server error {response.status_code}, retrying...")

                else:
                    print("Error:", response.text)
                    return None

                retries += 1
                time.sleep(wait_time)
                wait_time *= 2

            except Exception as e:
                print("Exception:", e)
                retries += 1
                time.sleep(wait_time)

        print("Max retries exceeded")
        return None

    # Save JSON
    def save_json(self, data, filename="minerstat_data.json"):
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print("Data saved successfully")