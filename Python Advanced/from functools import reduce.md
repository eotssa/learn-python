# `reduce`
`reduce` is a function from the `functools` module. As the name implies, its purpose is to reduce the items in a series into a single value.

`reduce` begins with an operation and an initial value. It performs the given operation on each item in the series in turn, so that the value changes at each step. Once all items have been processed, the resulting value is returned.

Here's how to use `reduce` for summation of a list of integers:

```python
from functools import reduce

my_list = [2, 3, 1, 5]
sum_of_numbers = reduce(lambda reduced_sum, item: reduced_sum + item, my_list, 0)
print(sum_of_numbers)
```

**Sample output:**
```
11
```

The first argument to `reduce` is a function, which represents the operation we want to perform on each item. In this case, it's an anonymous `lambda` function:

```python
lambda reduced_sum, item: reduced_sum + item
```

This function takes two arguments: the current reduced value and the item being processed. These are used to calculate a new reduced value.

Let's understand `reduce` better by using a named function:

```python
from functools import reduce

my_list = [2, 3, 1, 5]

def sum_helper(reduced_sum, item):
    print(f"the reduced sum is now {reduced_sum}, next item is {item}")
    return reduced_sum + item

sum_of_numbers = reduce(sum_helper, my_list, 0)
print(sum_of_numbers)
```

**Sample output:**
```
the reduced sum is now 0, next item is 2
the reduced sum is now 2, next item is 3
the reduced sum is now 5, next item is 1
the reduced sum is now 6, next item is 5
11
```

For multiplication, we can make a few changes:

```python
from functools import reduce

my_list = [2, 2, 4, 3, 5, 2]
product_of_list = reduce(lambda product, item: product * item, my_list, 1)
print(product_of_list)
```

**Sample output:**
```
480
```

Now, let's explore a more complex example. We'll use `reduce` to calculate the total balance across all bank accounts:

```python
class BankAccount:
    def __init__(self, account_number: str, name: str, balance: float):
        self.__account_number = account_number
        self.name = name
        self.__balance = balance

    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance

a1 = BankAccount("123456", "Randy Riches", 5000)
a2 = BankAccount("12321", "Paul Pauper", 1)
a3 = BankAccount("223344", "Mary Millionaire ", 1000000)
accounts = [a1, a2, a3]

from functools import reduce

def balance_sum_helper(balance_sum, account):
    return balance_sum + account.get_balance()

balances_total = reduce(balance_sum_helper, accounts, 0)
print("The total of the bank's balances:")
print(balances_total)
```

**Sample output:**
```
The total of the bank's balances:
1005001
```

### Reduce without an initial value

You don't always need to pass a third argument to `reduce`. For instance:

```python
my_list = [2, 3, 1, 5]
sum_of_numbers = reduce(lambda reduced_sum, item: reduced_sum + item, my_list)
print(sum_of_numbers)
```

If the initial value is omitted, `reduce` takes the first item in the list as the initial value and starts reducing from the second item.

However, if the items in the series are of a different type than the intended reduced result, the third argument is mandatory.

---

### **Programming Exercise: Study credits**
**Points:** 0/3

---

**Introduction:**
In this exercise, you will be working with a modified version of the `CourseAttempt` class. The student's name is omitted, but the number of credits is included.

---

**Class Definition:**

```python
class CourseAttempt:
    def __init__(self, course_name, grade, credits):
        # Constructor contents

    # Sample Usage:
    attempt = CourseAttempt("Data Structures and Algorithms", 3, 10)
    print(attempt)  # Expected Output: Data Structures and Algorithms (10 cr) grade 3
    print(attempt.course_name)  # Expected Output: Data Structures and Algorithms
    print(attempt.credits)  # Expected Output: 10
    print(attempt.grade)  # Expected Output: 3
```

---

**1. The sum of all credits:**

Implement a function named `sum_of_all_credits`:

```python
def sum_of_all_credits(attempts: list) -> int:
    pass
```

- **Input:** A list of `CourseAttempt` objects named `attempts`.
- **Output:** The function should return the sum of credits for all the courses.
- **Note:** Implement using the `reduce` function.

**Sample Usage:**
```python
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 4, 5)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_all_credits([s1, s2, s3])
print(credit_sum)  # Expected Output: 20
```

---

**2. The sum of passed credits:**

Implement a function named `sum_of_passed_credits`:

```python
def sum_of_passed_credits(attempts: list) -> int:
    pass
```

- **Input:** A list of `CourseAttempt` objects named `attempts`.
- **Output:** The function should return the sum of credits for the courses with grade 1 or above.
- **Note:** Implement using the `reduce` and `filter` functions.

**Sample Usage:**
```python
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
credit_sum = sum_of_passed_credits([s1, s2, s3])
print(credit_sum)  # Expected Output: 15
```

---

**3. Average grade for passed courses:**

Implement a function named `average`:

```python
def average(attempts: list) -> float:
    pass
```

- **Input:** A list of `CourseAttempt` objects named `attempts`.
- **Output:** The function should return the average grade for the course attempts with grade 1 or above. The average should be a simple mean value, not a weighted average.
- **Note:** Implement using the `reduce` and `filter` functions.

**Sample Usage:**
```python
s1 = CourseAttempt("Introduction to Programming", 5, 5)
s2 = CourseAttempt("Advanced Course in Programming", 0, 4)
s3 = CourseAttempt("Data Structures and Algorithms", 3, 10)
ag = average([s1, s2, s3])
print(ag)  # Expected Output: 4.0
```

---

**Hint:** Remember that the return value of `filter` is an iterator. 

---

**Solution Space:**
```python
# Add your solutions here
from functools import reduce

class CourseAttempt:
    def __init__(self, course_name: str, grade: int, credits: int):
        self.course_name = course_name
        self.grade = grade
        self.credits = credits

    def __str__(self):
        return f"{self.course_name} ({self.credits} cr) grade {self.grade}"

# Write your solution

def sum_of_all_credits(attempts: list):
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, attempts, 0)

def sum_of_passed_credits(attempts: list):
    passed_attempts = filter(lambda attempt: attempt.grade >= 1, attempts)
    return reduce(lambda reduced_sum, attempt: reduced_sum + attempt.credits, passed_attempts, 0)

def average(attempts: list):
    # because I use passed_attempts twice, need to convert iter -> list otherwise the object is "used" after 1st go through. 
    passed_attempts = list(filter(lambda attempt: attempt.grade >= 1, attempts))
    total = reduce(lambda reduced_sum, attempt: reduced_sum + attempt.grade, passed_attempts, 0)
    num_courses = reduce(lambda reduced_sum, attempt: reduced_sum + 1, passed_attempts, 0)

    # print(total)
    # print(num_courses)
    return total / num_courses
```