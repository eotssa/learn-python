## Writing Data to Files

We can create a new file every time we want to write data to a file, but we can also append new data to the end of an existing file. In both cases, we use the `open` function from the previous section. For writing files, the function requires a second argument.

### Creating a New File

If you want to create a new file, you would call the `open` function with the additional argument `"w"` to signify that the file should be opened in write mode. So, the function call could look like this:

```python
with open("new_file.txt", "w") as my_file:
    # code to write something to the file
```

**NB:** If the file already exists, all the contents will be overwritten. It's important to be very careful when creating new files.

With the file open, you can write data to it. You can use the `write` method, which takes the string that is to be written as its argument.

```python
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
```

When you execute the program, a new file named `new_file.txt` will appear in the directory. The contents would look like this:

**Sample data:**
```
Hello there!
```

If you want line breaks in the file, you will have to add them manually. The `write` function doesn't work exactly like the more familiar `print` function, although they are similar. So, the following program:

```python
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!")
    my_file.write("This is the second line")
    my_file.write("This is the last line")
```

Would result in a file with these contents:

**Sample data:**
```
Hello there!This is the second lineThis is the last line
```

Line breaks are achieved by adding new line characters (`\n`) to the argument strings:

```python
with open("new_file.txt", "w") as my_file:
    my_file.write("Hello there!\n")
    my_file.write("This is the second line\n")
    my_file.write("This is the last line\n")
```

Now the contents of `new_file.txt` would look like this:

**Sample data:**
```
Hello there!
This is the second line
This is the last line
```


## Appending Data to an Existing File

To append data to the end of an existing file, you can open the file in append mode by passing `"a"` as the second argument to the `open()` function.

```python
with open("new_file.txt", "a") as my_file:
    my_file.write("This is the 4th line\n")
    my_file.write("And yet another line.\n")
```

Appending data to a file allows you to add new content without overwriting the existing contents. If the file doesn't exist, it will be created. However, it's important to note that appending data to files is not a common practice in programming. In most cases, files are read, processed, and overwritten entirely when needed.

Remember to include the appropriate newline characters (`\n`) if you want to separate the appended content into separate lines within the file.


# Writing CSV Files

## Writing CSV files line by line

CSV files can be written line by line using the `write` method, similar to writing any other file. Each line in the CSV file represents a record, with fields separated by a specific delimiter, such as a semicolon or a comma.

Here's an example that creates a file called `coders.csv` and writes programmer data to it:

```python
with open("coders.csv", "w") as my_file:
    my_file.write("Eric;Windows;Pascal;10\n")
    my_file.write("Matt;Linux;PHP;2\n")
    my_file.write("Alan;Linux;Java;17\n")
    my_file.write("Emily;Mac;Cobol;9\n")
```

Executing this program would result in a CSV file with the following contents:

```
Eric;Windows;Pascal;10
Matt;Linux;PHP;2
Alan;Linux;Java;17
Emily;Mac;Cobol;9
```

## Writing CSV files from a list

If the data to be written is stored in a list in computer memory, you can iterate over the list and construct the lines using an f-string:

```python
coders = [
    ["Eric", "Windows", "Pascal", 10],
    ["Matt", "Linux", "PHP", 2],
    ["Alan", "Linux", "Java", 17],
    ["Emily", "Mac", "Cobol", 9]
]

with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = f"{coder[0]};{coder[1]};{coder[2]};{coder[3]}"
        my_file.write(line + "\n")
```

If the list contains a large number of items, building the string manually may become cumbersome. In such cases, you can use nested loops to construct the line:

```python
with open("coders.csv", "w") as my_file:
    for coder in coders:
        line = ""
        for value in coder:
            line += f"{value};"
        line = line[:-1]
        my_file.write(line + "\n")
```

## Clearing file contents and deleting files

To clear the contents of an existing file, you can open it in write mode and close it immediately. This can be achieved using a `pass` statement within a `with` block:

```python
with open("file_to_be_cleared.txt", "w") as my_file:
    pass
```

Alternatively, you can use a one-liner to bypass the `with` block:

```python
open("file_to_be_cleared.txt", "w").close()
```

To delete a file entirely, you can use the `os` module:

```python
import os

os.remove("unnecessary_file.csv")
```

This will delete the file called "unnecessary_file.csv" from the filesystem.