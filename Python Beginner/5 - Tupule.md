Tuple is a data structure which is, in many ways, similar to a list. The most important differences between the two are:

- Tuples are enclosed in parentheses (), while lists are enclosed in square brackets [].
- Tuples are immutable, while the contents of a list may change.

The following bit of code creates a tuple containing the coordinates of a point:

```python
point = (10, 20)
```

The items stored in a tuple are accessed by index, just like the items stored in a list:

```python
point = (10, 20)
print("x coordinate:", point[0])
print("y coordinate:", point[1])
```

Sample output:

```
x coordinate: 10
y coordinate: 20
```

The values stored in a tuple cannot be changed after the tuple has been defined. The following will not work:

```python
point = (10, 20)
point[0] = 15
```

Sample output:

```
TypeError: 'tuple' object does not support item assignment
```

#### Programming exercise: The oldest person

```python

#### Points:
#### 1
#### / 
#### 1

#### Problem:
Please write a function named `oldest_person(people: list)`, which takes a list of tuples as its argument.
In each tuple, the first element is the name of a person, and the second element is their year of birth.
The function should find the oldest person on the list and return their name.

An example of the function in action:

```python
p1 = ("Adam", 1977)
p2 = ("Ellen", 1985)
p3 = ("Mary", 1953)
p4 = ("Ernest", 1997)
people = [p1, p2, p3, p4]

print(oldest_person(people))
```

#### Solution:
```python
def oldest_person(people: list):
    oldest = people[0]  # stores the first tuple 

    for person in people: 
        if person[1] < oldest[1]: 
            oldest = person 
        
    return oldest[0]


if __name__ == "__main__":
    p1 = ("Adam", 1977)
    p2 = ("Ellen", 1985)
    p3 = ("Mary", 1953)
    p4 = ("Ernest", 1997)
    people = [p1, p2, p3, p4]

    print(oldest_person(people))
```

The problem requires you to write a function named `oldest_person` that takes a list of tuples as its argument. Each tuple contains the name of a person as the first element and their year of birth as the second element. The function should find the oldest person in the list and return their name.

In the provided example, four tuples representing people's names and birth years are created: `p1`, `p2`, `p3`, and `p4`. These tuples are then added to the `people` list. The `oldest_person` function is called with the `people` list as the argument, and the result is printed.

The `oldest_person` function starts by initializing the `oldest` variable with the first tuple from the `people` list. It then iterates over each tuple in the `people` list and compares the birth year of each person with the birth year of the oldest person found so far. If a person has a lower birth year, the `oldest` variable is updated with that person's tuple.

Finally, the function returns the name of the oldest person (`oldest[0]`).


# Purpose of a Tuple

Tuples serve a specific purpose in Python programming. They are particularly useful when dealing with a fixed set of values that are somehow related. For instance, when working with coordinates like x and y, tuples are a natural choice because coordinates always consist of two values.

## Example:
```python
point = (10, 20)
```

While it is technically possible to use a list to store coordinates, it is not ideal. Lists are collections of consecutive items that can change in size. When storing coordinates, it is preferable to have a specific structure that represents the x and y values directly, rather than an arbitrary list.

An important characteristic of tuples is that they are immutable, unlike lists. This immutability allows tuples to be used as keys in dictionaries. Consider the following example, where a dictionary is created with coordinate points as keys:

```python
points = {}
points[(3, 5)] = "monkey"
points[(5, 0)] = "banana"
points[(1, 2)] = "harpsichord"
print(points[(3, 5)])
```

Output:
```
monkey
```

If we attempt to use lists instead of tuples as keys in the dictionary, it would result in an error:

```python
points = {}
points[[3, 5]] = "monkey"  # This line would cause an error
points[[5, 0]] = "banana"  # This line would cause an error
points[[1, 2]] = "harpsichord"  # This line would cause an error
print(points[[3, 5]])  # This line would cause an error
```

Output:
```
TypeError: unhashable type: 'list'
```

This error occurs because lists are mutable objects, and mutable objects cannot be used as dictionary keys. Tuples, being immutable, can be hashed and used as keys effectively.

In summary, tuples are beneficial for representing fixed sets of related values and can be used as keys in dictionaries due to their immutability.


## Tuples without parentheses

The parentheses are not strictly necessary when defining tuples. The following two variable assignments are identical in their results:

```python
numbers = (1, 2, 3)
numbers = 1, 2, 3
```

This means we can also easily return multiple values using tuples. Let's have a look at the following example:

```python
def minmax(my_list):
  return min(my_list), max(my_list)

my_list = [33, 5, 21, 7, 88, 312, 5]

min_value, max_value = minmax(my_list)
print(f"The smallest item is {min_value} and the greatest item is {max_value}")
```

**Sample output:**
The smallest item is 5 and the greatest item is 312

This function returns two values in a tuple. The return value is assigned to two variables at once:

```python
min_value, max_value = minmax(my_list)
```

Using parentheses may make the notation more clear. On the left-hand side of the assignment statement, we also have a tuple, which contains two variable names. The values contained within the tuple returned by the function are assigned to these two variables.

```python
(min_value, max_value) = minmax(my_list)
```

You may remember the dictionary method `items` in the previous section. We used it to access all the keys and values stored in a dictionary:

```python
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)
```

Tuples are at work here, too. The method `my_dictionary.items()` returns each key-value pair as a tuple, where the first item is the key and the second item is the value.

Another common use case for tuples is swapping the values of two variables:

```python
number1, number2 = number2, number1
```

The assignment statement above swaps the values stored in the variables `number1` and `number2`. The result is identical to what is achieved with the following bit of code, using a helper variable:

```python
helper_var = number1
number1 = number2
number2 = helper_var
	```