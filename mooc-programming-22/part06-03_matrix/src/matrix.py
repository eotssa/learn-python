# write your solution here

def row_sums(): 
    with open("matrix.txt") as new_file:
        sum_each_row = []
        for line in new_file: 
            line = line.replace("\n", "")
            line_lst = line.split(",")

            sum = 0
            for num in line_lst:
                sum += int(num) 

            sum_each_row.append(sum)
        
        return sum_each_row

def matrix_sum():
    this_lst = row_sums()

    return sum(this_lst)

def matrix_max():
    with open("matrix.txt") as new_file:

        biggest_num = 0
        for line in new_file: 
            line = line.replace("\n", "")
            line_lst = line.split(",")

            for num in line_lst: 
                if biggest_num < int(num):
                    biggest_num = int(num)
        
        return biggest_num



"""a more modular solution

def read_matrix():
    with open("matrix.txt") as file:
        m = []
        for row in file:
            mrow = []
            items = row.split(",")
            for item in items:
                mrow.append(int(item))
            m.append(mrow)
 
    return m
 
def combine(matrix: list):
    mlist = []
    for row in matrix:
        mlist += row
    
    return mlist
 
def matrix_sum():
    mlist = combine(read_matrix())
    return sum(mlist)
 
def matrix_max():
    mlist = combine(read_matrix())
    return max(mlist)
 
def row_sums():
    matrix = read_matrix()
    sums = []
    for row in matrix:
        sums.append(sum(row))
    return sums
        

"""