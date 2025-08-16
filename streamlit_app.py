import streamlit as st
from powerball_picker import fetch_powerball_data, load_data, pick_numbers

st.title("🎯 Smart Powerball Picker")
st.write("Scrapes last year's results and picks numbers using frequency, recency, and cluster logic.")

if st.button("Fetch Latest Data"):
    fetch_powerball_data()
    st.success("Data downloaded!")

draws = load_data('powerball_last_year.csv')
st.write(f"Loaded {len(draws)} draws")
st.write(draws[:5])  # Show sample

if st.button("Pick Numbers"):
    numbers = pick_numbers(draws)
    st.write("🎯 Suggested Numbers:")
    st.write(f"Main: {numbers[:-1]}")
    st.write(f"Powerball: {numbers[-1]}")





