import json
import os

def save_json(data, filename="crypto_data.json"):
    try:
        os.makedirs("data", exist_ok=True)

        file_path = os.path.join("data", filename)

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Data saved to {file_path}")

    except Exception as e:
        print(f"Error saving file: {e}")