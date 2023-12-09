# Validator methods 
```python
 The class definition contains separate validator methods which ascertain that the arguments passed are valid. The methods are called already within the constructor. This ensures the object created is internally sound.

from datetime import date

class PersonalBest:

    def __init__(self, player: str, day: int, month: int, year: int, points: int):
        # Default values
        self.player = ""
        self.date_of_pb = date(1900, 1, 1)
        self.points = 0

        if self.name_ok(player):
            self.player = player

        if self.date_ok(day, month, year):
            self.date_of_pb = date(year, month, day)

        if self.points_ok(points):
            self.points = points

    # Helper methods to check the arguments are valid
    def name_ok(self, name: str):
        return len(name) >= 2 # Name should be at least two characters long

    def date_ok(self, day, month, year):
        try:
            date(year, month, day)
            return True
        except:
            # an exception is raised if the arguments are not valid
            return False

    def points_ok(self, points):
        return points >= 0

if __name__ == "__main__":
    result1 = PersonalBest("Peter", 1, 11, 2020, 235)
    print(result1.points)
    print(result1.player)
    print(result1.date_of_pb)

    # The date was not valid
    result2 = PersonalBest("Paula", 4, 13, 2019, 4555)
    print(result2.points)
    print(result2.player)
    print(result2.date_of_pb) # Tulostaa oletusarvon 1900-01-01
```

# Python Classes and Object-Oriented Programming Concepts

## 1. Self Parameter in Classes

Python classes use a `self` parameter to access instance attributes and methods. 

```python
class MyClass:
    def __init__(self, value):
        self.value = value  # Here, 'self' is used to define an instance attribute
```

## 2. Static Methods

Python allows the definition of static methods within a class. These methods can be invoked without creating an instance of the class.

```python
class MyClass:
    @staticmethod
    def my_static_method():
        print("This is a static method.")
    
MyClass.my_static_method()  # Calling static method without creating an instance
```

## 3. Local Variables in Methods

Within class methods, local variables can be created without the `self` keyword. Such variables are confined to the method where they are defined and can't be accessed outside this method.

```python
class MyClass:
    def my_method(self):
        my_local_var = 10  # This variable can't be accessed outside this method
```

## 4. Attributes and Methods

In Python terminology, instance variables (data attributes) and methods are sometimes collectively referred to as the 'attributes' of an object.

```python
class MyClass:
    def __init__(self, value):
        self.value = value  # This is a data attribute

    def my_method(self):  # This is a method, but can also be considered an 'attribute' of the object
        pass
```



# Special Methods in Python Classes: `__str__` Method

The `__str__` method in Python represents the class objects as a string – it can be used for classes. The `__str__` method should be the most human-readable while `__repr__` is meant to be unambiguous.

## 1. The `__str__` Method

When you print an instance of a class, the `__str__` method is called. This method returns a string that represents the object. You can define your own `__str__` method in your class.

```python
class Rectangle:
    def __init__(self, left_upper, right_lower):
        self.left_upper = left_upper
        self.right_lower = right_lower

    # This method returns the state of the object in string format
    def __str__(self):
        return f"rectangle {self.left_upper} ... {self.right_lower}"
```
Now the `print` command produces something more user-friendly:

```python
rectangle = Rectangle((1, 1), (4, 3))
print(rectangle)  # Calls `__str__` method internally
```
**Sample output**
```
rectangle (1, 1) ... (4, 3)
```

## 2. Usage of `__str__` with `str` Function

The `__str__` method is also used when the `str` function is called on an object. It returns a string which is a human-readable form of the object.

```python
rectangle = Rectangle((1, 1), (4, 3))
str_rep = str(rectangle)  # Calls `__str__` method internally
print(str_rep)
```
**Sample output**
```
rectangle (1, 1) ... (4, 3)
```

This makes it easy to provide a human-readable representation of your class for usage in debugging and logging.

