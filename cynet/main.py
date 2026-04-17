from client import CynetAPIClient
from utils import save_to_json   # import this

def main():
    client = CynetAPIClient()

    print("\n--- Devices ---")
    devices = client.get_devices()
    print(devices)

    print("\n--- Alerts ---")
    alerts = client.get_alerts()
    print(alerts)

    print("\n--- Threats ---")
    threats = client.get_threats()
    print(threats)

    # COMBINE ALL DATA
    full_data = {
        "devices": devices,
        "alerts": alerts,
        "threats": threats
    }
    save_to_json(full_data, "cynet_mock.json")

if __name__ == "__main__":
    main()