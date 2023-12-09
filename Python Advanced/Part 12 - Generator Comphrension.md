# Generator comprehensions

You do not necessarily need a function definition to create a generator. We can use a structure similar to a list comprehension instead. This time we use round brackets to signify a generator instead of a list or a dictionary:

```python
# This generator returns squares of integers
squares = (x ** 2 for x in range(1, 64))

print(squares) # the printout of a generator object isn't too informative

for i in range(5):
    print(next(squares))
```

**Sample output**
```
<generator object <genexpr> at 0x000002B4224EBFC0>
1
4
9
16
25
```

In the following example we print out substrings of the English alphabet, each three characters long. This prints out the first 10 items in the generator:

```python
substrings = ("abcdefghijklmnopqrstuvwxyz"[i : i + 3] for i in range(24))

# print out first 10 substrings
for i in range(10):
    print(next(substrings))
```

**Sample output**
```
abc
bcd
cde
def
efg
fgh
ghi
hij
ijk
jkl
```

---

### **Programming Exercise: Random Words**

**Task**:
Write a function named `word_generator(characters: str, length: int, amount: int)` that generates random words based on the parameters provided.

**Input**:
- A string named `characters` containing the set of characters to choose from.
- An integer `length` which indicates the length of each random word to generate.
- An integer `amount` that indicates the number of words to generate.

**Output**: 
The function should return a generator that yields random words based on the given criteria.

---

**Example**:

```python
wordgen = word_generator("abcdefg", 3, 5)
for word in wordgen:
    print(word)
```

**Sample Output**:
(Note: Since it's random, the output will vary. This is just a potential output.)
```
dbf
baf
ead
fga
ccc
```

---

**Your Solution**:

```python
import random

def word_generator(characters: str, length: int, amount: int):
    for _ in range(amount):
        yield ''.join(random.choice(characters) for _ in range(length))
```

```python
# Write your solution here:
from random import choice

# inner and outer generator 
def word_generator(characters: str, length: int, amount: int):
    return ("".join(choice(characters) for _ in range(length)) for _ in range(amount))


if __name__ == "__main__":

    wordgen = word_generator("abcdefg", 3, 5)
    for word in wordgen:
        print(word)
```