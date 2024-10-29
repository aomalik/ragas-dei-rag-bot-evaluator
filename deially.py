import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_deially(question):
    url = os.getenv('DEIALLY_API_URL')
    headers = {
        "Authorization": f"Api-key {os.getenv('DEIALLY_API_KEY')}/chat/api/chat/",
        "Content-Type": "application/json"
    }
    payload = {
        "query": question
    }
    response = requests.post(url, json=payload, headers=headers)
    #print(response.json())
    return response.json()

ask_deially("What is the capital of France?")