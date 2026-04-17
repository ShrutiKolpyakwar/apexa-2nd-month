from client import APIClient
from config import BASE_URL, API_KEY
from utils import save_json

def main():
    client = APIClient(BASE_URL, API_KEY)

    data = client.get_data(query="python")

    if data:
        save_json(data)

if __name__ == "__main__":
    main()