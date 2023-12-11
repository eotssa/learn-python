# Write your solution here
def block_correct(sudoku: list, row_no: int, column_no: int):

    list_A = []

    for row in sudoku[row_no: row_no + 3]:
        for cell in row[column_no: column_no + 3]: 
            if cell > 0 and cell in list_A:
                return False
            list_A.append(cell)
    
    return True


"""Model Code vs Mine 
I will say, I'm not that comfortable using "in range" yet, but the idea here makes sense, it achieves the same thing I do, but with more steps. 
When I mean the same, I mean the method is the same. 
I think I get caught up in trying to be "fancy" or use "fancy new" methods I learned instead of keeping it simple. 
Also, take the time to understand the problem instead of diving head first by skimming. 

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
 
    return True
"""