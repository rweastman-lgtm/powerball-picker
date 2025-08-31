import streamlit as st
from powerball_picker.fetcher import fetch_powerball_draws
from powerball_picker.picker import pick_numbers

st.title("🎱 Powerball Picker")
draws = fetch_powerball_draws()
st.write("Recent Draws", draws[:3])
strategy = st.selectbox("Pick Strategy", ["random"])
if st.button("Generate Numbers"):
    picks = pick_numbers(draws, strategy)
    st.success(f"Your Powerball picks: {picks}")
