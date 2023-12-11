# Write your solution here


def histogram(my_str : str):
    this_dict = {}

    for letter in my_str:
        if letter not in this_dict: # if this letter is not a key
            this_dict[letter] = 0

        this_dict[letter] += 1
    
    for key, value in this_dict.items(): 
        print(key, end="")
        print(" ", end="")
        print("*" * value)
