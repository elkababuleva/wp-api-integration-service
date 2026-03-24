import requests
from config import API_BASE_URL


def fetch_market_data(market):
    try:
        params = {
            "market": market
        }

        response = requests.get(API_BASE_URL, params=params)

        if response.status_code == 200:
            return response.json()

        print(f"Error: {response.status_code}")
        return None

    except Exception as e:
        print(f"Request failed: {e}")
        return None