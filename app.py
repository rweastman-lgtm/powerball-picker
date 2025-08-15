import streamlit as st
from powerball_picker import fetch_powerball_data, load_data, pick_numbers

st.title("🎯 Smart Powerball Picker")
st.write("Scrapes last year's results and picks numbers using frequency, recency, and cluster logic.")

if st.button("Fetch Latest Data"):
    fetch_powerball_data()
    st.success("Data downloaded!")

if st.button("Pick Numbers"):
    draws = load_data('powerball_last_year.csv')
    st.write("Suggested Numbers:")
    pick_numbers(draws)
