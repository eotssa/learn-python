# Classes: Point and Line

- These classes are designed to model a point in a two-dimensional space and a line segment between two points.

```python
import math

class Point:
    """ The class represents a point in two-dimensional space """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    @classmethod
    def origo(cls):
        return Point(0, 0)

    @classmethod
    def mirrored(cls, point: "Point", mirror_x: bool, mirror_y: bool):
        x = point.x
        y = point.y
        if mirror_x:
            y = -y
        if mirror_y:
            x = -x
        return Point(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Line:
    """ The class represents a line segment in two-dimensional space """

    def __init__(self, beginning: Point, end: Point):
        self.beginning = beginning
        self.end = end

    def length(self):
        sum_of_squares = (self.end.x - self.beginning.x) ** 2 + (self.end.y - self.beginning.y) ** 2
        return math.sqrt(sum_of_squares)

    def centre_point(self):
        centre_x = (self.beginning.x + self.end.x) / 2
        centre_y = (self.beginning.y + self.end.y) / 2
        return Point(centre_x, centre_y)

    def __str__(self):
        return f"{self.beginning} ... {self.end}"
```

**Usage:**
```python
point = Point(1,3)
print(point)  # Output: (1, 3)

origo = Point.origo()
print(origo)  # Output: (0, 0)

point2 = Point.mirrored(point, True, True)
print(point2)  # Output: (-1, -3)

line = Line(point, point2)
print(line.length())  # Output: 6.324555320336759
print(line.centre_point())  # Output: (0.0, 0.0)
print(line)  # Output: (1, 3) ... (-1, -3)
```

---

# Default Values of Parameters

- Python allows default values for function/method parameters.
- If no argument is provided, the default is used.
- Default values can ensure object integrity.

**Example with `Student` class:**

```python
class Student:
    """ This class models a student """

    def __init__(self, name: str, student_number: str, credits: int = 0, notes: str = ""):
        self.name = name
        if len(student_number) < 5:
            raise ValueError("A student number should have at least five characters")
        self.__student_number = student_number
        self.credits = credits
        self.__notes = notes

    # [Other methods and properties are here...]

    def summary(self):
        print(f"Student {self.__name} ({self.student_number}):")
        print(f"- credits: {self.__credits}")
        print(f"- notes: {self.notes}")
```

**Usage:**
```python
student1 = Student("Sally Student", "12345")
student1.summary()  # Displays student summary...

# ... additional usage examples ...
```

> **Note:** There's no setter for `student_number` since it shouldn't change.

---

## Pitfall: Mutable Default Values

- Default mutable values (e.g., lists) can cause unexpected behavior due to shared references.

**Flawed Example:**

```python
class Student:
    def __init__(self, name, completed_courses=[]):
        self.name = name
        self.completed_courses = completed_courses
```

**Improved Version:**
```python
class Student:
    def __init__(self, name, completed_courses=None):
        self.name = name
        if completed_courses is None:
            self.completed_courses = []
        else:
            self.completed_courses = completed_courses
```



