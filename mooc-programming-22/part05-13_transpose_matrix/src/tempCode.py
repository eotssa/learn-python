def transpose(matrix: list):
    temp_list = matrix[:]            # copies row references
    for i, row in enumerate(matrix): # copies information from each row 
        temp_list[i] = row[:]

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            matrix[y][x] = temp_list[x][y] 
