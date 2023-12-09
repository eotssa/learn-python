## Special Classes for Special Purposes

### Introduction
Programming often involves defining classes with special traits or similar attributes. Inheritance in object-oriented programming allows the creation of a base class containing shared attributes, reducing redundancy.

### Example 1: Student and Teacher Classes

Initial classes for `Student` and `Teacher` are defined, sharing the `name` and `email` attributes.

```python
class Student:
    def __init__(self, name: str, id: str, email: str, credits: str):
        self.name = name
        self.id = id
        self.email = email
        self.credits = credits

class Teacher:
    def __init__(self, name: str, email: str, room: str, teaching_years: int):
        self.name = name
        self.email = email
        self.room = room
        self.teaching_years = teaching_years
```

This leads to repetition if we need to perform actions on common attributes:

```python
def update_email(o: Student):
    o.email = o.email.replace(".com", ".edu")

def update_email2(o: Teacher):
    o.email = o.email.replace(".com", ".edu")
```

### Inheritance

#### Creating a Base Class
To avoid redundancy, we create a `Person` class and make `Student` and `Teacher` inherit from it:

```python
class Person:
   def __init__(self, name: str, email: str):
       self.name = name
       self.email = email

class Student(Person):
   def __init__(self, name: str, id: str, email: str, credits: str):
       self.name = name
       self.id = id
       self.email = email
       self.credits = credits

class Teacher(Person):
   def __init__(self, name: str, email: str, room: str, teaching_years: int):
       self.name = name
       self.email = email
       self.room = room
       self.teaching_years = teaching_years

if __name__ == "__main__":
   saul = Student("Saul Student", "1234", "saul@example.com", 0)
   saul.update_email_domain("example.edu")
   print(saul.email)

   tara = Teacher("Tara Teacher", "tara@example.fi", "A123", 2)
   tara.update_email_domain("example.ex")
   print(tara.email)
```

#### Book Example
Inheritance can also be seen in the `Book`, `BookContainer`, and `Bookshelf` classes:

```python
class Book:
   def __init__(self, name: str, author: str):
       self.name = name
       self.author = author

class BookContainer:
   def __init__(self):
       self.books = []

   def add_book(self, book: Book):
       self.books.append(book)

   def list_books(self):
       for book in self.books:
           print(f"{book.name} ({book.author})")

class Bookshelf(BookContainer):
   def __init__(self):
       super().__init__()

   def add_book(self, book: Book, location: int):
       self.books.insert(location, book)

if __name__ == "__main__":
   #...
   print("Container:")
   container.list_books()

   print()

   print("Shelf:")
   shelf.list_books()
```

### Inheritance and Scope of Traits

#### Constructor Reuse
The constructor of a base class can be reused in the derived class:

```python
class Bookshelf(BookContainer):
   def __init__(self):
       super().__init__()
```

#### Extending the Base Class
The derived class can also add new attributes and call the constructor from the base class:

```python
class Thesis(Book):
    def __init__(self, name: str, author: str, grade: int):
        super().__init__(name, author)
        self.grade = grade
```

#### Overriding Methods
A derived class can override methods and call the overridden method in the base class:

```python
class Product:

    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

class BonusCard:

    def __init__(self):
        self.products_bought = []

    def add_product(self, product: Product):
        self.products_bought.append(product)

    def calculate_bonus(self):
        bonus = 0
        for product in self.products_bought:
            bonus += product.price * 0.05

        return bonus

class PlatinumCard(BonusCard):

    def __init__(self):
	        super().__init__()

    def calculate_bonus(self):
        # Call the method in the base class
        bonus = super().calculate_bonus()

        # ...and add five percent to the total
        bonus = bonus * 1.05
        return bonus
```

### Conclusion
Inheritance is a powerful technique that enables code reuse, enhances readability, and allows the creation of classes with special or shared traits. It provides a structured way to represent relationships between objects, as demonstrated in the examples of students and teachers, books and containers, and bonus cards.