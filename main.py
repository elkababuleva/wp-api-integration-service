from api_client import fetch_market_data
from data_processor import filter_market_data
from wp_client import send_to_wordpress
from config import MARKETS
import logging


def main():
    for market in MARKETS:
        print(f"Fetching: {market}")

        data = fetch_market_data(market)

        if not data:
            print("No data received")
            continue

        filtered = filter_market_data(data)

        print(f"Records: {len(filtered)}")

        send_to_wordpress(filtered, market)


if __name__ == "__main__":
    main()