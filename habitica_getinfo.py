import requests
import json

import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Ditt Habitica-konto
USER_ID = os.getenv("USER_ID")
API_TOKEN = os.getenv("API_TOKEN")

url = "https://habitica.com/api/v3/tasks/user?type=todos"

headers = {
    "x-api-user": USER_ID,
    "x-api-key": API_TOKEN,
    "Content-Type": "application/json",
    "Accept-Language": "en"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:


    data = response.json()
    #print(json.dumps(data, indent=2))  # Snygg struktur
    for todo in data['data']:
        print(f"🔸 {todo['text']}")

    #int(f"{'✅' if is_owner else '❌'} {ch['name']} → {ch['_id']}")
else:
    print("Fel vid anrop:", response.status_code)
    print(response.text)