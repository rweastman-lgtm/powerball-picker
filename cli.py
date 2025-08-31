from powerball_picker.fetcher import fetch_powerball_draws
from powerball_picker.picker import pick_numbers
from powerball_picker.utils import print_draws

def main():
    draws = fetch_powerball_draws()
    print_draws(draws)
    picks = pick_numbers(draws)
    print(f"\n🎯 Your Powerball picks: {picks}")

if __name__ == "__main__":
    main()
