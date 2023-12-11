# Write your solution here
def shortest(my_list : list[str]) -> str:
    shortest_name = my_list[0]
    for name in my_list:
        if len(shortest_name) > len(name):
            shortest_name = name
    
    return shortest_name


""" notice how the if statement accounts for the first one, compared to my C++ way 
### "pythonic coding?" 
def shortest(names: list):
    result = ""
 
    for nimi in names:
        if result == "" or len(nimi) < len(result):
            result = nimi
 
    return result
"""