# Write your solution here
def longest(my_list : list) -> str: 
    longest = ""
    for this_string in my_list:
        if len(longest) < len(this_string):
            longest = this_string
    
    return longest