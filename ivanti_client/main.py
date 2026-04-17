from client import IvantiAPIClient
from config import BASE_URL, API_KEY

def main():
    client = IvantiAPIClient(BASE_URL, API_KEY)

    print("\n Vulnerabilities")
    vulnerabilities = client.get_vulnerabilities(save=True)
    print(vulnerabilities)

    print("\n Users ")
    users = client.get_users(save=True)
    print(users)
    
    print("\n Devices ")
    devices = client.get_devices(save=True)
    print(devices)

if __name__ == "__main__":
    main()