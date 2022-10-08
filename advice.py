import requests


def nice_advice():
    resp = requests.get("http://fucking-great-advice.ru/api/random")
    return resp.json()["text"]