import requests
from datetime import datetime, timedelta

def fetch_powerball_draws():
    base_url = "https://www.powerball.com/api/v1/numbers/powerball"
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)

    params = {
        "start": start_date.strftime("%Y-%m-%d"),
        "end": end_date.strftime("%Y-%m-%d")
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        raise Exception("Failed to fetch Powerball data")

    data = response.json()
    sorted_draws = sorted(data, key=lambda d: d["field_draw_date"])
    return sorted_draws

def print_oldest_draws(draws, count=3):
    print(f"\n📅 Oldest {count} Powerball draws:")
    for draw in draws[:count]:
        date = draw["field_draw_date"]
        numbers = draw["field_winning_numbers"]
        print(f"{date}: {numbers}")

if __name__ == "__main__":
    draws = fetch_powerball_draws()
    print_oldest_draws(draws)
