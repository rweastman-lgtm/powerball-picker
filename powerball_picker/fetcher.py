import requests
from datetime import datetime

POWERBALL_URL = "https://data.ny.gov/resource/d6yy-54nr.json"

def fetch_powerball_draws(limit=10, separator="-"):
    params = {"$limit": limit, "$order": "draw_date DESC"}
    response = requests.get(POWERBALL_URL, params=params)
    response.raise_for_status()
    data = response.json()

    draws = []
    for d in data:
        # Truncate date to YYYY-MM-DD
        draw_date = datetime.strptime(d["draw_date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%Y-%m-%d")
        numbers = d["winning_numbers"].split()
        white_balls = separator.join(numbers[:5])
        powerball = numbers[5]
        multiplier = d.get("multiplier", "1")

        draws.append({
            "draw_date": draw_date,
            "numbers": f"{white_balls} {separator} {powerball}",
            "multiplier": multiplier
        })

    return draws

