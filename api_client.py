import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_api_data():
    try:
        response = requests.get(BASE_URL)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}")
            return None

    except Exception as e:
        print(f"Request failed: {e}")
        return None