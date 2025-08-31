import requests
from datetime import datetime, timedelta

def fetch_powerball_draws(days=365):
    base_url = "https://www.powerball.com/api/v1/numbers/powerball"
    end_date = datetime.today()
    start_date = end_date - timedelta(days=days)
    params = {
        "start": start_date.strftime("%Y-%m-%d"),
        "end": end_date.strftime("%Y-%m-%d")
    }
    response = requests.get(base_url, params=params)
    response.raise_for_status()
    data = response.json()
    return sorted(data, key=lambda d: d["field_draw_date"])
