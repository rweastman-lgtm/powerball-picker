import streamlit as st
from powerball_picker import fetch_powerball_data, load_data, pick_numbers

st.title("🎯 Powerball Picker")

# Fetch and load data
fetch_powerball_data()
draws = load_data("powerball_last_year.csv")
numbers = pick_numbers(draws)

if numbers:
    st.write(f"Your statistically picked numbers are: {numbers[:5]}")
    st.write(f"Powerball: {numbers[-1]}")
else:
    st.warning("No valid Powerball numbers could be generated. Please check the data source.")





