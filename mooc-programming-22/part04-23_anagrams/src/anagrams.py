# Write your solution here

def anagrams(senOne : str, senTwo : str):
    for i in senOne:
        if i in senTwo:
            continue
        else: 
            return False

    for i in senTwo:
        if i in senOne:
            continue
        else: 
            return False  
    
    if len(senOne) == len(senTwo): 
        return True
    else:
        return False


"""
bruh

return sorted(string1) == sorted(string2)
"""

