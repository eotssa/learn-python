**Generators**

*Learning Objectives*:
- Understand what a Python generator is.
- Recognize the significance of the `yield` keyword.
- Ability to write custom generator functions.

Python generators offer an efficient way to produce items from a series one-by-one without generating the entire series every time. This is particularly useful in cases like generating the Fibonacci series where generating the whole series every time could be redundant.

**Differences between Generators and Normal Functions**:
- Generators produce items from a series on-demand.
- Normal functions return the same output for the same input. Generators remember their state and produce the next item in the series.
- Generators can simplify code and save memory/computational resources in certain scenarios.

**Using `yield` in Generators**:
- A generator function contains the `yield` keyword to denote its return value.
- Unlike the `return` keyword which terminates a function, `yield` keeps track of the function's state, so the function can continue from where it left off the next time it's called.

Here's a basic generator function example:
```python
def counter(max_value: int):
    number = 0
    while number <= max_value:
        yield number
        number += 1

# Using the generator:
numbers = counter(10)
print(next(numbers))  # Outputs: 0
print(next(numbers))  # Outputs: 1
```

**Handling the End of a Generator**:
When a generator runs out of items, it raises a `StopIteration` exception. This can be caught using a `try-except` block:
```python
numbers = counter(1)
try:
    print(next(numbers))
    print(next(numbers))
    print(next(numbers))
except StopIteration:
    print("ran out of numbers")
```

**Traversing Generators**:
A `for` loop can be used to iterate through a generator:
```python
numbers = counter(5)
for number in numbers:
    print(number)
```

However, ensure the generator terminates. Using a `for` loop with an infinite generator can cause endless execution.

**Conclusion**:
Generators provide a way to produce values from a series without the overhead of generating the entire series every time. They can be more efficient, especially when dealing with large or infinite data sets.


### **Programming Exercise: Even Numbers**

**Task**:
Write a generator function named `even_numbers(beginning: int, maximum: int)`.

**Input**:
- Two integers: `beginning` and `maximum`.

**Output**: 
The function should produce even numbers starting from `beginning` and ending with, at most, `maximum`.

---

**Example**:

```python
numbers = even_numbers(2, 10)
for number in numbers:
    print(number)
```

**Expected Output**:
```
2
4
6
8
10
```

---

**Your Solution**:

```python
# Place your solution here

# Write your solution here
def even_numbers(beginning: int, maximum: int):
    for i in range (beginning, maximum + 1):
        if i % 2 == 0: 
            yield i


# model solution 
def even_numbers(beginning: int, maximum: int):
    if beginning % 2 != 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning
        beginning += 2
 
```

---

### **Programming Exercise: Prime Numbers**

**Task**:
Write a generator function `prime_numbers()` which returns prime numbers, one by one in sequence, from 2 onwards.

**Output**: 
The generator should return new prime numbers, one by one in sequence, from 2 onwards.

---

**Example**:

```python
numbers = prime_numbers()
for i in range(8):
    print(next(numbers))
```

**Expected Output**:
```
2
3
5
7
11
13
17
19
```

---

**Your Solution**:

```python
# Place your solution here

def prime_numbers():
    def is_prime(num):
        if num < 2:
            return False

        for i in range (2, num - 1):
            if num % i == 0: 
                return False
        return True

    num = 2
    while True:
        if is_prime(num):
            yield num 
        num += 1

if __name__ == "__main__":

    # Test the generator
    numbers = prime_numbers()
    for i in range(8):
        print(next(numbers))
```