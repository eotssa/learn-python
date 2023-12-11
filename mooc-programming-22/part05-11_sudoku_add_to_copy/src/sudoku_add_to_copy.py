# Write your solution here
def print_sudoku(sudoku: list):
    for i, row in enumerate(sudoku):
        if i % 3 == 0 and i > 0:
            print()
        for j, cell in enumerate(row):
            if j % 3 == 0 and j > 0:
                print(" ", end="")
            if cell == 0: 
                print("_ ", end="")
            else: 
                print(f"{cell} ", end="")
        print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    this_sudoku = sudoku[:]      # shallow copy of the rows, but the inner row lists remain referenced 
    for i, row in enumerate(sudoku): # shallow copy of the inner row lists, but this double shallow copy effective creates the entire copy of the list of list
            this_sudoku[i] = row[:]

    add_number(this_sudoku, row_no, column_no, number)

    return this_sudoku

# The model solution of copy and add sidelines this issue by initializing a new list to begin with. 
# Then it adds the rows after. It's the same as what I did, but with more steps. 
"""
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
 
    new_list[row_no][column_no] = number
    return new_list
"""

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)