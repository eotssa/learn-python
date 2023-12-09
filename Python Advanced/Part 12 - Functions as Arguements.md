# Functions as arguments within your own functions

We established above that it is possible to pass a reference to a function as an argument to another function. To wrap this section up, let's write our very own function which takes a function as its argument.

```python
# the type hint "callable" refers to a function
def perform_operation(operation: callable):
    # Call the function which was passed as an argument
    return operation(10, 5)

def my_sum(a: int, b: int):
    return a + b

def my_product(a: int, b: int):
    return a * b

if __name__ == "__main__":
    print(perform_operation(my_sum))
    print(perform_operation(my_product))
    print(perform_operation(lambda x,y: x - y))
```

**Sample output**
```
15
50
5
```

The value returned by the function `perform_operation` depends on which function was passed as an argument. Any function which accepts two arguments would do, no matter whether it is anonymous or named.

Passing references to functions as arguments to other functions might not be something you will end up doing on a daily basis in your programming career, but it can be a useful technique. This following program selects some lines from one file and writes them to another file. The way the lines are selected is determined by a function which returns `True` only if the lines should be copied:

```python
def copy_lines(source_file: str, target_file: str, criterion= lambda x: True):
    with open(source_file) as source, open(target_file, "w") as target:
        for line in source:
            # Remove any whitespace from beginning and end of line
            line = line.strip()

            if criterion(line):
                target.write(line + "\n")

# Some examples
if __name__ == "__main__":
    # If the third parameter is not given, copy all lines
    copy_lines("first.txt", "second.txt")

    # Copy all non-empty lines
    copy_lines("first.txt", "second.txt", lambda line: len(line) > 0)

    # Copy all lines which contain the word "Python"
    copy_lines("first.txt", "second.txt", lambda line: "Python" in line)

    # Copy all lines which do not end in a full stop
    copy_lines("first.txt", "second.txt", lambda line: line[-1] != ".")
```

The function definition contains a default value for the keyword parameter `criterion`: `lambda x: True`. This anonymous function always returns `True` regardless of the input. So, the default behaviour is to copy all lines. As usual, if a value is given for a parameter with a default value, the new value replaces the default value.

---

### **Programming Exercise: Product Search**

**Task**:
The exercise involves working with products which are stored in tuples. Each tuple contains three items: name, price, and amount.

You are required to write a function named `search(products: list, criterion: callable)`.

**Input**:
- A list `products` of tuples. Each tuple contains the name of the product, its price, and its amount.
- A callable `criterion` which is a function that processes a tuple and returns a Boolean value.

**Output**: 
The `search` function should return a new list containing those tuples from the original which fulfill the criterion.

---

**Example**:

```python
products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]

def price_under_4_euros(product):
    return product[1] < 4

for product in search(products, price_under_4_euros):
    print(product)
```

**Expected Output**:
```
('apple', 3.95, 3)
('kale', 0.99, 1)
```

Another example using lambda:

```python
for product in search(products, lambda t: t[2]>10):
    print(product)
```

**Expected Output**:
```
('banana', 5.95, 12)
('watermelon', 4.95, 22)
```

---

**Your Solution**:

```python
# Place your solution here

# products = (name, price, amount) -> list containing tupules from the original that meet criterion 
def search(products: list, criterion: callable) -> list:
    return [product for product in products if criterion(product)]

def price_under_4_euros(product):
    return product[1] < 4


if __name__ == "__main__":
    products = [("banana", 5.95, 12), 
                ("apple", 3.95, 3), 
                ("orange", 4.50, 2), 
                ("watermelon", 4.95, 22), 
                ("kale", 0.99, 1)]


    for product in search(products, price_under_4_euros):
        print(product)
```