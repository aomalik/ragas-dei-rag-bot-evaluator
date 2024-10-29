import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_deially(question):
    url = os.getenv('DEIALLY_API_URL') + "/chat/api/chat/"
    headers = {
        "Authorization": f"Api-key {os.getenv('DEIALLY_API_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "query": question
    }
    response = requests.post(url, json=payload, headers=headers)
    #print(response.json())
    if response.status_code == 200:
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError:
            print("Error: Response is not in JSON format")
            return None
    else:
        print(f"Error: Received response with status code {response.status_code}")
        print("Response content:", response.text)
        return None

#ask_deially("What is the capital of France?")