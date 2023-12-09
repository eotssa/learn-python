# Lambda expressions

We have mostly worked with functions from the viewpoint of modularity. It is true that functions play an important role in managing the complexity of your programs and avoiding code repetition. Functions are usually written so that they can be used many times.

But sometimes you need something resembling a function that you will use just once. Lambda expressions allow you to create small, anonymous functions which are created (and discarded) as they are needed in the code. The general syntax is as follows:

```
lambda <parameters> : <expression>
```

Sorting a list of tuples by the second item in each tuple would look like this implemented with a lambda expression:

```python
products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

# Function is created "on the fly" with a lambda expression:
products.sort(key=lambda item: item[1])

for product in products:
    print(product)
```

**Sample output**
```
('apple', 3.95)
('orange', 4.5)
('watermelon', 4.95)
('banana', 5.95)
```

The expression

```
lambda item: item[1]
```

is equivalent to the function definition

```python
def price(item):
    return item[1]
```

except for the fact that a lambda function doesn't have a name. This is why lambda functions are called anonymous functions.

In every other respect a lambda function is no different from any other function, and they can be used in all the same contexts as any equivalent named function. For example, the following program sorts a list of strings alphabetically by the last character in each string:

```python
strings = ["Mickey", "Mack", "Marvin", "Minnie", "Merl"]

for word in sorted(strings, key=lambda word: word[-1]):
    print(word)
```

**Sample output**
```
Minnie
Mack
Merl
Marvin
Mickey
```

We can also combine list comprehensions, the join method and lambda expressions. For example, we could sort strings based on just the vowels in them, ignoring all other characters:

```python
strings = ["Mickey", "Mack", "Marvin", "Minnie", "Merl"]

for word in sorted(strings, key=lambda word: "".join([c for c in word if c in "aeiou"])):
    print(word)
```

**Sample output**
```
Mack
Marvin
Merl
Mickey
Minnie
```

Anonymous functions can also be used with other built in Python functions, not just those used for sorting. For example, the `min` and `max` functions also take a keyword argument named `key`. It is used as the criteria for comparing the items when selecting the minimum or maximum value.

In the following example we are dealing with audio recordings. First we select the oldest recording, and then the longest:

```python
class Recording:
    """ The class models a single audio recording """
    def __init__(self, name: str, performer: str, year: int, runtime: int):
        self.name = name
        self.performer = performer
        self.year = year
        self.runtime = runtime

    def __str__(self):
        return f"{self.name} ({self.performer}), {self.year}. {self.runtime} min."

if __name__ == "__main__":
    r1 = Recording("Nevermind", "Nirvana", 1991, 43)
    r2 = Recording("Let It Be", "Beatles", 1969, 35)
    r3 = Recording("Joshua Tree", "U2", 1986, 50)

    recordings = [r1, r2, r3]

    print("The oldest recording:")
    print(min(recordings, key=lambda rec: rec.year))

    print("The longest recording:")
    print(max(recordings, key=lambda rec: rec.runtime))
```

**Sample output**
```
The oldest recording:
Let It Be (Beatles), 1969. 35 min.
The longest recording:
U2 (Joshua Tree), 1986. 50 min.
```

---
### **Programming Exercise: BallPlayers**

**Task**:
The exercise template contains the definition for a class named `BallPlayer` with the following public attributes:

- `name`
- `shirt number`
- `scored goals`
- `assists completed`
- `minutes played`

You are to implement the following functions:

---

**1. Most goals**:

Write a function named `most_goals(players: list)`. 

**Input**: A list of `BallPlayer` objects.

**Output**: Return the name of the player who scored the most goals in string format.

---

**2. Most points**:

Write a function named `most_points(players: list)`.

**Input**: A list of `BallPlayer` objects.

**Output**: Return a tuple containing the name and shirt number of the player who has scored the most points. The total number of points is the number of goals and the number of assists combined.

---

**3. Least minutes**:

Write a function named `least_minutes(players: list)`.

**Input**: A list of `BallPlayer` objects.

**Output**: Return the `BallPlayer` object which has the smallest value of minutes played.

---

**Example**:

```python
player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)

team = [player1, player2, player3, player4, player5]
print(most_goals(team))
print(most_points(team))
print(least_minutes(team))
```

**Expected Output**:
```
Archie Bonkers
('Cruella De Hill', 9)
BallPlayer(name=Donald Quack, number=4, goals=3, assists=9, minutes=12)
```

---

**Your Solution**:

```python
# Place your solution here
class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here

# takes list of BallPlayer
def most_goals(players: list):
    # max is a sorting function, which sorts based on the key, and then returns the object, which is accessed for its name
    return max(players, key=lambda player : player.goals).name

#takes list of BallPlayer
def most_points(players: list):
   best = max(players, key=lambda player : player.number + player.passes)
   return (best.name, best.number)


def least_minutes(players: list):
    return min(players, key=lambda player : player.minutes)


if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team))
    print(most_points(team))
    print(least_minutes(team))
```