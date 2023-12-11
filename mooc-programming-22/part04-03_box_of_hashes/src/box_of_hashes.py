# Copy here code of line function from previous exercise
def line(num, str_A):
    if len(str_A) != 0:
        print(str_A[0] * num) 
    else:
        print("*" * num) 

def box_of_hashes(height):
    # You should call function line here with proper parameters
    i = 1
    while i <= height:
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
