import os
import json

def get_mock_data():
    return {
        "devices": [
            {
                "id": "dev-001",
                "hostname": "DESKTOP-01",
                "ipAddress": "192.168.1.10",
                "os": "Windows 10",
                "status": "online"
            },
            {
                "id": "dev-002",
                "hostname": "SERVER-01",
                "ipAddress": "192.168.1.20",
                "os": "Linux",
                "status": "offline"
            }
        ],
        "alerts": [
            {
                "alertId": "alert-101",
                "severity": "High",
                "description": "Malware detected",
                "deviceId": "dev-001"
            },
            {
                "alertId": "alert-102",
                "severity": "Medium",
                "description": "Suspicious login attempt",
                "deviceId": "dev-002"
            }
        ],
        "threats": [
            {
                "threatId": "th-001",
                "type": "Ransomware",
                "status": "active"
            }
        ]
    }
def save_to_json(data, filename):
    try:
        import os, json
        os.makedirs("data", exist_ok=True)   # creates folder
        file_path = os.path.join("data", filename)

        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

        print(f"saved to {file_path}")
        return file_path

    except Exception as e:
        print(f"Error: {e}")