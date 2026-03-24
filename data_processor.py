def filter_market_data(data):
    if not data:
        return []

    if isinstance(data, dict):
        data = data.get("results", [])

    filtered = []

    for item in data:
        record = {
            "title": str(item.get("title", "")),
            "price": item.get("price", ""),
            "date": item.get("date", ""),
            "market": item.get("market", "")
        }

        filtered.append(record)

    return filtered