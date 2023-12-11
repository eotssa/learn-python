# Write your solution here
def list_sum(my_list1 : list, my_list2 : list):
    this_list = []
    for i in range(0, len(my_list1)): # recall that it doens't include 3
        result = my_list1[i] + my_list2[i]
        this_list.append(result)
    
    return this_list
        