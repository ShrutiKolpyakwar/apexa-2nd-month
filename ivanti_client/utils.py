import json
import os
def get_mock_data():
    return {
    "vulnerabilities": [
        {
            "device": "Laptop-1",
            "severity": "High",
            "cve": "CVE-2024-1234",
            "description": "Remote code execution vulnerability",
            "status": "Open"
        },
        {
            "device": "Server-1",
            "severity": "Medium",
            "cve": "CVE-2024-5678",
            "description": "Privilege escalation issue",
            "status": "In Progress"
        },
        {
            "device": "Desktop-3",
            "severity": "Low",
            "cve": "CVE-2023-9987",
            "description": "Information disclosure vulnerability",
            "status": "Resolved"
        },
        {
            "device": "Database-Server",
            "severity": "Critical",
            "cve": "CVE-2025-1111",
            "description": "SQL injection vulnerability",
            "status": "Open"
        }
    ],

    "devices": [
        {
            "id": "123",
            "name": "Device-A",
            "type": "Laptop",
            "status": "Active",
            "os": "Windows 11"
        },
        {
            "id": "124",
            "name": "Device-B",
            "type": "Server",
            "status": "Inactive",
            "os": "Linux"
        },
        {
            "id": "125",
            "name": "Device-C",
            "type": "Desktop",
            "status": "Active",
            "os": "Windows 10"
        },
        {
            "id": "126",
            "name": "Device-D",
            "type": "Database Server",
            "status": "Active",
            "os": "Ubuntu"
        }
    ],

    "users": [
        {
            "id": "1",
            "name": "Shruti",
            "role": "Admin",
            "email": "shruti@example.com",
            "status": "Active"
        },
        {
            "id": "2",
            "name": "User-2",
            "role": "Viewer",
            "email": "user2@example.com",
            "status": "Active"
        },
        {
            "id": "3",
            "name": "User-3",
            "role": "Analyst",
            "email": "user3@example.com",
            "status": "Inactive"
        },
        {
            "id": "4",
            "name": "User-4",
            "role": "Manager",
            "email": "user4@example.com",
            "status": "Active"
        }
    ]
}

def save_to_json(data, filename):
    try:
        os.makedirs("data", exist_ok=True)
        file_path = os.path.join("data", filename)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        print(f"Saved to {file_path}")
        return file_path

    except Exception as e:
        print(f"Error saving file: {e}")
        return None