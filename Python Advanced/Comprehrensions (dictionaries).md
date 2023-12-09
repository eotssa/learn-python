### Comprehensions and dictionaries

There is nothing intrinsically "listey" about comprehensions. The result is a list because the comprehension statement is encased in square brackets, which indicate a Python list. Comprehensions work just as well with Python dictionaries if you use curly brackets instead. Remember, though, that dictionaries require key-value pairs. Both must be specified when a dictionary is created, also with comprehensions.

The basis of a comprehension can be any iterable series, be it a list, a string, a tuple, a dictionary, any of your own iterable classes, and so forth.

In the following example we use a string as the basis of a dictionary. The dictionary contains all the unique characters in the string, along with the number of times they occurred:

```python
sentence = "hello there"

char_counts = {character : sentence.count(character) for character in sentence}
print(char_counts)
```

**Sample output**

```plaintext
{'h': 2, 'e': 3, 'l': 2, 'o': 1, ' ': 1, 't': 1, 'r': 1}
```

The principle of the comprehension statement is exactly the same as with lists, but instead of a single value, the expression now consists of a key and a value. The general syntax looks like this:

```plaintext
{<key expression> : <value expression> for <item> in <series>}
```

To finish off this section, lets take a look at factorials again. This time we store the results in a dictionary. The number itself is the key, while the value is the result of the factorial from our function:

```python
def factorial(n: int):
    """ The function calculates the factorial n! for integers above zero """
    k = 1
    while n >= 2:
        k *= n
        n -= 1
    return k

if __name__ == "__main__":
    numbers = [-2, 3, 2, 1, 4, -10, 5, 1, 6]
    factorials = {number : factorial(number) for number in numbers if number > 0}
    print(factorials)
```

**Sample output**

```plaintext
{3: 6, 2: 2, 1: 1, 4: 24, 5: 120, 6: 720}
```


### Programming exercise: Lengths of strings

**Points:**
1 / 1

Please write a function named `lengths(strings: list)` which takes a list of strings as its argument. The function should return a dictionary with the strings in the list as the keys and their lengths as the values.

The function should be implemented with a dictionary comprehension. The maximum length of the function is two lines of code, including the header line beginning with the `def` keyword.

The function should work as follows:

```python
word_list = ["once", "upon", "a", "time", "in"]

word_lengths = lengths(word_list)
print(word_lengths)
```

**Sample output**

```plaintext
{'once': 4, 'upon': 4, 'a': 1, 'time': 4, 'in': 2}
```

---

```python
# WRITE YOUR SOLUTION HERE:
def lengths(strings: list):
    return {string : len(string) for string in strings}

if __name__ == "__main__":
    word_list = ["once", "upon" , "a", "time", "in"]

    word_lengths = lengths(word_list)
    print(word_lengths)
```