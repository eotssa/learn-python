# Write your solution here
def no_vowels(my_str : str) -> str: 
    vowels = "aeiou"
    for vowel in vowels: 
        my_str = my_str.replace(vowel, "")
    
    return my_str


"""
def no_vowels(my_string: str):
    vowels = "aeiou"
    result = ""
 
    for letter in my_string:
        if letter not in vowels:
            result += letter
 
    return result
    """