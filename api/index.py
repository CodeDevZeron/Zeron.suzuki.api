import random
import string
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

API_URL = "https://suzuki.com.bd/signup"

def random_name(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

def random_password():
    return (
        ''.join(random.choices(string.ascii_lowercase, k=4)) + "-" +
        ''.join(random.choices(string.ascii_lowercase, k=4)) + "-" +
        ''.join(random.choices(string.digits, k=4))
    )

@app.get("/signup")
def signup(phone: str):
    first_name = random_name()
    last_name = random_name()
    password = random_password()

    payload = [
        {
            "firstName": first_name,
            "lastName": last_name,
            "countryCode": "BD",
            "phone": phone,
            "email": "",
            "password": password,
            "confirmPassword": password,
            "otp": ""
        },
        "initial"
    ]

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)
        return JSONResponse({
            "status": response.status_code,
            "response": response.json() if response.headers.get("content-type","").startswith("application/json") else response.text,
            "used_data": payload[0]
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
