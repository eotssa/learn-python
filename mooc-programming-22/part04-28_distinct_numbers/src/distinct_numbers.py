# Write your solution here
def distinct_numbers(my_list : list):
    this_list = []
    for i in my_list:
        if i not in this_list: 
            this_list.append(i)

    #this_list.sort()  
    #return this_list.sort() ## doesn't work. Recall what sort() does. It doesn't return anything. 
    return sorted(this_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))