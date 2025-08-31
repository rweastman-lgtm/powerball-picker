import requests
from datetime import datetime, timedelta

POWERBALL_URL = "https://data.ny.gov/resource/d6yy-54nr.json"

def fetch_powerball_draws(limit=10):
    params = {"$limit": limit, "$order": "draw_date DESC"}
    response = requests.get(POWERBALL_URL, params=params)
    response.raise_for_status()
    data = response.json()
    return [
        {
            "draw_date": d["draw_date"],
            "white_balls": d["winning_numbers"].split()[:5],
            "powerball": d["winning_numbers"].split()[5],
            "multiplier": d.get("multiplier", "1")
        }
        for d in data
    ]

