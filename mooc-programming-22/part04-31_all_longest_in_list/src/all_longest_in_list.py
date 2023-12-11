# Write your solution here
def all_the_longest(my_list : list[str]) -> list[str]:
    this_list = []
    longest_word = ""
    for word in my_list: 
        if longest_word == "" or len(word) > len(longest_word):
            longest_word = word 
    

    for word in my_list:
        if len(longest_word) == len(word):
            this_list.append(word)


    return this_list


"""
def all_the_longest(names: list):
    result = []
 
    for name in names:
        if result == [] or len(name) > len(result[0]):
            result = [name]
        elif len(name) == len(result[0]):
            result.append(name)
 
    return result

### pythonic coding?
        if result == [] or len(name) > len(result[0]):
            result = [name]

    
"""