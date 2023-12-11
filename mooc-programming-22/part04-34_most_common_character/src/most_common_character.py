# Write your solution here
def most_common_character(my_str : str): 
    freq_char = ""
    for character in my_str:
        if freq_char == "" or my_str.count(freq_char) < my_str.count(character):
            freq_char = character
    
    return freq_char