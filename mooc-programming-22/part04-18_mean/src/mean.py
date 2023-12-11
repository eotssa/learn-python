# Write your solution here
def mean(vals : list): 
    i = 0
    sum = 0
    while i < (len(vals)):
        sum += vals[i]
        i += 1
    
    return (sum / len(vals))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)



"""
def mean(my_list : list):
    return sum(my_list) / len(my_list)
"""