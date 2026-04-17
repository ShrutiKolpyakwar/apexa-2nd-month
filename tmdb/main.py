from config import BASE_URL, ACCESS_TOKEN
from client import TMDBClient
from utils import save_json

def main():
    client = TMDBClient(BASE_URL, ACCESS_TOKEN)

    movie_id = 11   # Example: Star Wars
    data = client.fetch_movie_data(movie_id)

    if data:
        save_json(data)

if __name__ == "__main__":
    main()