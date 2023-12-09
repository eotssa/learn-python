## Object-Oriented Programming in Python

### 1. Using Class Instances as Attributes

#### a. Defining Classes with Mutable Attributes:

**Course Class**:

```python
class Course:
    def __init__(self, name: str, code: str, credits: int):
        self.name = name
        self.code = code
        self.credits = credits
```

**Student Class**:

```python
class Student:
    def __init__(self, name: str, student_number: str, credits: int):
        self.name = name
        self.student_number = student_number
        self.credits = credits
```

**CompletedCourse Class**:

```python
from course import Course
from student import Student

class CompletedCourse:
    def __init__(self, student: Student, course: Course, grade: int):
        self.student = student
        self.course = course
        self.grade = grade 
```

- Instances of classes can be used as attributes within other classes.
- This technique is showcased in the `CompletedCourse` class, which takes a `Student` and a `Course` instance as attributes.

#### b. Understanding Attribute Access:

- In the line `print(course.student.name)`, the attribute access is taking place as follows:
    - `course` is an instance of `CompletedCourse`.
    - `student` refers to the `Student` object in the `CompletedCourse` object.
    - `name` is the attribute in the `Student` object containing the student's name.

### 2. Import Statements

- An import statement is necessary when utilizing code defined outside the current file.
- Importing classes from other files was demonstrated above.
- Standard library modules can also be imported, as in `import math`.

### 3. Using a List of Objects as an Attribute

- Classes can have a collection of objects as an attribute.

**Example - Player & Team**:

```python
class Player:
    # ...

class Team:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def add_player(self, player: Player):
        self.players.append(player)
```

- The `Team` class has a list of `Player` objects as an attribute.

### 4. None: A Reference to Nothing

- `None` represents a reference to an "empty" object.
- It can be used when a reference is needed for something that doesn't exist, but care must be taken to avoid accessing attributes or methods on `None`.

```python
player = ca.find_player("Charlie")
if player is not None:
    print(f"Goals by Charlie: {player.goals}")
else:
    print(f"Charlie doesn't play in Campus Allstars :(")
```

### Conclusion

The principles discussed include the use of instances of classes as attributes in other classes, understanding attribute access through dots, import statements, handling collections of objects as attributes, and dealing with `None`. These concepts are essential in object-oriented programming and enable more flexible and modular code.