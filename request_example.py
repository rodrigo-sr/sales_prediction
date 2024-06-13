import requests

url = "http://127.0.0.1:8000/predict/"
data = {
    "country": "France",
    "month": 10,
    "day_of_week_numeric": 1
}

response = requests.post(url, json=data)
print(response.json())
