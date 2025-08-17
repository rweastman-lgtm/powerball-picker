import requests
import csv
from datetime import datetime, timedelta
from collections import Counter

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
        print("❌ Failed to fetch data.")
        return []

    data = response.json()
    with open("powerball_last_year.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["DrawDate", "Numbers"])
        for draw in data:
            date = draw["field_draw_date"]
         import re  # Add at the top if not already present

nums_raw = draw["field_winning_numbers"]
nums = re.findall(r'\d+', nums_raw)
writer.writerow([date, " ".join(nums)])

    print(f"✅ Saved {len(data)} draws to powerball_last_year.csv")
    return data

def load_data(filename):
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
        print(f"❌ File {filename} not found.")
    return draws

def pick_numbers(draws):
    main_nums = []
    powerballs = []
    for draw in draws:
        if len(draw) == 6:
            main_nums.extend(draw[:5])
            powerballs.append(draw[5])
    if not main_nums or not powerballs:
        print("⚠️ No valid numbers found in draw data.")
        return []

    main_freq = Counter(main_nums)
    powerball_freq = Counter(powerballs)

    top_main = [num for num, _ in main_freq.most_common(5)]
    top_powerball = powerball_freq.most_common(1)[0][0]

    print("🎯 Statistically picked numbers:", top_main + [top_powerball])
    return top_main + [top_powerball]

if __name__ == "__main__":
    fetch_powerball_data()
    draws = load_data("powerball_last_year.csv")
    if draws:
        pick_numbers(draws)
