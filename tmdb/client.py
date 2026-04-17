import requests

class TMDBClient:
    def __init__(self, base_url, access_token):
        self.base_url = base_url
        self.access_token = access_token
        self.session = requests.Session()

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }

    def fetch_movie_data(self, movie_id):
        endpoint = f"{self.base_url}/movie/{movie_id}"
        params = {
            "append_to_response": "videos,credits"
        }

        try:
            response = self.session.get(
                endpoint,
                headers=self.get_headers(),
                params=params
            )
            response.raise_for_status()
            return response.json()

        except requests.exceptions.RequestException as e:
            print("Error fetching data:", e)
            return None