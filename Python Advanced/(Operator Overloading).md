#### Learning Objectives

After this section, you'll be able to understand:

- The different uses for the variable name `self`.
- How to overload operators in your own classes.
- How to create an iterable class.
- How a class can contain a method which returns an object of the very same class.

#### Class that Returns an Object of the Same Class

You can create a class that returns an object of the same class. For example:

```python
class Product:
    def product_on_sale(self):
        on_sale = Product(self.__name, self.__price * 0.75)
        return on_sale
```

##### Sample Code and Output

```python
apple1 = Product("Apple", 2.99)
apple2 = apple1.product_on_sale()
print(apple1) # Apple (price 2.99)
print(apple2) # Apple (price 2.2425)
```

#### The Purpose of `self`

The variable `self` refers to the object itself and is used to refer to the object's own traits, attributes, and methods.

#### Overloading Operators

You can use specially named built-in methods for working with standard arithmetic and comparison operators.

##### Greater Than Operator

Implementing the `__gt__` method enables the use of the `>` operator:

```python
def __gt__(self, another_product):
    return self.price > another_product.price
```

##### Sample Output with Different Criteria

Based on price:

```python
# Apple is greater
```

Based on alphabetical order:

```python
# Orange is greater
```

##### More Operators

You can also implement methods for other comparison and arithmetic operators:

| Operator | Traditional Meaning                  | Name of Method               |
|----------|--------------------------------------|------------------------------|
| `<`      | Less than                            | `__lt__(self, another)`     |
| `>`      | Greater than                         | `__gt__(self, another)`     |
| `==`     | Equal to                             | `__eq__(self, another)`     |
| `!=`     | Not equal to                         | `__ne__(self, another)`     |
| `<=`     | Less than or equal to                | `__le__(self, another)`     |
| `>=`     | Greater than or equal to             | `__ge__(self, another)`     |
| `+`      | Addition                             | `__add__(self, another)`    |
| `-`      | Subtraction                          | `__sub__(self, another)`    |
| `*`      | Multiplication                       | `__mul__(self, another)`    |
| `/`      | Division (floating point result)     | `__truediv__(self, another)`|
| `//`     | Division (integer result)            | `__floordiv__(self, another)`|


##### Example: Note Class with Addition Operator

```python
from datetime import datetime

class Note:
    def __add__(self, another):
        new_note = Note(datetime.now(), "")
        new_note.entry = self.entry + " and " + another.entry
        return new_note
```

###### Sample Output

```python
# 2020-09-09 14:13:02.163170: Remember to buy presents and Remember to get a tree
```

#### String Representation of an Object

Two similar methods: `__str__` and `__repr__`. 

- `__str__`: Returns a string representation of the object.
- `__repr__`: Returns a technical representation of the object.

##### Example

```python
class Person:
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"
    def __str__(self):
        return f"{self.name} ({self.age} years)"
```

###### Sample Output

```python
# Anna (25 years)
# Person('Anna', 25)
```

In data structures like lists, Python always uses the `__repr__` method:

```python
# [Person('Anna', 25), Person('Peter', 99), Person('Mary', 55)]
```