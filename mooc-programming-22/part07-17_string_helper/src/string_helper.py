# Write your solution here
def change_case(orig_string: str):
     return orig_string.swapcase()


def split_in_half(orig_string: str):
    length = len(orig_string)
    return (orig_string[:length // 2], orig_string[length // 2:])
    
def remove_special_characters(orig_string: str):
    # creates a list of characters that fit the requirements, then join() creates a string. 
    return ''.join(c for c in orig_string if c.isalpha() or c.isdigit() or c.isspace())
