# Write your solution here
def even_numbers(beginning: int, maximum: int):
    for i in range (beginning, maximum + 1):
        if i % 2 == 0: 
            yield i


# model solution 
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2
 