# Write your solution here
def invert(dictionary: dict):
    list_key = []
    list_value = []
    for key, value in dictionary.items():
        list_key.append(key)
        list_value.append(value)

    dictionary.clear()

    for key, value in zip(list_key, list_value):
        dictionary[value] = key



"""          - following doesn't work b/c can't iterate over a changing size 
    for key, value in dictionary.items():
        del dictionary[key]
        dictionary[value] = key
    
    return dictionary
"""