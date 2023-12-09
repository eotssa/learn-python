

## Object-Oriented Programming Techniques

### Learning Objectives
After this section, you will:
- Understand the different uses of the `self` variable
- Learn how to overload operators in your own classes
- Know how to create an iterable class

### Working with `self` Variable

The `self` variable refers to the object itself and is used to refer to the object's attributes and methods.

```python
class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    def product_on_sale(self):
        on_sale = Product(self.__name, self.__price * 0.75)
        return on_sale

apple1 = Product("Apple", 2.99)
apple2 = apple1.product_on_sale()
print(apple1) # Apple (price 2.99)
print(apple2) # Apple (price 2.2425)
```

### Overloading Operators

You can overload Python's built-in operators to work with instances of your classes. Here's an example of overloading the `>` operator:

```python
def __gt__(self, another_product):
    return self.price > another_product.price
```

### More Operators

You can implement various operators:

- Comparison: `<` (`__lt__`), `>` (`__gt__`), `==` (`__eq__`), `!=` (`__ne__`), `<=` (`__le__`), `>=` (`__ge__`)
- Arithmetic: `+` (`__add__`), `-` (`__sub__`), `*` (`__mul__`), `/` (`__truediv__`), `//` (`__floordiv__`)

### A String Representation of an Object

You can use the `__str__` and `__repr__` methods to define human-readable and technical representations of an object.

```python
class Person:
    def __str__(self):
        return f"{self.name} ({self.age} years)"
    def __repr__(self):
        return f"Person({repr(self.name)}, {self.age})"
```

### Iterators

By implementing the `__iter__` and `__next__` methods, you can make your classes iterable:

```python
class Bookshelf:
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n < len(self._books):
            book = self._books[self.n]
            self.n += 1
            return book
        else:
            raise StopIteration

b1 = Book("The Life of Python", "Montague Python", 123)
b2 = Book("The Old Man and the C", "Ernest Hemingjavay", 204)
b3 = Book("A Good Cup of Java", "Caffee Coder", 997)
shelf = Bookshelf()
shelf.add_book(b1)
shelf.add_book(b2)
shelf.add_book(b3)
for book in shelf:
    print(book)
```

