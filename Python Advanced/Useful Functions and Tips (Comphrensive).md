# # Multiline Strings with Triple Quotes
```markdown
# Multiline Strings with Triple Quotes

While you can use the `\n` escape character to put a newline into a string, it is often easier to use multiline strings. A multiline string in Python begins and ends with either three single quotes or three double quotes. Any quotes, tabs, or newlines in between the "triple quotes" are considered part of the string. Python’s indentation rules for blocks do not apply to lines inside a multiline string.

Open the file editor and write the following:

```python
print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob''')
```

Save this program as `catnapping.py` and run it. The output will look like this:

```
Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
```

Notice that the single quote character in Eve's does not need to be escaped. Escaping single and double quotes is optional in raw strings. The following `print()` call would print identical text but doesn’t use a multiline string:

```python
print('Dear Alice,\n\nEve\'s cat has been arrested for catnapping, cat burglary, and extortion.\n\nSincerely,\nBob')
```


# Use join() to create strings from lists
```python 
genres = ["comedy", "action"]
genre_string = ", ".join(self.genres)
```

# `key=` functionality 

The `key` parameter in functions like `min`, `max`, `sorted`, and others is used to specify a custom function that determines how the elements in the collection are compared.

When you pass a function to the `key` parameter, that function is applied to each element in the collection, and the results are used for comparison.

Here's a more detailed breakdown:

### Syntax

The `key` parameter takes a function that accepts a single argument and returns a value:

```python
key=function
```

### How It Works

1. **Applying the Key Function**: The function provided to the `key` parameter is applied to each element in the collection.
2. **Comparison**: The results of the key function are used for comparison instead of the elements themselves.
3. **Result**: The element that corresponds to the minimum (or maximum, or sorted order) of the key function's results is returned.

### Examples

#### Example 1: Finding the Shortest String

Suppose you want to find the shortest string in a list of strings. You can use the `len` function as the key function:

```python
words = ["apple", "banana", "cherry"]
shortest_word = min(words, key=len)
print(shortest_word) # Output: apple
```

Here, the `len` function is applied to each word, so the comparison is based on the lengths of the strings.

#### Example 2: Finding the Person with the Smallest Height

In the context of your previous code snippet:

```python
shortest_person = min(self.persons, key=lambda person: person.height)
```

Here, the lambda function `lambda person: person.height` is applied to each `Person` object in `self.persons`. It returns the height of each person, and the `min` function compares these heights to find the person with the smallest height.

### Summary

The `key` parameter is a powerful tool that allows you to customize how elements are compared in functions like `min`, `max`, and `sorted`. By passing a function to the `key` parameter, you can control how the comparison is performed based on the attributes or computed values of the elements, rather than the elements themselves.

# Lambda Functions
- It's like functional programming like I've done in ML. 

Lambda functions, also known as anonymous functions or lambda expressions, are a powerful feature in Python. They provide a concise way to define simple functions. Here's a detailed explanation:

### Lambda Functions

A lambda function is a small anonymous function. It can have any number of arguments but can only have one expression. The expression is evaluated and returned.

#### Syntax

The syntax of a lambda function is as follows:

```python
lambda arguments: expression
```

#### Example 1: Adding Two Numbers

Here's a simple example of a lambda function that takes two arguments and returns their sum:

```python
add = lambda x, y: x + y
print(add(5, 3)) # Output: 8
```

This is equivalent to defining the following named function:

```python
def add(x, y):
    return x + y
```

#### Example 2: Sorting a List of Tuples

You can use lambda functions as a key argument in sorting. Suppose you have a list of tuples representing people's names and ages, and you want to sort them by age. You can use a lambda function to do that:

```python
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
people.sort(key=lambda person: person[1])
print(people) # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]
```

In this example, the lambda function takes a tuple (representing a person) and returns the second element (the age), which is used as the sorting key.

### Advantages of Lambda Functions

1. **Conciseness**: Lambda functions are often more concise than named functions for simple operations.
2. **Inline Definition**: They can be defined right where you need them, such as inside a call to a higher-order function like `map` or `filter`.
3. **No Need for a Name**: Since they are anonymous, you don't have to think of a name for a function that you will only use in one place.

### When to Use Lambda Functions

Lambda functions are best used for small, simple functions that are passed to higher-order functions or used for one-off calculations. If you find that a lambda function is becoming complex or you need to reuse it, it's often better to define a named function instead.

### Summary

Lambda functions are a compact way to define simple functions on the fly. They can be particularly useful for operations like sorting or mapping where you need a small function for a single operation. While they can make code more concise, overuse or misuse of lambda functions can lead to less readable code, so it's wise to use them judiciously.


# An Example Encountered with Lambda (`shortest()`)

This is the snippet of code I wrote because I wanted to use list comprehensions. It wasn't particularly concise. 
```python
    def shortest(self):
        if self.is_empty():
            return None

        # returns a smallest integer number 
        shortest_height = min([person.height for person in self.persons])
        # uses integer number to return a string 
        shorest_person = [person for person in self.persons if person.height == shortest_height]
        return shorest_person[0]
```

#### Lambda Functionality 
```python
	def shortest(self):
		if self.is_empty()):
			return None
			
	shortest_person = min(self.persons, key=lambda person: person.height)
	return shortest_person
```


```python
shortest_person = min(self.persons, key=lambda person: person.height)
```

### Step-by-Step Breakdown

1. **Access `self.persons`**: The method accesses `self.persons`, which is a list of `Person` objects in the room. This list contains all the persons that have been added to the room.

2. **Call `min` Function**: The `min` function is called with two arguments:
   - The first argument is `self.persons`, the list of `Person` objects.
   - The second argument is a lambda function provided as the `key` parameter.

3. **Start Iterating Through `self.persons`**: The `min` function starts iterating through each `Person` object in `self.persons`.

4. **Apply Lambda Function to Each Person**:
   - For each `Person` object, the lambda function `lambda person: person.height` is called.
   - The lambda function takes a `Person` object as its argument and returns the value of that person's height attribute.

5. **Compare Heights**:
   - The `min` function compares the heights returned by the lambda function for each person.
   - It keeps track of the `Person` object with the smallest height encountered so far.
   - The comparison continues until all persons have been examined.

6. **Return the Shortest Person**:
   - After iterating through all the persons and applying the lambda function to each one, the `min` function identifies the `Person` object with the smallest height.
   - This `Person` object is returned by the `min` function.

7. **Assign to `shortest_person`**: The `Person` object with the smallest height is assigned to the variable `shortest_person`.


### The Model Way To Solve `shortest()`

```python
    def shortest(self):
        shortest_person = None
        height_of_shortest = 0
        for person in self.persons:
	        # first if statement stores the first person. 
            if shortest_person is None or person.height < height_of_shortest:
                shortest_person = person
                height_of_shortest = person.height
 
        return shortest_person
```


# `from collections import Counter` and `generator expressions`

Sure, let's break down the process using an example list: `my_list = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 8, 8, 9]`.

**Step 1:** Import the `Counter` class from the `collections` module.

```python
from collections import Counter
```

**Step 2:** Create a `Counter` object from `my_list`. This will create a dictionary-like object where the keys are the unique elements in `my_list` and the values are their corresponding counts.

```python
counter = Counter(my_list)
```

If you print `counter`, you'll see: `Counter({2: 2, 3: 2, 6: 2, 8: 2, 1: 1, 4: 1, 5: 1, 7: 1, 9: 1})`.

**Step 3:** Use a generator expression to count the number of elements that occur at least twice.

```python
doubles = sum(1 for count in counter.values() if count >= 2)
```

Here's what's happening in this line:

- `counter.values()` gives you a view of all the counts in the `counter` object: `[2, 2, 2, 2, 1, 1, 1, 1, 1]`.
- The generator expression `(1 for count in counter.values() if count >= 2)` generates a sequence of 1s for each count that is 2 or more: `1, 1, 1, 1`.
- `sum()` adds up these 1s to give you the total number of elements that occur at least twice: `4`.

**Step 4:** Return the result.

```python
return doubles
```

Here's the complete code for the `doubles` method:

```python
from collections import Counter

class ListHelper:
    @classmethod
    def doubles(cls, my_list: list):
        counter = Counter(my_list)
        return sum(1 for count in counter.values() if count >= 2)
```


# One line Conditions (Part 7)
```python
   def __str__(self):
        # Use the one-line condition introduced at the end of part 7
        end_s = "s" if len(self.__items) != 1 else ""
 
        return f"{len(self.__items)} item{end_s} ({self.weight()} kg)"
```

# ANY() for comphrensions 
- prevents me from having t
```python
    def status_of_programmer(self, programmer: str) -> tuple:
        if any(order.programmer == programmer for order in self._all_orders): 
            task_done = sum([1 for order in self._all_orders if order.programmer == programmer and order.is_finished() == True])
            task_undone = sum([1 for order in self._all_orders if order.programmer == programmer and order.is_finished() == False])

            num_done_hours = sum([order.workload for order in self._all_orders if order.programmer == programmer and order.is_finished() == True])
            num_undone_hours = sum([order.workload for order in self._all_orders if order.programmer == programmer and order.is_finished() == False])
    
            return (task_done, task_undone, num_done_hours, num_undone_hours)
        
        raise ValueError("STATUS OF PROGRAMMER ERROR")

```