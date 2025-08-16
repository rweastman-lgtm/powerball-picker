import pandas as pd
import requests
from bs4 import BeautifulSoup
import random

import requests
import csv
from datetime import datetime, timedelta

def fetch_powerball_data():
    base_url = "https://www.powerball.com/api/v1/numbers/powerball"
    end_date = datetime.today()
    start_date = end_date - timedelta(days=365)

    params = {
        "start": start_date.strftime("%Y-%m-%d"),
        "end": end_date.strftime("%Y-%m-%d")
    }

    response = requests.get(base_url, params=params)
    if response.status_code != 200:
        print("Failed to fetch data.")
        return

    data = response.json()
    with open("powerball_last_year.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["DrawDate", "Numbers"])
        for draw in data:
            date = draw["field_draw_date"]
            nums = draw["field_winning_numbers"].replace(",", "")
            writer.writerow([date, nums])
    print(f"✅ Saved {len(data)} draws to powerball_last_year.csv")

def load_data(filename):
    import csv
    draws = []
    try:
        with open(filename, newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                try:
                    nums = [int(n) for n in row[1].split()]
                    if len(nums) == 6:
                        draws.append(nums)
                except ValueError:
                    continue
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return draws


def pick_numbers(draws):
    from collections import Counter
    import random

    flat = [num for draw in draws for num in draw]
    freq = Counter(flat)
    top = [num for num, _ in freq.most_common(5)]
    powerball = random.randint(1, 26)
    return top + [powerball]

    print("Your numbers:", top + [powerball])
