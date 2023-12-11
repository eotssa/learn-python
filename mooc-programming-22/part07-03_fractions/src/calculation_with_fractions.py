# Write your solution here
import fractions

def fractionate(amount: int):

    this_lst = []
    for x in range(amount):
        this_lst.append(fractions.Fraction(1, amount))

    return this_lst