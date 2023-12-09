# Shallow Copy Problem
```python
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
    this_sudoku = sudoku[:]
    #add_number(this_sudoku, row_no, column_no, number)

    return this_sudoku



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
```

**The line `this_sudoku = sudoku[:]` is creating a shallow copy of the list `sudoku`, which means it creates a new list containing all of the elements in the old list. However, it's important to note that it's a "shallow" copy. This means that while the top-level list is duplicated, the inner lists (the rows in your Sudoku grid) are still the same lists. If you modify one of these inner lists, the change will be reflected in both `this_sudoku` and `sudoku`.**

Here is a small example that demonstrates this behavior:

```python
sudoku = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
this_sudoku = sudoku[:]

sudoku[0][0] = 10
print(this_sudoku)  # [[10, 2, 3], [4, 5, 6], [7, 8, 9]]
```

If you need a deep copy of the list, where changes to one list do not affect the other, you should use the `copy` module's `deepcopy` function:

```python
import copy

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    this_sudoku = copy.deepcopy(sudoku)
    #add_number(this_sudoku, row_no, column_no, number)

    return this_sudoku
```

With `deepcopy`, changes to the inner lists in `sudoku` will not affect `this_sudoku`, and vice versa.

------------

## My Solution vs. Model Solution vs. deepcopy Solution
    # shallow copy of the rows, but the inner row lists remain referenced  
    # shallow copy of the inner row lists, but this double shallow copy effective creates the entire copy of the list of list
```python
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number


def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    this_sudoku = sudoku[:]      
    for i, row in enumerate(sudoku):
            this_sudoku[i] = row[:]
    add_number(this_sudoku, row_no, column_no, number)
  
return this_sudoku
```


**The model solution of copy and add sidelines this issue by initializing a new list to begin with.  Then it adds the rows after. It's the same as what I did, but with more steps.** 
```python
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
 
    new_list[row_no][column_no] = number
    return new_list
```

## List Comphrension Solution (Limits is only List of List)
```python
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    this_sudoku = [list(row) for row in sudoku]  # Create a new list for each row
    add_number(this_sudoku, row_no, column_no, number)

    return this_sudoku
```

## More "Sophisticated" Solution
```python
import copy

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    this_sudoku = copy.deepcopy(sudoku)
    #add_number(this_sudoku, row_no, column_no, number)

    return this_sudoku

```

```
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
```

---
