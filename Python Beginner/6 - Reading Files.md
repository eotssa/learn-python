# Working with Text Files in Python

## Overview
- Python programming often involves reading and writing data to files.
- This provides a simple and effective way to handle large datasets.
- In this guide, we focus only on text files, which contain lines of text. 

## Text Files vs Word Processor Documents
- **Text Files**: Simple to handle; used with programs like Visual Studio Code.
- **Word Documents**: Contain text but aren't text files. Includes formatting info; complex to handle programmatically.

## Reading from Text Files
- Example file used: `example.txt`, with content:
    ```
    Hello there!
    This example file contains three lines of text.
    This is the last line.
    ```

## Including Files in Python 
- Python's `with` statement is used to include and handle files.
- It opens the file, allows operations within its block, then automatically closes it.

## Example Code
```python
with open("example.txt") as new_file:
    contents = new_file.read()
    print(contents)
```
- **Output**: 
    ```
    Hello there!
    This example file contains three lines of text.
    This is the last line.
    ```

## File Handle and `read` Method
- `new_file` is a file handle that allows access to the file.
- `read` method returns file contents as a single string.
- String returned by `read`: `"Hello there!\nThis example file contains three lines of text.\nThis is the last line."`

# Processing Text Files Line-by-Line in Python

## `read` Method vs Line-by-Line Iteration
- `read` method: prints entire file content.
- Line-by-line iteration: more common and flexible, treats file as list of strings (lines).

## Iterating Through Lines with a `for` Loop
- Each string represents a single line in the file.
- Use a `for` loop to traverse the file.

## Code Example: Counting and Printing Lines
```python
with open("example.txt") as new_file:
    count = 0
    total_length = 0

    for line in new_file:
        line = line.replace("\n", "")
        count += 1
        print("Line", count, line)
        length = len(line)
        total_length += length

print("Total length of lines:", total_length)
```
- **Output**:
    ```
    Line 1 Hello there!
    Line 2 This example file contains three lines of text.
    Line 3 This is the last line.
    Total length of lines: 81
    ```

## Understanding the Code
- Line breaks (`\n`) are removed from each line with the `replace` method.
- `replace` method: Replaces line break characters with an empty string, thereby allowing accurate calculation of line lengths.
- The `for` loop counts the lines, prints each line with its line number, and sums the lengths of all lines.

## Key Takeaway
- **`replace` Method**: Used for manipulating strings; very useful for cleaning data in files.


# Working with CSV Files in Python

## CSV File Basics
- CSV: Comma-separated values.
	- A type of text file with data separated by a predetermined character, usually a comma (,) or semicolon (;).
- Used for storing different kinds of records; easy data exchange between systems.

## Python `split` Method
- Splits a string into a list of substrings based on a separator character.
- Used to separate different fields on a line.

## Code Example: Processing CSV Data
- Assume `grades.csv` file contains student names and their grades, separated by semicolons.

```python
with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades = parts[1:]
        print("Name:", name)
        print("Grades:", grades)
```
- **Output**:
    ```
    Name: Paul
    Grades: ['5', '4', '5', '3', '4', '5', '5', '4', '2', '4']
    Name: Beth
    Grades: ['3', '4', '2', '4', '4', '2', '3', '1', '3', '3']
    Name: Ruth
    Grades: ['4', '5', '5', '4', '5', '5', '4', '5', '4', '4']
    ```

## Understanding the Code
- For each line, remove the line break (`\n`) and split the line into parts at each semicolon using `split`.
- The first part is the student's name, the rest are the grades.

## Key Takeaway
- **`split` Method**: Powerful tool for parsing and processing structured data in files, such as CSVs.

# Reading a File Multiple Times in Python

## Problem Statement
- Need to process contents of a file more than once in a single program.
- Attempting to read a file twice leads to an error because after the first read, the file handle rests at the end of the file and data in the file can't be accessed again.

## Incorrect Code
- Tries to read the file twice, leading to an error.
```python
with open("people.csv") as new_file:
    # Print out the names
    for line in new_file:
        parts = line.split(";")
        print("Name:", parts[0])

    # Find the oldest
    age_of_oldest = -1
    for line in new_file:
        parts = line.split(";")
        name = parts[0]
        age = int(parts[1])
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("The oldest is", oldest)
```
- Error encountered: `UnboundLocalError: local variable 'oldest' referenced before assignment`

## Inefficient Solution
- Open and read the file twice.
```python
with open("people.csv") as new_file:
    # Print out the names
    for line in new_file:
        parts = line.split(";")
        print("Name:", parts[0])

with open("people.csv") as new_file:
    # Find the oldest
    age_of_oldest = -1
    for line in new_file:
        parts = line.split(";")
        name = parts[0]
        age = int(parts[1])
        if age > age_of_oldest:
            age_of_oldest = age
            oldest = name
    print("The oldest is", oldest)
```
- Cons: Unnecessary repetition, inefficiency as the file is read twice.

## Efficient Solution
- Read the file once, store its contents in a suitable data structure for future use.
```python
people = []
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(";")
        people.append((parts[0], int(parts[1]), parts[2]))

# Print out the names
for person in people:
    print("Name:", person[0])

# Find the oldest
age_of_oldest = -1
for person in people:
    name = person[0]
    age = person[1]
    if age > age_of_oldest:
        age_of_oldest = age
        oldest = name
print("The oldest is", oldest)
```
- Pros: More efficient, as the file is only read once. Contents are stored in a list for further processing.

## Key Takeaway
- **File Reading Strategy**: Avoid reading the same file multiple times, instead store contents in memory for efficient processing.


# Processing CSV Files in Python

## Context
- Working with file `grades.csv`, which contains student names and their grades.
- Aim: Create a dictionary `grades` where keys are student names and values are lists of grades.

## Reading and Storing Data
```python
grades = {}
with open("grades.csv") as new_file:
    for line in new_file:
        line = line.replace("\n", "")
        parts = line.split(";")
        name = parts[0]
        grades[name] = []
        for grade in parts[1:]:
            grades[name].append(int(grade))
```
- **Output**: `{'Paul': [5, 4, 5, 3, 4, 5, 5, 4, 2, 4], 'Beth': [3, 4, 2, 4, 4, 2, 3, 1, 3, 3], 'Ruth': [4, 5, 5, 4, 5, 5, 4, 5, 4, 4]}`

## Compute and Display Statistics
- Compute best grade and average grade for each student.
```python
for name, grade_list in grades.items():
    best = max(grade_list)
    average = sum(grade_list) / len(grade_list)
    print(f"{name}: best grade {best}, average {average:.2f}")
```
- **Output**:
    - `Paul: best grade 5, average 4.10`
    - `Beth: best grade 4, average 2.90`
    - `Ruth: best grade 5, average 4.50`

## Key Concepts
- **Dictionary in Python**: Powerful data structure for storing key-value pairs. In this case, used for mapping student names to their grades.
- **File Processing**: Used the `with open` statement to read the CSV file line by line, then split each line into parts and stored them in the dictionary.
- **Statistics Calculation**: Computed the maximum (best grade) and average grade for each student using built-in Python functions `max()` and `sum()`.

## Note
This technique is applicable for processing many different types of data contained in files, not just for grade lists.


# CSV File Processing in Python with Whitespace Handling

## Context
- A CSV file `people.csv` with unnecessary white spaces and line breaks exported from Excel.
- Each line contains a first and last name separated by a semicolon, and extra spaces.

### Before Cleanup
When we read from the CSV file and print the names without using any strip functions, we see extra spaces and line breaks in the output.

```python
last_names = []
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "first":
            continue # this was the header line, so it is ignored
        last_names.append(parts[1])
print(last_names)
```

Sample output:
```python
[' Python\n', ' Java\n', ' Haskell']
```

## Reading and Storing Data (After Cleanup) 
```python
last_names = []
with open("people.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "first":
            continue # this was the header line, so it is ignored
        last_names.append(parts[1].strip())
```
- **Output**: `['Python', 'Java', 'Haskell']`

## Key Concepts
- **Whitespace Removal**: Utilizing the `strip()` method to remove unnecessary white spaces from beginning and end of a string. In the example above, the strip method is used to remove the leading and trailing white spaces from the last names.

## Other Whitespace Handling Techniques
- `lstrip()`: Removes leading white spaces (from the left).
- `rstrip()`: Removes trailing white spaces (from the right).

## Demonstration:
```python
>>> " teststring  ".rstrip()
' teststring'
>>> " teststring  ".lstrip()
'teststring  '
```
## Note
`strip()`, `lstrip()`, and `rstrip()` are powerful string methods that can be particularly useful when cleaning up data in Python. Their usage can be extended beyond the given example to handle data from various sources which might not always be cleanly formatted.


# Combining Data from Different Files in Python

In many scenarios, the data required for processing by a program could be scattered across multiple files. Here's an example that illustrates how you can connect data from multiple CSV files using a common identifier.

## Context
- A company's personal details of employees are stored in a file `employees.csv`.
- The employee's salaries are stored in another file `salaries.csv`.
- Each data line in both files contains a Personal Identity Code (PIC) that can be used as a common identifier.

## Sample Data
**employees.csv**
```
pic;name;address;city
080488-123X;Pekka Mikkola;Vilppulantie 7;00700 Helsinki
290274-044S;Liisa Marttinen;Mannerheimintie 100 A 10;00100 Helsinki
010479-007Z;Arto Vihavainen;Pihapolku 4;01010 Kerava
010499-345K;Leevi Hellas;Tapiolantie 11 B;02000 Espoo
```
**salaries.csv**
```
pic;salary;bonus
080488-123X;3300;0
290274-044S;4150;200
010479-007Z;1300;1200
```
## Code
```python
names = {}
with open("employees.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        names[parts[0]] = parts[1]

salaries = {}
with open("salaries.csv") as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == "pic":
            continue
        salaries[parts[0]] = int(parts[1]) +int(parts[2])

print("incomes:")
for pic, name in names.items():
    if pic in salaries:
        salary = salaries[pic]
        print(f"{name:16} {salary} euros")
    else:
        print(f"{name:16} 0 euros")
```
```
"""First the program produces the dictionaries **names** and salaries. They have the following contents:

{ # names
    '080488-123X': 'Pekka Mikkola',
    '290274-044S': 'Liisa Marttinen',
    '010479-007Z': 'Arto Vihavainen',
    '010499-345K': 'Leevi Hellas'
}

{ # salaries
    '080488-123X': 3300,
    '290274-044S': 4350,
    '010479-007Z': 2500
}
```
### Output
```
incomes:
Pekka Mikkola    3300 euros
Liisa Marttinen  4350 euros
Arto Vihavainen  2500 euros
Leevi Hellas     0 euros
```
## Key Concepts
- **Dictionaries**: The program uses two dictionaries `names` and `salaries` which use the Personal Identity Code (PIC) as the key. 
- **Data Linking**: The PIC is used as a common identifier to link the employee's name from `employees.csv` to their corresponding salary in `salaries.csv`.

## Note
- The program also handles cases where an employee's PIC is not present in the salary file, it prints 0 euros as the salary for those employees.
- The order of storing items in a dictionary doesn't matter as keys are processed based on hash values.