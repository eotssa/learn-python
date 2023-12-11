# WRITE YOUR SOLUTION HERE:
def lengths(lists: list):
    return [len(inner_list) for inner_list in lists]


if __name__ == "__main__":
    lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(lengths(lists))