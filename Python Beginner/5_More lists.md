
## Lists within Lists

The items in a list can be lists themselves:

```python
my_list = [[5, 2, 3], [4, 1], [2, 2, 5, 1]]
print(my_list)
print(my_list[1])
print(my_list[1][0])
```

The output is:

```
[[5, 2, 3], [4, 1], [2, 2, 5, 1]]
[4, 1]
4
```

Lists within lists can be useful for storing structured data. For example, you could store information about a person in a list. Each person's information can be represented as a sublist within the main list:

```python
persons = [["Betty", 10, 1.37], ["Peter", 7, 1.25], ["Emily", 32, 1.64], ["Alan", 39, 1.78]]

for person in persons:
    name = person[0]
    age = person[1]
    height = person[2]
    print(f"{name}: age {age} years, height {height} meters")
```

The output is:

```
Betty: age 10 years, height 1.37 meters
Peter: age 7 years, height 1.25 meters
Emily: age 32 years, height 1.64 meters
Alan: age 39 years, height 1.78 meters
```

In this example, each sublist represents a person, with the first item being the name, the second item being the age, and the third item being the height.

## Matrices

A two-dimensional array, or a matrix, can be represented using a list within a list. Each sublist corresponds to a row in the matrix.

For example, consider the following matrix:

```
5 1 1
```

It can be represented as a two-dimensional list in Python:

```python
my_matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
```

To access individual elements within the matrix, use consecutive square brackets. The first index refers to the row, and the second index refers to the column. Indexing starts from zero. For example, `my_matrix[0][1]` refers to the second item on the first row.

```python
my_matrix = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]

print(my_matrix[0][1])
my_matrix[1][0] = 10
print(my_matrix)
```

The output is:

```
2
[[1, 2, 3], [10, 2, 1], [4, 5, 6]]
```

Traversing rows and elements within the matrix can be done using nested loops:

```python
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print(row)
```

The output is:

```
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
```

To access individual elements, use nested loops:

```python
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for row in my_matrix:
    print("A new row")
    for element in row:
        print

(element)
```

The output is:

```
A new row
1
2
3
A new row
4
5
6
A new row
7
8
9
```

## Visualizing Code with Lists within Lists

Understanding programs that involve lists within lists can be challenging. The Python Tutor visualisation tool can help in visualizing how they work.

Working with matrices and nested lists can be easier to grasp using visualizations. For example, a 3x3 matrix technically consists of four lists. The first list represents the entire matrix, while the remaining lists represent the rows.

The visualisation tool helps in understanding the reference relationships between the main list and the nested lists representing the rows.

## Accessing Items in a Matrix

Accessing a single row within a matrix is straightforward by selecting the desired row. The following function calculates the sum of the elements in a chosen row:

```python
def sum_of_row(my_matrix, row_no: int):
    row = my_matrix[row_no]
    row_sum = 0
    for item in row:
        row_sum += item
    return row_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_row(m, 1)
print(my_sum)  # prints out 33 (which equals 9 + 1 + 12 + 11)
```

Working with columns within a matrix requires iterating through each row and selecting the item at the chosen position:

```python
def sum_of_column(my_matrix, column_no: int):
    column_sum = 0
    for row in my_matrix:
        column_sum += row[column_no]
    return column_sum

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

my_sum = sum_of_column(m, 2)
print(my_sum)  # prints out 39 (which equals 3 + 12 + 9 + 15)
```

Changing the value of a single element within the matrix can be done by selecting the desired row and column:

```python
def change_value(my_matrix, row_no: int, column_no: int, new_value: int):
    row = my_matrix[row_no]
    row[column_no] = new_value

m = [[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]

print(m)
change_value(m, 2, 3, 1000)
print(m)
```

The output is:

```
[[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]
[[4, 2, 3, 2], [9, 1, 12, 11], [7, 8, 9, 1000], [2, 9, 15, 1]]
```

To modify the contents of a matrix, it is necessary to access elements by their indexes rather than using a simple loop. A loop using the `range` function can be used to iterate over the indexes.


# Understanding Python Variables and References

## Variables as References in Python

Instead of considering a variable as a "box" containing its value, it is more accurate to think of a Python variable as a reference to the actual object, which can be a number, a string, or a list, among others. This reference information points to the location in computer memory where the value can be found, but it is not the value itself.

```python
a = [1, 2, 3]
print(id(a))
b = "This is a reference, too"
print(id(b))
```

### Using References to Identify Variables

The function `id` can be used to find out the exact location the variable points to, returning an integer that can be thought of as the memory address. For instance, if you execute the code above on your own computer, the result will likely differ as your variables will point to different locations - the references will be different.

The Python Tutor visualization tool also presents references as arrows from the variable to the actual value. However, it simplifies how strings are represented by displaying them as if they are stored in the variables themselves, even though Python handles strings much like lists with references to locations in memory.

## Understanding Immutable and Mutable Types in Python

Many of Python's built-in types like `str` are immutable, meaning their value or any part of it cannot change. Conversely, some types like `list` are mutable, meaning their content can change without needing to create an entirely new object. 

Surprisingly, the basic data types `int`, `float`, and `bool` are also immutable in Python. Although it may seem like you're changing the value stored in the variable, each operation creates a new object in memory.

```python
number = 1
print(id(number))
number += 10
print(id(number))
a = 1
print(id(a))
```

## Multiple References and List Assignment

When you assign a list variable to a new variable, what gets copied is the reference, not the list itself. This means there are now two references to the same memory location containing the list, and changes made to the list through one reference affect the other reference too, as they both point to the same location.

```python
list1 = [1, 2, 3, 4]
list2 = list1
list1[0] = 10
list2[1] = 20
print(list1)
print(list2)
```

## Copying a List

To create an actual separate copy of a list, you can either create a new list and add each item from the original list, or use the bracket operator `[:]` to select all items in the original list, which creates a copy.

```python
my_list = [1,2,3,4]
new_list = my_list[:]
my_list[0] = 10
new_list[1] = 20
print(my_list)
print(new_list)
```

## Lists as Parameters in Functions

When passing a list as an argument to a function, you're passing a reference to that list, meaning the function can modify the list directly. Note that changes made to the list inside the function persist outside the function because they're modifying the same list referenced in the calling scope.

```python
def add_item(my_list: list):
    new_item = 10
    my_list.append(new_item)
a_list = [1,2,3]
print(a_list)
add_item(a_list)
print(a_list)
```

## Editing Lists Given as Arguments

When you try to modify a list argument within a function by assigning a new list to the argument variable, the original list is not affected because the argument variable now points to a new memory location. A better approach is to directly modify the original list or copy items from the new list into the original one.

```python
def augment_all(my_list: list):
    for i in range(len(my_list)):
        my_list[i] += 10
```