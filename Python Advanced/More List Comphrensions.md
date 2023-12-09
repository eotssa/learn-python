Certainly! Here's the content formatted in Markdown, with the exercises moved to the end and linked back to their respective sections using Obsidian backlinking.

---

### String Manipulation in Python

Let's explore how we can manipulate strings in Python.

#### Uppercasing Name

```python
name = "Peter Python"

uppercased = [character.upper() for character in name]
print(uppercased)
```

**Sample output**

```plaintext
['P', 'E', 'T', 'E', 'R', ' ', 'P', 'Y', 'T', 'H', 'O', 'N']
```

The result is indeed a list, as dictated by the bracket notation around the comprehension statement. If we wanted a string instead, we could use the string method join to parse the list into a string. Remember, the method is called on the string we want to use as the "glue" between the characters. Let's take a look at some examples.

#### Using `join` Method

```python
name = "Peter"
char_list = list(name)
print(char_list)

print("".join(char_list))
print(" ".join(char_list))
print(",".join(char_list))
print(" and ".join(char_list))
```

**Sample output**

```plaintext
['P', 'e', 't', 'e', 'r']
Peter
P e t e r
P,e,t,e,r
P and e and t and e and r
```

#### Working with Vowels

You can use list comprehensions and the `join` method to create new strings based on other strings. See an example below:

```python
test_string = "Hello there, this is a test!"

vowels = [character for character in test_string if character in "aeiou"]
new_string = "".join(vowels)

print(new_string)
```

**Sample output**

```plaintext
eoeeiiae
```

This can also be done in a single line as follows:

```python
test_string = "Hello there, this is a test!"

vowel_string = "".join([character for character in test_string if character in "aeiou"])

print(vowel_string)
```

#### Sentence Processing

You can process entire sentences efficiently with a single statement. Here's an example:

```python
sentence = "Sheila keeps on selling seashells on the seashore"

sentence_no_initials = " ".join([word[1:] for word in sentence.split()])
print(sentence_no_initials)
```

**Sample output**

```plaintext
heila eeps n elling eashells n he eashore
```

The code above can be understood in the following steps:

1. `word[1:]` extracts a substring from the second character (at index 1) onwards.
2. `sentence.split()` splits the sentence into sections at the given character. In this case, there is no argument given to the method, so the sentence is split at space characters by default.
3. `" ".join()` combines the items in the list into a new string using a space character between the items.

A more traditional iterative approach could look like this:

```python
sentence = "Sheila keeps on selling seashells on the seashore"

word_list = []
words = sentence.split()
for word in words:
    word_no_initials = word[1:]
    word_list.append(word_no_initials)

sentence_no_initials = " ".join(word_list)

print(sentence_no_initials)
```

### Exercise: Filter forbidden [[#Exercise-1]]

### Working with Custom Classes

#### Using Comprehensions with Custom Classes

Comprehensions can be a useful tool for processing or formulating instances of your own classes, as we'll see in the following examples.

Here's an example with a `Country` class:

```python
class Country:
    """ This class models a single country with population """
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

if __name__ == "__main__":
    finland = Country("Finland", 6000000)
    malta = Country("Malta", 500000)
    sweden = Country("Sweden", 10000000)
    iceland = Country("Iceland", 350000)

    countries = [finland, malta, sweden, iceland]

    bigger_countries = [country.name for country in countries if country.population > 5000000]
    for country in bigger_countries:
        print(country)
```

**Sample output**

```plaintext
Finland
Sweden
```

#### Creating a List of Running Events

Another example using a `RunningEvent` class:

```python
class RunningEvent:
    """ The class models a foot race event of a length of n metres  """
    def __init__(self, length: int, name: str = "no name"):
        self.length = length
        self.name = name

    def __repr__(self):
        return f"{self.length} m. ({self.name})"

if __name__ == "__main__":
    lengths
    ```