import streamlit as st
from powerball_picker import fetch_powerball_data, load_data, pick_numbers

st.title("🎯 Powerball Picker")

# Fetch and load data
def fetch_powerball_data():
    return fetch_powerball_draws()

def load_data(csv_path):
    import csv
    with open(csv_path, newline='') as f:
        reader = csv.reader(f)
        return [row for row in reader]

def pick_numbers(draws):
    # Dummy logic for now
    from collections import Counter
    all_nums = [int(n) for draw in draws for n in draw["field_winning_numbers"].split()]
    freq = Counter(all_nums)
    most_common = [num for num, _ in freq.most_common(6)]
    return most_common

if numbers:
    st.write(f"Your statistically picked numbers are: {numbers[:5]}")
    st.write(f"Powerball: {numbers[-1]}")
else:
   if not numbers:
    st.error("No valid Powerball numbers could be generated. Please check the CSV format and ensure it contains recent draws.")


