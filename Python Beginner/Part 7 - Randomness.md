# Randomness

## Learning objectives

After this section, you will be able to:
- Understand and utilize the functions in the `random` module
- Generate random numbers in your programs
- Shuffle data structures using the `shuffle` function
- Pick random items from a data structure using the `choice` function
- Generate unique sets of random numbers

## Generating a random number

The `random` module in Python's standard library provides tools for generating random numbers and implementing other randomized functionality.

To generate a random integer value between `a` and `b` (inclusive), you can use the `randint(a, b)` function. For example:

```python
from random import randint

print("The result of the throw:", randint(1, 6))
```

Output:
```
The result of the throw: 4
```

You can also generate multiple random numbers by using a loop:

```python
from random import randint

for i in range(10):
    print("The result of the throw:", randint(1, 6))
```

## More randomizing functions

The `random` module provides other functions for randomizing data structures. The `shuffle` function shuffles a list in-place:

```python
from random import shuffle

words = ["atlas", "banana", "carrot"]
shuffle(words)
print(words)
```

Output:
```
['banana', 'atlas', 'carrot']
```

The `choice` function returns a randomly selected item from a data structure:
**The choice function from the random module picks a random element each time.**

```python
from random import choice

words = ["atlas", "banana", "carrot"]
print(choice(words))
```

Output:
```
'carrot'
```

## Lottery numbers

Generating lottery numbers involves selecting a set of unique random numbers within a specified range. Here are a few approaches to achieve this:

### Approach 1: List and loop

```python
from random import randint

weekly_draw = []
while len(weekly_draw) < 7:
    new_rnd = randint(1, 40)
    if new_rnd not in weekly_draw:
        weekly_draw.append(new_rnd)

print(weekly_draw)
```

### Approach 2: Shuffle and slice

```python
from random import shuffle

number_pool = list(range(1, 41))
shuffle(number_pool)
weekly_draw = number_pool[0:7]
print(weekly_draw)
```

### Approach 3: Sample function

```python
from random import sample

number_pool = list(range(1, 41))
weekly_draw = sample(number_pool, 7)
print(weekly_draw)
```

## True randomness

The `random` module in Python generates pseudorandom numbers, which are not truly random but rather based on an algorithm and a seed value. To ensure the same sequence of pseudorandom numbers, you can set the seed value using the `seed` function:

```python
from random import randint, seed

seed(1337)
print(randint(1, 100))  # Always produces the same "random" number
```

For true randomness, external sources such as background radiation or noise levels are used to generate the seed value.

## Programming exercise: Password generator

You can use the `random` module to create a password generator. Here's an example of generating passwords consisting of lowercase characters 'a' to 'z':

```python
from random import choice
from string import ascii_lowercase

def generate_password(length: int):
    password = ''
    for _ in range(length):
        password += choice(ascii_lowercase)
    return password

for _ in range(10):
    print(generate_password(8))
```

Output:
```
lttehepy
olsxttjl
cbjncrzo
dwxqjdgu
gpfdcecs
jabyvgar
xnbbonbl
ktmsjyww
ejhprmel
rjkoacib
```

The `choice` function is used to randomly select a character from the lowercase alphabet. The generated password length is specified as an argument to the `generate_password` function.

Remember, this is a simple example using only lowercase characters. You can extend it to include uppercase letters, digits, and special characters based on your requirements.

#### Code 

```python
from random import choice, shuffle
from string import ascii_lowercase, digits


def generate_strong_password(length: int, include_num: bool, include_special_chars: bool):
    
    spec_chrs = "!?=+-()#"
    pwd = [choice(ascii_lowercase)]  # ensures at least 1 char

    characters_pool = ascii_lowercase
    if include_num:
        pwd.append(choice(digits))  # ensures at least 1 digit if true
        characters_pool += digits

    if include_special_chars:
        pwd.append(choice(spec_chrs))  # ensures at least 1 special char if true
        characters_pool += spec_chrs

    while len(pwd) < length:
        pwd.append(choice(characters_pool))

    shuffle(pwd)
    
    return ''.join(pwd)

```