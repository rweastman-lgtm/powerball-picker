import pandas as pd
import requests
from bs4 import BeautifulSoup
import random

def fetch_powerball_data():
    # Placeholder: scrape and save to CSV
    with open('powerball_last_year.csv', 'w') as f:
        f.write("DrawDate,Numbers\n2025-08-10,5 12 23 34 56 22")

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
