# Transposing Elements

```
The following matrix

1 2 3
4 5 6
7 8 9

transposed looks like this:

1 4 7
2 5 8
3 6 9

```

- #### Solution 1 (creating a temp matrix) -- inefficient 
	The initial code is my take on creating a deep copy of a matrix, or in this case a `list[list[int]]`. A temporary matrix is created and used as a temp variable. However, the problem specifies that the original list is modified. (So yes, while this solution works, it somewhat defeats the original goal." 
	
```python
def transpose(matrix: list):
    temp_list = matrix[:]            # copies row references
    for i, row in enumerate(matrix): # copies information from each row 
        temp_list[i] = row[:]

    for x in range(len(matrix)):
        for y in range(len(matrix)):
            matrix[y][x] = temp_list[x][y] 
```

#### Copying a matrix: `deepcopy()` vs. `list comphrension vs. manually

- **deepcopy** 
```Python
#import copy
def transpose(matrix: list):
	temp_list = copy.deepcopy(matrix) 
```

- list comphrension
```python
def transpose(matrix: list): 
	temp_list = [row[:] for row in matrix] 

""" manually, but too many lines 
def transpose(matrix: list):
    temp_list = matrix[:]            # copies row references
    for i, row in enumerate(matrix): # copies information from each row 
        temp_list[i] = row[:]
"""
```

#### Solution 2: Model Solution
```python
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
```

#### Solution 3: Pythonic 
- Variables are assigned in order, and left hand side is evaluted first, creating a tuple, and then assignment is done in a single, atomic, operation. 
```python: 
def transpose(matrix: list):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

```

---

# Side Effects

The following program has an unintended side effect:

```python
def second_smallest(my_list: list) -> int:
    # in an ordered list, the second smallest item is at index 1
    my_list.sort()
    return my_list[1]

numbers = [1, 4, 2, 5, 3, 6, 4, 7]
print(second_smallest(numbers))
print(numbers)
```

The since `my_list` is passed as a reference, calling `my_list.sort()` affects the original list. 

We can avoid the side effect by making a small change to the function:

```python
def second_smallest(my_list: list) -> int:
    list_copy = sorted(my_list)
    return list_copy[1]

numbers = [1, 4, 2, 5, 3, 6, 4, 7]
print(second_smallest(numbers))
print(numbers)
```

`sorted()` returns a list, whereas `sort()` alters the original list. 

Functions free of side effects are also called **pure functions**. Especially when adhering to a **functional programming style**, this is a common ideal to follow.

---
