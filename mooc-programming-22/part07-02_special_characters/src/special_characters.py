# Write your solution here
import string

def separate_characters(my_string: str):
    tuple1 = ""
    tuple2 = ""
    tuple3 = ""
    
    for char in my_string:
        if char in string.ascii_letters:
            tuple1 += char
        elif char in string.punctuation:
            tuple2 += char
        else:
            tuple3 += char
        
    
    return (tuple1, tuple2, tuple3)
#string.ascii_letters
#string.punctuation
#all other