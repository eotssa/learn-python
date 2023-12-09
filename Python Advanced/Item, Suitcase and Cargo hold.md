## My Solution
```python
# Write your solution here:
class Item:
    def __init__(self, name: str, weight: int = 0) -> None:
        self.__name = name     
        self.__weight = weight 

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self) -> str:
        return f"{self.__name} ({self.__weight} kg)"    

# pack Item(s) into Suitcase, keep track of weight 
class Suitcase:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__current_weight = 0
        self.__things = []


    def add_item(self, item: Item):
        if item.weight() + self.__current_weight <= self.__max_weight:
            self.__things.append(item)
            self.__current_weight += item.weight()

    
    def print_items(self):
        for item in self.__things:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__things)

    def heaviest_item(self):
        if len(self.__things) == 0:
            return None

        return max(self.__things, key=lambda item_obj: item_obj.weight())


    def __str__(self) -> str:
        if len(self.__things) == 1: 
            return f"{len(self.__things)} item ({self.__current_weight} kg)"
        else:
            return f"{len(self.__things)} items ({self.__current_weight} kg)"


class CargoHold:
    def __init__(self, max_weight: int) -> None:
        self.__max_weight = max_weight
        self.__current_weight = 0
        self.__things = []

    def add_suitcase(self, suitcase: Suitcase):
        if suitcase.weight() + self.__current_weight <= self.__max_weight:
            self.__things.append(suitcase)
            self.__current_weight += suitcase.weight()    


    def print_items(self):
        for suitcase in self.__things:
            suitcase.print_items()

    def __str__(self) -> str:
        if len(self.__things) == 1:
                return f"{len(self.__things)} suitcase, space for {self.__max_weight - self.__current_weight} kg"    
        else:
            return f"{len(self.__things)} suitcases, space for {self.__max_weight - self.__current_weight} kg"    

```



---

# Programming exercise: Item, Suitcase and Cargo hold

**Points:** 7/7

**Note:** Some exercises have multiple parts, and you can receive points for the different parts separately. You can submit a partially completed exercise by choosing 'Submit Solution' from the menu next to the button for executing tests.

In this series of exercises, you will create the classes Item, Suitcase, and Cargo Hold, which will let you further practice working on objects which contain references to other objects.

## Item

Please create a class named `Item` which is used to create items of different kinds. Each item has a name and a weight (in kilograms).

You can use the following code to test your class:

```python
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)

print("Name of the book:", book.name())
print("Weight of the book:", book.weight())

print("Book:", book)
print("Phone:", phone)
```

**Sample output:**

```
Name of the book: ABC Book
Weight of the book: 2
Book: ABC Book (2 kg)
Phone: Nokia 3210 (1 kg)
```

An `Item` should provide the methods `weight` and `name`, which return the values stored in those attributes. The name and weight should be encapsulated within the class. The following code should not work:

```python
book = Item("ABC Book", 2)
book.weight = 10
```

## Suitcase

Please write a class named `Suitcase`. You should be able to pack items into a suitcase. A suitcase also has a maximum combined weight for the items stored within.

Your class should contains the following members:

- A constructor which takes the maximum weight as an argument.
- A method named `add_item` which adds the item given as an argument to the suitcase. The method has no return value.
- A `__str__` method which returns a string in the format "x items (y kg)".

The class should make sure that the combined weight of the items stored within any `Suitcase` does not exceed the maximum weight set for that instance. If the maximum weight would be exceeded when the `add_item` method is called, the new item should not be added to the suitcase.

**Test code:**

```python
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(5)
print(suitcase)

suitcase.add_item(book)
print(suitcase)

suitcase.add_item(phone)
print(suitcase)

suitcase.add_item(brick)
print(suitcase)
```

**Sample output:**

```
0 items (0 kg)
1 item (2 kg)
2 items (3 kg)
2 items (3 kg)
```

**Hint:** The notification "1 items" is not very grammatical. Instead, it should say "1 item". Please make the required changes to your `__str__` method.

### All the items

Please add the following methods to your `Suitcase` class definition:

- `print_items`: prints out all the items stored in the suitcase.
- `weight`: returns an integer number representing the combined weight of all the items stored in the suitcase.

**Test code:**

```python
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

print("The suitcase contains the following items:")
suitcase.print_items()
combined_weight = suitcase.weight()
print(f"Combined weight: {combined_weight} kg")
```

**Sample output:**

```
The suitcase contains the following items:
ABC Book (2 kg)
Nokia 3210 (1 kg)
Brick (4 kg)
Combined weight: 7 kg
```

### The heaviest item

Please add a new method to your `Suitcase` class: `heaviest_item` should return the `Item` which is the heaviest. If there are two or more items with the same, heaviest weight, the method may return any one of these. The method should return a reference to an object. If the suitcase is empty, the method should return `None`.

**Test code:**

```python
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

suitcase = Suitcase(10)
suitcase.add_item(book)
suitcase.add_item(phone)
suitcase.add_item(brick)

heaviest = suitcase.heaviest_item()
print(f"The heaviest item: {heaviest}")
```

**Sample output:**

```
The heaviest item: Brick (4 kg)
```

## Cargo hold

Please write a class named `CargoHold` with the following methods:

- A constructor which takes the maximum weight as an argument.
- A method named `add_suitcase` which adds the suitcase given as an argument to the cargo hold.
- A `__str__` method which returns a string in the format "x suitcases, space for y kg".

The class should make sure that the combined weight of the items stored within any `CargoHold` does not exceed the maximum weight set for that instance. If the maximum weight would be exceeded when the `add_suitcase` method is called, the new suitcase should not be added to the cargo hold.

**Test code:**

```python
cargo_hold = CargoHold(1000)
print(cargo_hold)

book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold.add_suitcase(adas_suitcase)
print(cargo_hold)

cargo_hold.add_suitcase(peters_suitcase)
print(cargo_hold)
```

**Sample output:**

```
0 suitcases, space for 1000 kg
1 suitcase, space for 997 kg
2 suitcases, space for 993 kg
```

### The contents of the cargo hold

Please add a method named `print_items` to your `CargoHold` class. It should print out all the items in all the suitcases within the cargo hold.

**Test code:**

```python
book = Item("ABC Book", 2)
phone = Item("Nokia 3210", 1)
brick = Item("Brick", 4)

adas_suitcase = Suitcase(10)
adas_suitcase.add_item(book)
adas_suitcase.add_item(phone)

peters_suitcase = Suitcase(10)
peters_suitcase.add_item(brick)

cargo_hold = CargoHold(1000)
cargo_hold.add_suitcase(adas_suitcase)
cargo_hold.add_suitcase(peters_suitcase)

print("The suitcases in the cargo hold contain the following items:")
