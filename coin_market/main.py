from config import BASE_URL, API_KEY, MAX_RETRIES
from client import APIClient
from utils import save_json

def main():
    client = APIClient(BASE_URL, API_KEY, MAX_RETRIES)
    data = client.get_data()

    if data:
        save_json(data)

if __name__ == "__main__":
    main()