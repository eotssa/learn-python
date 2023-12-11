# Write your solution here
def no_shouting(my_list : list[str]) -> list[str]: 
    pruned_list = []
    for word in my_list:
        if word.isupper():
            continue
        else:
            pruned_list.append(word)
    
    return pruned_list