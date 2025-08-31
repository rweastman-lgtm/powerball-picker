import random

def pick_numbers(draws, strategy="random"):
    if strategy == "random":
        return random.sample(range(1, 70), 5) + [random.randint(1, 26)]
    # Add more strategies here
