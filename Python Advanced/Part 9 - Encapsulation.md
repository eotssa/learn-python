Certainly! Below is a summary of the provided information, formatted in markdown, including code examples:

## Encapsulation

### Learning Objectives

- Understand the meaning of encapsulation
- Create private attributes
- Know how to create getters and setters for attributes

### Overview

In object-oriented programming, encapsulation refers to the act of hiding certain details of an object from the outside world. This helps to preserve the integrity of the object, ensuring that the internal state of the object remains valid.

#### Example of Integrity Violation

```python
class Student:
    def __init__(self, name: str, student_number: str):
        self.name = name
        self.student_number = student_number
        self.study_credits = 0

    def add_credits(self, study_credits):
        if study_credits > 0:
            self.study_credits += study_credits

sally = Student("Sally Student", "12345")
sally.study_credits = -100  # integrity violation
```

### Private Attributes

Private attributes are hidden from the client. In Python, you can create a private attribute by adding two underscores `__` at the beginning of the attribute name.

```python
class CreditCard:
    def __init__(self, number: str, name: str):
        self.__number = number
        self.name = name
```

### Encapsulated Methods

Encapsulated attributes can be accessed through publicly visible methods, allowing controlled access to the object's data.

```python
class CreditCard:
    def __init__(self, number: str, name: str, balance: float):
        self.__number = number
        self.name = name
        self.__balance = balance

    def deposit_money(self, amount: float):
        if amount > 0:
            self.__balance += amount
```

### Getters and Setters

Getters and setters are methods specifically designed to access and modify the attributes of a class. Python provides the `@property` decorator for defining getters and setters in a pythonic way.

#### Example with Getters and Setters

```python
class Wallet:
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, money):
        if money >= 0:
            self.__money = money
        else:
            raise ValueError("The amount must not be below zero")
```

### Flexibility with Encapsulation

Encapsulation ensures that the internal implementation of the class can be changed without affecting the client's code. It creates a clear boundary between the class's interface and its underlying implementation.

#### Example with Various Interfaces

```python
class Diary:
    def __init__(self, owner: str):
        self.__owner = owner
        self.__entries = []

    @property
    def owner(self):
        return self.__owner

    def add_entry(self, entry: str):
        self.__entries.append(entry)

    def print_entries(self):
        for entry in self.__entries:
            print("- " + entry)
```

This structured approach helps maintain the integrity of the objects, provides a clean and clear interface for clients, and allows flexibility in the internal implementation of the class.


# Benefits of `@property decorator`

The `@property` decorator in Python allows you to define a method that can be accessed like an attribute, providing a way to encapsulate data within a class.

In the example you provided, the `@property` decorator is used with the `owner` method, allowing you to retrieve the value of the private attribute `__owner` without directly accessing it.

Here's how the `@property` decorator contributes to encapsulation:

1. **Access Control**: By using the `__owner` attribute with double underscores, it's marked as private within the class. This is a convention in Python to indicate that the attribute should not be accessed directly outside the class. The `@property` decorator provides a controlled way to access this private attribute, preserving the encapsulation.

2. **Read-Only Property**: Since there's no corresponding setter method for the `owner` property, clients of the class can't change the value of the `__owner` attribute directly. This makes the `owner` attribute read-only, providing further encapsulation.

3. **Flexibility**: By using the `@property` decorator, you can control how the `__owner` attribute is accessed. If, in the future, you need to change how the `owner` value is computed or add additional logic when it is accessed, you can do so within the `owner` method without changing how clients interact with the `Diary` class. This flexibility allows the underlying implementation to be changed without affecting existing code that uses the class.

4. **Abstraction**: The `@property` decorator helps create a clear and clean interface for the class, hiding the underlying implementation details. Clients of the class don't need to know how the `owner` attribute is implemented; they just need to know that they can access it like a regular attribute. This level of abstraction supports the principle of encapsulation.

In summary, the `@property` decorator helps in maintaining the integrity of the object by providing controlled access to its attributes, allowing the internal implementation to be flexible and change without affecting clients' code.

### Explained 

1. **Access Control**:
   The private attribute `__owner` is only accessible through the `owner` property. Trying to access it directly will result in an error.

   ```python
   diary = Diary('Alice')
   print(diary.__owner)  # AttributeError
   print(diary.owner)    # 'Alice' - Correct way to access
   ```

2. **Read-Only Property**:
   Without a corresponding setter method, the `owner` attribute is read-only.

   ```python
   diary = Diary('Alice')
   diary.owner = 'Bob'  # AttributeError, cannot set attribute
   ```

3. **Flexibility**:
   Suppose you later decide that the `owner` attribute should be formatted in a specific way. You can change the `owner` method without affecting how clients interact with the class.

   ```python
   class Diary:
       # ...

       @property
       def owner(self):
           return f"The owner is {self.__owner}"

   diary = Diary('Alice')
   print(diary.owner)    # 'The owner is Alice'
   ```

4. **Abstraction**:
   Clients of the `Diary` class don't need to know the underlying details of the `owner` attribute. Whether it's stored directly, computed on the fly, or retrieved from another source, the client code remains the same.

   ```python
   class Diary:
       # ...

       @property
       def owner(self):
           # Imagine the owner is now derived from a database or other complex logic
           return self.get_owner_from_database()

   diary = Diary('Alice')
   print(diary.owner)    # Same way to access, even though the underlying logic changed
   ```

