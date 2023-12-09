```python
# Write your solution here

def row_correct(sudoku : list, row_no: int) -> bool: 
    for cell in sudoku[row_no]:
        if (sudoku[row_no].count(cell) != 1) and cell > 0: 
            return False
        
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
    
    return True


def block_correct(sudoku: list, row_no: int, column_no: int):

    list_A = []

    for row in sudoku[row_no: row_no + 3]:
        for cell in row[column_no: column_no + 3]: 
            if cell > 0 and cell in list_A:
                return False
            list_A.append(cell)
    
    return True

def sudoku_grid_correct(sudoku: list):
    for i in range(0, 8):
        if column_correct(sudoku, i)  == False:
            return False
        
        if row_correct(sudoku, i) == False:
            return False
    
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            if block_correct(sudoku, i, j) == False:
                return False
            
    return True
```