# Write your solution here
def times_ten(start_index: int, end_index: int):
    this_dictionary = {} 

    for i in range(start_index, end_index + 1):
        this_dictionary[i] = i * 10
    
    return this_dictionary