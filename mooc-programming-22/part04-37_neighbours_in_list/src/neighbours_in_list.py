# Write your solution here
def longest_series_of_neighbours(my_list : list[int]) -> int:
    current_num = my_list[0]
    series = 1
    longest = 0
    for num in my_list:
        if current_num == num + 1 or current_num == num - 1:
            series += 1
            current_num = num
            if series > longest: 
                longest = series
        else:
            series = 1
            current_num = num


    return longest


"""model solution, i suppose is more "pythonic"--mine takes too much C++ 

def longest_series_of_neighbours(my_list: list):
    longest = 1
    result = 1
    for i in range(1, len(my_list)):
        # function abs calculates the absolute value
        if abs(my_list[i-1]-my_list[i]) == 1:
            result += 1
        else:
            result = 1
        # function max returns the highest of the parameters
        longest = max(longest, result)
    return longest

"""
