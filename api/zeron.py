import random
import string
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

API_URL = "https://suzuki.com.bd/signup?goback=%2F?"

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
        "Accept": "text/x-component",
        "Content-Type": "application/json",
        "Next-Action": "b45aa2700649f9fa8fb8befec1519c7f2b4c2192",   # ডাইনামিকও হতে পারে
        "Next-Router-State-Tree": "%5B%22%22%2C%7B%22children%22%3A%5B%22(authentication)%22%2C%7B%22children%22%3A%5B%22signup%22%2C%7B%22children%22%3A%5B%22__PAGE__%3F%7B%5C%22goback%5C%22%3A%5C%22%2F%3F%5C%22%7D%22%2C%7B%7D%5D%7D%5D%7D%5D%7D%2Cnull%2Cnull%2Ctrue%5D",
        "Next-Url": "/signup"
      
    }

    try:
        response = requests.post(API_URL, json=payload, headers=headers)

        content_type = response.headers.get("content-type", "")
        if "application/json" in content_type or response.text.strip().startswith("{"):
            data = response.json()
        else:
            data = {"raw_html": response.text[:500]}  # debug purpose

        return JSONResponse({
            "status": response.status_code,
            "response": data,
            "used_data": payload[0]
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
