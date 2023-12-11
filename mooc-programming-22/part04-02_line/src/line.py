# Write your solution here
def line(num, str_A):
    if len(str_A) != 0:
        print(str_A[0] * num) 
    else:
        print("*" * num) 


# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(10, "LOL")
