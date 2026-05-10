import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = "http://localhost:3030"
sentiment_analyzer_url = "http://localhost:5050/"


def get_request(endpoint, **kwargs):
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"
        request_url = backend_url + endpoint + "?" + params
    else:
        request_url = backend_url + endpoint
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print("Network exception occurred", err)
        return []


def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url + "analyze/" + text
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print("Network exception occurred", err)
        return {"sentiment": "unknown"}


def post_review(data_dict):
    request_url = backend_url + "/insertReview"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as err:
        print("Network exception occurred", err)