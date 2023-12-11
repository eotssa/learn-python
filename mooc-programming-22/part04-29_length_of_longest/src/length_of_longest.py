# Write your solution here

def length_of_longest(my_list : list[str]):
    val = len(my_list[0])
    i = 1
    for i in my_list:
        if val < len(i):
            val = len(i)
    
    return val

