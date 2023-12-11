# Write your solution here
from random import sample


def lottery_numbers(amount: int, lower: int, upper: int):
    number_pool = list(range(lower, upper))
    weekly_draw = sample(number_pool, amount)

    return sorted(weekly_draw)


