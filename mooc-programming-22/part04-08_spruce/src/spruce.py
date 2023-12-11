# Write your solution here


def spruce(size): 
    #print(" " * (size - 1) + "*")
    print("a spruce!")

    i = 1
    j = 1
    while i <= (size): 
        print(" " * (size - i) + "*" * j)
        i += 1
        j += 2

    print(" " * (size - 1) + "*")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(3)