# Write your solution here
def even_numbers(my_list : list):
    this_list = []
    for num in my_list:
        if num % 2 == 0:
            this_list.append(num)
    
    return this_list