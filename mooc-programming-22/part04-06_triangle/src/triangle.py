# Copy here code of line function from previous exercise
def line(num, str_A):
    if len(str_A) != 0:
        print(str_A[0] * num) 
    else:
        print("*" * num) 

def triangle(size):
    # You should call function line here with proper parameters
    i = 1
    while i <= size:
        line(i, "#")
        i += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
