from api_client import fetch_api_data

def main():
    data = fetch_api_data()

    if data:
        print("Data fetched successfully!")
        print(data)

if __name__ == "__main__":
    main()