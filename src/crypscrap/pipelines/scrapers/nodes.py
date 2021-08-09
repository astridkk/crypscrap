import requests


def crypcur_scraper():
    response = requests.get("https://oxylabs.io/")
    return response.text

