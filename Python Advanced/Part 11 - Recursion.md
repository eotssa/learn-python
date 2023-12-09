## Recursion in Programming

### Learning Objectives
* Understand the meaning of recursion
* Ability to write a simple recursive function

### Introduction

* Functions can call other functions. For instance:
  ```python
  def hello(name: str):
      print("Hello", name)

  def hello_many_times(name: str, times: int):
      for i in range(times):
          hello(name)
  ```
* A function can also call itself (known as recursion), but there's a risk of endless loops.
  ```python
  def hello(name: str):
      print("Hello", name)
      hello(name)  # function calls itself
  ```
  This would result in an error: `RecursionError: maximum recursion depth exceeded`

### Understanding Recursion

* Recursion means defining something in terms of itself.
* For recursion to work without causing infinite loops, arguments passed must change each time, ensuring termination.
* An example of a simple recursive function to add zeroes to a list until it has 10 items:
  ```python
  def fill_list(numbers: list):
      if len(numbers) < 10:
          numbers.append(0)
          fill_list(numbers)
  ```

* The same task can be done using an iterative (loop) approach:
  ```python
  def fill_list(numbers: list):
      while len(numbers) < 10:
          numbers.append(0)
  ```

### Iterative vs Recursive

* **Iterative** solutions use sequential processing, mostly using loops.
* **Recursive** methods involve a function calling itself with varied parameter values.
* Each method has its own use cases, and choosing between them comes with experience.

### Exercises and Examples

1. **Programming Exercise:** Create a recursive function `add_numbers_to_list(numbers: list)` to add numbers until the list length is divisible by five.
   ```python
   def add_numbers_to_list(numbers: list):
       # Implementation goes here
   ```

2. **Factorial using Recursion:** A factorial function is demonstrated recursively.
   ```python
   def factorial(n: int):
       if n < 2:
           return 1
       return n * factorial(n - 1)
   ```

   The recursion ends when `n < 2` is met. The factorial function uses a helper variable to store return values. Visualizing the function calls can help understand recursion better.

3. **Fibonacci Series using Recursion:** The Fibonacci sequence is another example. Each number is a sum of the preceding two numbers, starting with two 1's.
   ```python
   def fibonacci(n: int):
       if n <= 2:
           return 1
       return fibonacci(n - 1) + fibonacci(n - 2)
   ```

   This function returns 1 if n is 1 or 2. For any other value of n, it uses the recursive formula. The function's workings can be analyzed and verified step-by-step.

