from fastapi import FastAPI
from fastapi.responses import JSONResponse
import requests

app = FastAPI()

# === Chaldal API endpoints ===
API_1 = "https://chaldal.com/yolk/api-v4/ContactUs/SendAppDownloadLink"
API_2 = "https://chaldal.com/yolk/api-v4/Auth/RequestOtpWithApiKey"

# === Common headers ===
HEADERS = {
    "X-Egg-StoreId": "1",
    "X-Egg-ClientApp": "Omelette",
    "X-Egg-Platform": "Browser",
    "Accept": "application/json",
    "Content-Type": "application/json"
}

@app.get("/api1")
def api1(phone: str, apiKey: str):
    url = f"{API_1}?apiKey={apiKey}&phoneNumber=%2B88{phone}"
    try:
        response = requests.post(url, headers=HEADERS, json={})
        return JSONResponse({
            "status": response.status_code,
            "response": response.json() if response.headers.get("content-type","").startswith("application/json") else response.text
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@app.get("/api2")
def api2(phone: str, apiKey: str, retry: int = 0):
    url = f"{API_2}?apiKey=0cAFcWeA5U5tMlqSCe5wuP-SFvHya21IHq_D7N_hxtDMP1GPQEaALOorzSpi-SVVakT5gunr5rgx5oaAeGsBcsd__9i_pOVMiok7IYgZFIDgEWCX8KNwc1y0uk8buGlvgsMY_No-M65G3JNJCHTPfFYRnxChdX3bJMNmGDVBtPpGYozVPAdCPXMU1dKu_GdODB1RdiOGmgbeW8sUNU-eaCF0yXcTVknmqTityznrlDTQIqTT115RMADCcDwoiQUCIBYMQzOhtZHG-hLa-9IblrLeVvXPQ3z7yNqX1lFslsjcmSlHFT2Ku1memZc0gMEedM5UEL8dvbrMKn2I3_FSchlPHTo_yt8BOX8PP_SvKcyQrXa41uE-re_G-u3kHIH3d4w714okOGjVo2XRgmWJbV2-QNaz9duTy3QTfovLKDC5ADYyLWS3TjtbNq_jWMCb9KV0gmG3ysbmagS49YtFrkd1gQes9r6_qmOboTwVavxx67tVwqcdrgKGRrW2r51HE4F6qdvve8eRGsrJF9LMkY0an1U75a6htNMF8EeZitcK6WXsh6zH818rZOGYR29j07fW_-qvV4DaTc_0VJcpXmSYBGYz8bnZST0A-rhIOjWGAiKuZ3ZdvvNnkaJnNgWpGw_5vwr-NpFUCHoMCNkuqBmkG2N-CJij9-pVTLEIhut7cNZoA2yX8dQqMJZA7L8kjggC5W7-1epD1xtcFOtqnEODdiNCnH9QogNAsE9BP5nk0lZS73vHoCgSh-pkoz-Oe1C0Fq5i6tZx9c6aeVGIYfgRin81RP7uNwwugbymqIrC61eFIUUwJHgkRsoAvyYuWmtLRy5ydR4VWv&phoneNumber=%2B88{phone}&retryAttempt={retry}"
    try:
        response = requests.post(url, headers=HEADERS, json={})
        return JSONResponse({
            "status": response.status_code,
            "response": response.json() if response.headers.get("content-type","").startswith("application/json") else response.text
        })
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
