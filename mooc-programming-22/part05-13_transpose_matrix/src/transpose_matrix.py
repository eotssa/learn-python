# Write your solution here
# The function should not have a return value. The matrix should be modified directly through the reference.

def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]