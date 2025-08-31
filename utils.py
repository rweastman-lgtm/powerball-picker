def print_draws(draws, count=3):
    print(f"\n📅 Oldest {count} Powerball draws:")
    for draw in draws[:count]:
        date = draw["field_draw_date"]
        numbers = draw["field_winning_numbers"]
        print(f"{date}: {numbers}")
