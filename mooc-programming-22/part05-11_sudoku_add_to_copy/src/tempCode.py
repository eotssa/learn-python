def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    this_sudoku = sudoku[:]      # shallow copy of the rows, but the inner row lists remain referenced 
    for i, row in enumerate(sudoku):
        for j, num in enumerate(row): 
            this_sudoku[i][j] = num

    add_number(this_sudoku, row_no, column_no, number)

    return this_sudoku
