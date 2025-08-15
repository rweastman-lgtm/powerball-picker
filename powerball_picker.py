import pandas as pd
import requests
from bs4 import BeautifulSoup
import random

def fetch_powerball_data():
    # Placeholder: scrape and save to CSV
    with open('powerball_last_year.csv', 'w') as f:
        f.write("DrawDate,Numbers\n2025-08-10,5 12 23 34 56 22")

def load_data(filepath):
    df = pd.read_csv(filepath)
    draws = [list(map(int, row.split())) for row in df['Numbers']]
    return draws

def pick_numbers(draws):
    # Simple frequency-based picker
    from collections import Counter
    flat = [num for draw in draws for num in draw]
    freq = Counter(flat)
    top = [num for num, _ in freq.most_common(5)]
    powerball = random.randint(1, 26)
    print("Your numbers:", top + [powerball])
