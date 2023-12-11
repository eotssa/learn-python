# Write your solution here
from random import shuffle
from random import choice

def roll(die: str):
    if die == "A":
        sides = [3, 3, 3, 3, 3, 6]
        shuffle(sides)
        return choice(sides)


    if die == "B":
        sides = [2, 2, 2, 5, 5, 5]
        shuffle(sides)
        return choice(sides)


    if die == "C":
        sides = [1, 4, 4, 4, 4, 4]
        shuffle(sides)
        return choice(sides)


def play(die1: str, die2: str, times: int):
    die1_win = 0
    die2_win = 0
    tie = 0

    for i in range(times):
        A = roll(die1)
        B = roll(die2)

        if A < B:
            die2_win += 1
        elif B < A:
            die1_win += 1
        else:
            tie += 1

        
    return (die1_win, die2_win, tie)