#import todo från lista Habitica
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Ditt Habitica-konto
USER_ID = os.getenv("USER_ID")
API_TOKEN = os.getenv("API_TOKEN")



# 📋 Lista med uppgifter du vill importera
todo_list = [
    "Rensa garderoben",
    "Släng gamla papper",
    "Sortera elektronik",
    "Gå igenom förrådet"
]

# 📬 Habiticas API-endpoint för nya To-Dos
url = 'https://habitica.com/api/v3/tasks/user'

headers = {
    'x-api-user': USER_ID,
    'x-api-key': API_TOKEN,
    'Content-Type': 'application/json'
}

for task in todo_list:
    payload = {
        "type": "todo",
        "text": task,
        "notes": "Importerad via script",
        "priority": 1.5  # Standard = 1.0. Du kan justera.
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        print(f"✅ Skapade: {task}")
    else:
        print(f"❌ Fel för '{task}': {response.status_code} - {response.text}")
