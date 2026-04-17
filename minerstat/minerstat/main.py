from client import APIClient
from config import BASE_URL, API_KEY, MAX_RETRIES

def main():
    client = APIClient(BASE_URL, API_KEY, MAX_RETRIES)

    data = client.get_data()

    if data:
        client.save_json(data)

if __name__ == "__main__":
    main()