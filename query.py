import os
import requests
import json
from dotenv import load_dotenv

def generate_response(prompt):
    load_dotenv()
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise EnvironmentError("GEMINI_API_KEY not found in environment")
    
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"
    headers = {
        "Content-Type": "application/json"
    }
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        response_text = data['candidates'][0]['content']['parts'][0]['text']
        print("Response:\n")
        print(response_text)
        return response_text
    else:
        print("Error:", response.status_code)
        print(response.text)
        return None

if __name__ == "__main__":
    sample_text = "How many players are there in basketball ?"
    generate_response(sample_text)
