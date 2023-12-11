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


if __name__ == "__main__":

    s = [
    [ 9, 0, 0, 0, 8, 0, 3, 0, 0 ],
    [ 2, 0, 0, 2, 5, 0, 7, 0, 0 ],
    [ 0, 2, 0, 3, 0, 0, 0, 0, 4 ],
    [ 2, 9, 4, 0, 0, 0, 0, 0, 0 ],
    [ 0, 0, 0, 7, 3, 0, 5, 6, 0 ],
    [ 7, 0, 5, 0, 6, 0, 4, 0, 0 ],
    [ 0, 0, 7, 8, 0, 3, 9, 0, 0 ],
    [ 0, 0, 1, 0, 0, 0, 0, 0, 3 ],
    [ 3, 0, 0, 0, 0, 0, 0, 0, 2 ],
    ]
    print_sudoku(s)