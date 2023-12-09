Certainly! Below, you'll find a summarization of the material you provided, organized in markdown format to resemble master-level student's notes.

### Scope of Methods

#### Learning Objectives
- Understanding how to limit the visibility of a method in Python.
- Writing private methods.
- Learning the difference between the scope of a method, a class, and client code.

#### Private Attributes and Methods
Attributes and methods can be hidden by beginning them with two underscores `__`, making them private. While private attributes often come paired with getter and setter methods to control access, private methods are typically intended for internal use.

##### Example: Private Attribute and Method
```python
class Recipient:
    def __init__(self, name: str, email: str):
        self.__name = name
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")

    def __check_email(self, email: str):
        return len(email) > 5 and "." in email and "@" in email

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        if self.__check_email(email):
            self.__email = email
        else:
            raise ValueError("The email address is not valid")
```
- Accessing a private method directly will result in an `AttributeError`.

#### Python Scope and Namespace
The scope refers to the sections of a program where a name is visible, while the namespace refers to the names specifically available within a defined Python unit.

- **Method Scope**: Access to local variables, attributes, and methods of the class.
- **Class Scope**: Access to attributes and methods of the class, but not to local variables within its methods.
- **Client Code Scope**: Access only to public methods and attributes defined in the class.

Understanding scopes and namespaces is essential for maintaining the integrity of names within a program.

#### When to Use Private Methods
Private methods are generally less common than private attributes. They should be hidden when the client doesn't need direct access to them.

##### Example: Private Helper Method
```python
from random import shuffle

class DeckOfCards:
    def __init__(self):
        self.__reset_deck()

    def __reset_deck(self):
        self.__deck = []
        suits = ["spades", "hearts", "clubs", "diamonds"]
        for suit in suits:
            for number in range(1, 14):
                self.__deck.append((suit, number))
        shuffle(self.__deck)

    def deal(self, number_of_cards: int):
        hand = []
        for i in range(number_of_cards):
            hand.append(self.__deck.pop())
        return hand
```
This example illustrates the use of a private method to enhance code readability and provide potential future flexibility.


