# Functional Programming

Functional programming refers to a programming paradigm which avoids changes in program state as much as possible. Variables are generally avoided. Instead, chains of function calls form the backbone of the program.

Lambda expressions and different types of comprehensions are common techniques in the functional programming style. They let you process data without storing it in variables, ensuring the state of the program does not change. For example, a lambda expression is essentially a function, but we do not need to store a named reference to it anywhere.

As mentioned above, functional programming is a programming paradigm or a style of programming. There are many different programming paradigms, and we've already encountered some of them:

- **Imperative programming**, where the program consists of a sequence of commands executed in order.
- **Procedural programming**, where the program is grouped into procedures or sub-programs.
- **Object-oriented programming**, where the program and its state are stored in objects defined in classes.

There are differing opinions on the divisions between these paradigms. For example, some argue that imperative and procedural programming are the same, while others view imperative programming as an umbrella term covering both procedural and object-oriented programming. The terminology and divisions aren't crucial. What's important is recognizing that these different approaches exist, influencing the decisions programmers make.

Many programming languages cater to a specific paradigm, but Python is versatile. It supports several paradigms within a single program, allowing programmers to choose the most efficient method for each problem.

## Functional Programming Tools in Python

### `map`

The `map` function executes an operation on each item in an iterable series. This effect is similar to comprehensions, but with a different syntax.

```python
str_list = ["123","-10", "23", "98", "0", "-110"]
integers = map(lambda x : int(x), str_list)
print(integers)
for number in integers:
    print(number)
```

**Sample output:**
```
<map object at 0x0000021A4BFA9A90>
123
-10
23
98
0
-110
```

The general syntax for the `map` function is:

```python
map(<function>, <series>)
```

The `map` function returns an iterable `map` object, which can be converted into a list:

```python
def capitalize(my_string: str):
    first = my_string[0]
    first = first.upper()
    return first + my_string[1:]

test_list = ["first", "second", "third", "fourth"]
capitalized = map(capitalize, test_list)
capitalized_list = list(capitalized)
print(capitalized_list)
```

**Sample output:**
```
['First', 'Second', 'Third', 'Fourth']
```

The same result can be achieved with a list comprehension or a for loop. Knowing various approaches lets you choose the most appropriate one for each situation.

### `map` with Custom Classes

Custom classes can also be processed using the `map` function:

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
a3 = BankAccount("223344", "Mary Millionaire", 1000000)

accounts = [a1, a2, a3]
clients = map(lambda t: t.name, accounts)
for name in clients:
    print(name)

balances = map(lambda t: t.get_balance(), accounts)
for balance in balances:
    print(balance)
```

**Sample output:**
```
Randy Riches
Paul Pauper
Mary Millionaire
5000
1
1000000
```

---

### **Programming Exercise: Attempted courses**

---

**Task**:
The exercise deals with a class named `CourseAttempt` which contains attributes for `student_name`, `course_name`, and `grade`. You need to implement two functions that deal with lists of `CourseAttempt` objects.

---

### **Names of students**

**Function**:
```python
def names_of_students(attempts: list) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts`.

**Output**: 
- The function should return a list containing the names of students who have attempted the course.

**Note**: Please implement the function using the `map` function.

**Example**:

```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)
```

**Sample Output**:
```
Peter Python
Olivia C. Objective
Peter Python
```

---

### **Courses **

**Function**:
```python
def course_names(attempts: list) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts`.

**Output**: 
- The function should return a list containing the names of the courses from the original list in alphabetical order. Each course name should appear only once on the list.

**Note**: Please implement the function using the `map` function. Additionally, you'll need to ensure that the course names are unique.

**Example**:

```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in course_names([s1, s2, s3]):
    print(name)
```

**Sample Output**:
```
Advanced Course in Programming
Introduction to Programming
```

**Solution**
```
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

# takes list of CourseAttempt objects -> list of names of students who have attempted the the course
# implemented using map 
def names_of_students(attempts: list):
    return list(map(lambda course : course.student_name, attempts))

# takes list of CourseAttempt objects -> list containing unique names of the course in the original list in alphabetical order
def course_names(attempts: list):
    return sorted(list(set((map(lambda course : course.course_name, attempts)))))

```



### **Programming Exercise: Attempted courses**

**Task**:
You'll be working with a `CourseAttempt` class. Various functions have to be implemented to process a list of `CourseAttempt` objects based on different criteria.

---

**CourseAttempt Example Usage**

```python
attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
print(attempt.student_name)  # Peter Python
print(attempt.course_name)  # Introduction to Programming
print(attempt.grade)  # 5
print(attempt)  # Peter Python, grade for the course Introduction to Programming 5
```

---

**Names of students**

**Function**:
```python
def names_of_students(attempts: list) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts`.

**Output**: 
- The function should return a new list with the names of the students who have attempted the course.

**Note**: Implement the function using the `map` function.

**Example**:
```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in names_of_students([s1, s2, s3]):
    print(name)
```

**Sample Output**:
```
Peter Python
Olivia C. Objective
Peter Python
```

---

**Courses**

**Function**:
```python
def course_names(attempts: list) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts`.

**Output**: 
- The function should return a new list containing the names of the courses on the original list in alphabetical order. Each course name should appear only once on the list.

**Note**: Implement the function using the `map` function. You will need to use additional logic to ensure the course names are unique and are in alphabetical order.

**Example**:
```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

for name in course_names([s1, s2, s3]):
    print(name)
```

**Sample Output**:
```
Advanced Course in Programming
Introduction to Programming
```

---

**Your Solution**:

```python
# Add your solutions here
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# Write your solution here

# takes list of CourseAttempt objects -> list of names of students who have attempted the the course
# implemented using map 
def names_of_students(attempts: list):
    return list(map(lambda course : course.student_name, attempts))

# takes list of CourseAttempt objects -> list containing unique names of the course in the original list in alphabetical order
def course_names(attempts: list):
    return sorted(list(set((map(lambda course : course.course_name, attempts)))))

if __name__ == "__main__":

    attempt = CourseAttempt("Peter Python", "Introduction to Programming", 5)
    print(attempt.student_name)
    print(attempt.course_name)
    print(attempt.grade)
    print(attempt)


    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in names_of_students([s1, s2, s3]):
        print(name)

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 2)

    for name in course_names([s1, s2, s3]):
        print(name)
```

---

# `filter`

The built-in Python function `filter` is similar to the `map` function. However, as the name implies, it doesn't process all the items from the source. Instead, it filters them based on a criterion function passed as an argument. If the criterion function returns `True`, the item is selected.

Here's an example using `filter`:

```python
integers = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]
even_numbers = filter(lambda number: number % 2 == 0, integers)

for number in even_numbers:
    print(number)
```

**Sample output:**
```
2
6
4
10
14
```

Using a named function might make the example clearer:

```python
def is_it_even(number: int):
    if number % 2 == 0:
        return True
    return False

integers = [1, 2, 3, 5, 6, 4, 9, 10, 14, 15]
even_numbers = filter(is_it_even, integers)

for number in even_numbers:
    print(number)
```

Both programs are functionally identical. The choice of approach is a matter of preference.

Here's another filtering example, where the program models fishes and selects only those weighing at least 1000 grams:

```python
class Fish:
    """ The class models a fish of a certain species and weight """
    def __init__(self, species: str, weight: int):
        self.species = species
        self.weight = weight

    def __repr__(self):
        return f"{self.species} ({self.weight} g.)"

if __name__ == "__main__":
    f1 = Fish("Pike", 1870)
    f2 = Fish("Perch", 763)
    f3 = Fish("Pike", 3410)
    f4 = Fish("Cod", 2449)
    f5 = Fish("Roach", 210)

    fishes = [f1, f2, f3, f4, f5]

    over_a_kilo = filter(lambda fish: fish.weight >= 1000, fishes)

    for fish in over_a_kilo:
        print(fish)
```

**Sample output:**
```
Pike (1870 g.)
Pike (3410 g.)
Cod (2449 g.)
```

The same result can be achieved using a list comprehension:

```python
over_a_kilo = [fish for fish in fishes if fish.weight >= 1000]
```

## The Return Value of `filter` is an Iterator

The `filter` function, like `map`, returns an iterator. Since iterators can only be traversed once, there are situations where one should be cautious when using `filter`. For instance, trying to print out a filtered collection twice may not work as expected:

```python
f1 = Fish("Pike", 1870)
f2 = Fish("Perch", 763)
f3 = Fish("Pike", 3410)
f4 = Fish("Cod", 2449)
f5 = Fish("Roach", 210)

fishes = [f1, f2, f3, f4, f5]

over_a_kilo = filter(lambda fish: fish.weight >= 1000, fishes)

for fish in over_a_kilo:
    print(fish)

print("print the same again:")

for Fish in over_a_kilo:
    print(Fish)
```

**Sample output:**
```
Pike (1870 g.)
Pike (3410 g.)
Cod (2449 g.)
print the same again:
```

To iterate over the contents of a `filter` result more than once, one can convert the result into a list:

```python
fishes = [f1, f2, f3, f4, f5]
over_a_kilo = list(filter(lambda fish: fish.weight >= 1000, fishes))
```

---

### **Programming Exercise: Filtering attempts**

**Task**:
This exercise revolves around the `CourseAttempt` class. Various functions need to be implemented to filter through a list of `CourseAttempt` objects based on different criteria.

---

**Accepted attempts**

**Function**:
```python
def accepted(attempts: list) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts`.

**Output**: 
- The function should return a new list of `CourseAttempt` objects, including only those items from the original list whose grade is at least 1.

**Note**: Implement the function using the `filter` function.

**Example**:
```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

for attempt in accepted([s1, s2, s3]):
    print(attempt)
```

**Sample Output**:
```
Peter Python, grade for the course Introduction to Programming 3
Olivia C. Objective grade for the course Introduction to Programming 5
```

---

**Attempts with grade**

**Function**:
```python
def attempts_with_grade(attempts: list, grade: int) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts` and an integer `grade`.

**Output**: 
- The function should return a new list containing only those `CourseAttempt` objects from the original list whose grade matches the provided grade.

**Note**: Implement the function using the `filter` function.

**Example**:
```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
    print(attempt)
```

**Sample Output**:
```
Peter Python, grade for the course Introduction to Programming 3
Peter Python, grade for the course Introduction to AI 3
Olivia C. Objective, grade for the course Data Structures and Algorithms 3
```

---

**Students who passed the course**

**Function**:
```python
def passed_students(attempts: list, course: str) -> list:
    pass
```

**Input**:
- A list of `CourseAttempt` objects named `attempts` and a string `course`.

**Output**: 
- The function should return an alphabetically ordered list of names of those students who passed the specified course, i.e., their grade for the given course was higher than 0.

**Note**: Implement the function using the `filter` and `map` functions.

**Example**:
```python
s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
    print(attempt)
```

**Sample Output**:
```
Jack Java
Olivia C. Objective
```

---

**Your Solution**:

```python
# Add your solutions here
class CourseAttempt:
    def __init__(self, student_name: str, course_name: str, grade: int):
        self.student_name = student_name
        self.course_name = course_name
        self.grade = grade

    def __str__(self):
        return f"{self.student_name}, grade for the course {self.course_name} {self.grade}"

# obj list -> list with grade of >= 1
def accepted(attempts: list):
    return filter(lambda x : x.grade >= 1, attempts)

def attempts_with_grade(attempts: list, grade: int):
    return filter(lambda x : x.grade == grade, attempts)

# obj list -> alphabetically ordered list of names who passed course
def passed_students(attempts: list, course: str):
    passed = filter(lambda x : x.grade > 0 and x.course_name == course, attempts)
    passed = map(lambda n : n.student_name, passed)
    return sorted(passed)

if __name__ == "__main__":
    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Advanced Course in Programming", 0)

    for attempt in accepted([s1, s2, s3]):
        print(attempt)



    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to Programming", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 3)
    s4 = CourseAttempt("Olivia C. Objective", "Data Structures and Algorithms", 3)

    for attempt in attempts_with_grade([s1, s2, s3, s4], 3):
        print(attempt)

    s1 = CourseAttempt("Peter Python", "Introduction to Programming", 3)
    s2 = CourseAttempt("Olivia C. Objective", "Introduction to AI", 5)
    s3 = CourseAttempt("Peter Python", "Introduction to AI", 0)
    s4 = CourseAttempt("Jack Java", "Introduction to AI", 3)

    for attempt in passed_students([s1, s2, s3, s4], "Introduction to AI"):
        print(attempt)
```