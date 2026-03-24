import requests
from config import WP_API_URL, WP_USER, WP_PASSWORD


def send_to_wordpress(data, market):
    if not data:
        return

    for item in data[:3]:
        post = {
            "title": f"{market} market update",
            "content": str(item),
            "status": "draft"
        }

        try:
            response = requests.post(
                WP_API_URL,
                json=post,
                auth=(WP_USER, WP_PASSWORD)
            )

            print("Sent:", response.status_code)

        except Exception as e:
            print("WP error:", e)