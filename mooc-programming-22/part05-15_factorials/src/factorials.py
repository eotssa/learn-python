# Write your solution here
def factorials(n: int):
    num = 1
    this_dict = {} 
    for i in range(1, n + 1):
        num *= i
        this_dict[i] = num

    return this_dict