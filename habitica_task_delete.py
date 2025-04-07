#import todo från lista Habitica
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# 🔐 Ditt Habitica-konto
USER_ID = os.getenv("USER_ID")
API_TOKEN = os.getenv("API_TOKEN")


# 📬 Habiticas API-endpoint för nya To-Dos
url = 'https://habitica.com/api/v3/tasks/user'
url_challenge = 'https://habitica.com/api/v3/challenges/user'


headers = {
    'x-api-user': USER_ID,
    'x-api-key': API_TOKEN,
    'Content-Type': 'application/json'
}

#response = requests.post(url, json=payload, headers=headers)
#response = requests.get(url, headers=headers, type="todos")

#get all owend challenges
#response = requests.get(url_challenge, headers=headers, params={"page": 0, "owned": "true"}, )

#print(response.json())
#print(f"Status: {response.status_code}")
#print(response.text)

#Loopa alla sidor och lsta det
page = 0
while True:
    response = requests.get(
        url_challenge,
        headers=headers,
        params={"page": page, "owned": "true"}
    )
    
    data = response.json().get("data", [])

    if not data:
        break  # Inga fler sidor

    print(f"📄 Sida {page}")
    for ch in data:
        is_owner = ch["leader"]["_id"] == USER_ID
        print(f"{'✅' if is_owner else '❌'} {ch['name']} → {ch['_id']}")

    page += 1  # Hämta nästa sida


#print(f"Status: {response.status_code}")
#data = response.json().get("data", [])

#for ch in data:
#    leader_id = ch["leader"]["_id"]
#    is_owner = (leader_id == USER_ID)
#    print(f"{'✅' if is_owner else '❌'} {ch['name']} → ID: {ch['_id']}")

#if response.status_code == 201:
#    print(f"✅ Skapade: {task}")
#else:
#    print(f"❌ Fel för '{task}': {response.status_code} - {response.text}")
