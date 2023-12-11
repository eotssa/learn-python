# Write your solution here
def row_correct(sudoku : list, row_no: int) -> bool: 
    for cell in sudoku[row_no]:
        if (sudoku[row_no].count(cell) != 1) and cell > 0: 
            return False
        
    return True

""" I keep seeing this reoccuring pattern to use a list, and 
place values into the empty list to check for reptition 
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
 
    return True
"""


