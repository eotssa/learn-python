You may remember that lists do not contain any objects themselves. They contain references to objects. The exact same object can appear multiple times in a single list, and it can be referred to multiple times within the list or outside it. Let's have a look at an example:

```python
class Product:
    def __init__(self, name: int, unit: str):
        self.name = name
        self.unit = unit


if __name__ == "__main__":
    shopping_list = []
    milk = Product("Milk", "litre")

    shopping_list.append(milk)
    shopping_list.append(milk)
    shopping_list.append(Product("Cucumber", "piece"))
9 1 1
If there is more than one reference to the same object, it makes no difference which one of the references is used:

class Dog:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

dogs = []
fluffy = Dog("Fluffy")
dogs.append(fluffy)
dogs.append(fluffy)
dogs.append(Dog("Fluffy"))

print("Dogs initially:")
for dog in dogs:
    print(dog)

print("The dog at index 0 is renamed:")
dogs[0].name = "Pooch"
for dog in dogs:
    print(dog)

print("The dog at index 2 is renamed:")
dogs[2].name = "Fifi"
for dog in dogs:
    print(dog)
```

```
Dogs initially:
Fluffy
Fluffy
Fluffy
The dog at index 0 is renamed:
Pooch
Pooch
Fluffy
The dog at index 2 is renamed:
Pooch
Pooch
Fifi
```


# Self or no self?
**In conclusion, if you need helper variables for use within a single method, the correct way to do it is without self. To make your code easier to understand, also use informative variable names:**

# Objects as arguments to functions

Similarly, objects can act as arguments to methods. Let's have a look at an example from an amusement park:

```python
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

class Attraction:
    def __init__(self, name: str, min_height: int):
        self.visitors = 0
        self.name = name
        self.min_height = min_height

    def admit_visitor(self, person: Person):
        if person.height >= self.min_height:
            self.visitors += 1
            print(f"{person.name} got on board")
        else:
            print(f"{person.name} was too short :(")

    def __str__(self):
        return f"{self.name} ({self.visitors} visitors)"
```
```
rollercoaster = Attraction("Rollercoaster", 120)
jared = Person("Jared", 172)
alice = Person("Alice", 105)

rollercoaster.admit_visitor(jared)
rollercoaster.admit_visitor(alice)

print(rollercoaster)
```
```
Jared got on board
Alice was too short :(
Rollercoaster (1 visitors)
```


# An instance of the same class as an argument to a method

**One of the principles of object oriented programming is to include any functionality which handles objects of a certain type in the class definition, as methods. So instead of a function we could write a method which allows us to compare the age of a Person object to another Person object:**

```python
class Person:
    def __init__(self, name: str, year_of_birth: int):
        self.name = name
        self.year_of_birth = year_of_birth

    # NB: type hints must be enclosed in quotation marks if the parameter
    # is of the same type as the class itself!
    def older_than(self, another: "Person"):
        if self.year_of_birth < another.year_of_birth:
            return True
        else:
            return False
```

Here the object which the method is called on is referred to as self, while the other Person object is another.

Remember, calling a method differs from calling a function. A method is attached to an object with the dot notation:

```python
muhammad = Person("Muhammad ibn Musa al-Khwarizmi", 780)
pascal = Person("Blaise Pascal", 1623)
grace = Person("Grace Hopper", 1906)

if muhammad.older_than(pascal):
    print(f"{muhammad.name} is older than {pascal.name}")
else:
    print(f"{muhammad.name} is not older than {pascal.name}")

if grace.older_than(pascal):
    print(f"{grace.name} is older than {pascal.name}")
else:
    print(f"{grace.name} is not older than {pascal.name}")
```

To the left of the dot is the object itself, which is referred to as self within the method definition. In parentheses is the argument to the method, which is the object referred to as another.

The printout from the program is exactly the same as with the function implementation above.

A rather cosmetic point to finish off: the if...else structure in the method older_than is by and large unneccessary. The value of the Boolean expression in the condition is already the exact same truth value which is returned. The method can thus be simplified:
```python
class Person:
    def __init__(self, name: str, year_of_birth: int):
        self.name = name
        self.year_of_birth = year_of_birth

    # NB: type hints must be enclosed in quotation marks if the parameter 
    # is of the same type as the class itself!
    def older_than(self, another: "Person"):
        return self.year_of_birth < another.year_of_birth:
```


```