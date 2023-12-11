# Write your solution here
def everything_reversed(my_list : list[str]) -> list[str]:
    this_list = []

    for name in my_list:
        this_list.append(name[::-1])


    return this_list[::-1]
