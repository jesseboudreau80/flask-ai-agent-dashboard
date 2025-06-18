# agents/geocode.py

import requests
import os

def get_jurisdiction(address):
    api_key = os.getenv("OPENCAGE_API_KEY")
    if not api_key:
        return "Missing OpenCage API key in environment."

    url = "https://api.opencagedata.com/geocode/v1/json"
    params = {
        "q": address,
        "key": api_key,
        "no_annotations": 1,
        "language": "en",
    }

    response = requests.get(url, params=params)
    data = response.json()

    if not data['results']:
        return "Could not determine jurisdiction from the address."

    components = data['results'][0]['components']

    return {
        "city": components.get("city") or components.get("town") or components.get("village"),
        "county": components.get("county"),
        "state": components.get("state"),
        "postcode": components.get("postcode"),
        "country": components.get("country"),
        "formatted": data['results'][0]['formatted']
    }
