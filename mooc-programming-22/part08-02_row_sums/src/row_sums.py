# Write your solution here
def row_sums(my_matrix: list):
    for row in my_matrix:
        total = 0
        for num in row:
            total += num
        
        row.append(total)
            

"""
def row_sums(matrix: list):
    for row in my_matrix:
        row.append(sum(row))
"""