def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True
    
    # if character, remove left until we hit a bracket
    if not my_string[0] in "[]()":
        return balanced_brackets(my_string[1:])

    # if character, remove right until we hit a bracket
    if not my_string[-1] in "[]()":
        return balanced_brackets(my_string[:-1])


    if (my_string[0] == '(' and my_string[-1] == ')'):
        return balanced_brackets(my_string[1:-1])


    if (my_string[0] == '[' and my_string[-1] == ']'):
        return balanced_brackets(my_string[1:-1])

    return False




"""
def balanced_brackets(my_string: str) -> bool:
    # Remove non-bracket characters
    my_string = ''.join([char for char in my_string if char in '()[]'])
    
    # Base case: If string is empty, it's balanced
    if not my_string:
        return True

    # Check for and remove innermost bracket pairs
    new_string = my_string.replace('()', '').replace('[]', '')
    
    # If no pairs were removed, then it's unbalanced
    if new_string == my_string:
        return False

    # Otherwise, check the resulting string recursively
    return balanced_brackets(new_string)

"""