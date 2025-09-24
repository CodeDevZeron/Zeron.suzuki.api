import random
import string
from fastapi import FastAPI, Request
import requests

app = FastAPI()

API_URL = "https://suzuki.com.bd/signup"

# Random নাম বানানোর ফাংশন
def random_name(length=5):
    return ''.join(random.choices(string.ascii_letters, k=length))

# Random password বানানোর ফাংশন
def random_password(length=12):
    return (
        ''.join(random.choices(string.ascii_lowercase, k=4)) + "-" +
        ''.join(random.choices(string.ascii_lowercase, k=4)) + "-" +
        ''.join(random.choices(string.digits, k=4))
    )

@app.get("/signup")
def signup(request: Request, phone: str):
    # Random generate firstName, lastName, password
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
        "Accept": "text/x-component",
        "Content-Type": "application/json"
    }

    response = requests.post(API_URL, json=payload, headers=headers)
    return {
        "status": response.status_code,
        "response": response.json(),
        "used_data": payload[0]
    }
