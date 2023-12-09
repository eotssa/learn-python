## Use of f strings to concatenate 

```python
limit = int(input("Limit: "))
number = 1
sum = 1
numbers = "1"
while sum < limit:
    number += 1
    sum += number
    # note that f-string can also be used like this
    numbers += f" + {number}"
print(f"The consecutive sum: {numbers} = {sum}")

```
```OUTPUT
The consecutive sum: 1 + 2 + 3 = 6
```

### Use of `a < b < c` is legal and has the intended mathematical effect in python. But why don't we use this?
- Consider other programming languages, C# does not have this feature. Best to avoid features that are not widely use...can be confusing

## Strings use the same indexing as perl. Negative indexing. 
-  You can think of input_string[-1] as shorthand for input_string[len(input_string) - 1].

## Searching for substrings
The in operator can tell us if a string contains a particular substring. The Boolean expression a in b is true, if b contains the substring a.

For example, this bit of code
```python
input_string = "test"

print("t" in input_string)
print("x" in input_string)
print("es" in input_string)
print("ets" in input_string)
prints out the following:
```
```
Sample output
True
False
True
False
```


## Instead, the Python string method `find` can be used for this purpose. It takes the substring searched for as an argument, and returns either the first index where it is found, or -1 if the substring is not found within the string.

The image below illustrates how it is used:
```
input_string = "test"

print(input_string.find("t"))
print(input_string.find("x"))
print(input_string.find("es"))
print(input_string.find("ets"))
```
```
Sample output
0
-1
1
-1
```

## Substrings and slices
A substring of a string is a sequence of characters that forms a part of the string. For example, the string example contains the substrings exam, amp and ple, among others. In Python programming, the process of selecting substrings is usually called slicing, and a substring is often referred to as a slice of the string. The two terms can often be used interchangeably.

If you know the beginning and end indexes of the slice you wish to extract, you can do so with the notation [a:b]. This means the slice begins at the index a and ends at the last character before index b - that is, including the first, but excluding the last. You can think of the indexes as separator lines drawn on the left side of the indexed character, as illustrated in the image below:

```python
input_string = "presumptious"

print(input_string[0:3])
print(input_string[4:10])

# if the beginning index is left out, it defaults to 0
print(input_string[:3])

# if the end index is left out, it defaults to the length of the string
print(input_string[4:])
```

```
pre
umptio
pre
umptious
```


### Type Hinting
```python
def print_many_times(message : str, times : int):
    while times > 0:
        print(message)
        times -= 1
```

```python 
def ask_for_name() -> str:
    name = input("Mikä on nimesi? ")
    return name
```


## Lists

### Adding items to a list

The `append` method adds items to the end of a list. It works like this:

```python
numbers = []
numbers.append(5)
numbers.append(10)
numbers.append(3)
print(numbers)
```
```
[5, 10, 3]

```


## Adding to a specific location

If you want to specify a location in the list where an item should be added, you can use the `insert` method. The method adds an item at the specified index. All the items already in the list with an index equal to or higher than the specified index are moved one index further "to the right". Here's an example:

```python
numbers = [1, 2, 3, 4]
numbers.insert(2, 10)
print(numbers)
```

```
# Program
numbers = [1, 2, 3, 4, 5, 6]
numbers.insert(0, 10)
print(numbers)
numbers.insert(2, 20)
print(numbers)

```

```
Sample output
[10, 1, 2, 3, 4, 5, 6]
[10, 1, 20, 2, 3, 4, 5, 6]
```


## Removing items from a list
There are two different approaches to removing an item from a list:

1. If the index of the item is known, you can use the method `pop`.
2. If the contents of the item are known, you can use the method `remove`.

So, the method `pop` takes the index of the item you want to remove as its argument. The following program removes items at indexes 2 and 3 from the list. Notice how the indexes of the remaining items change when one is removed.

```python
my_list = [1, 2, 3, 4, 5, 6]

my_list.pop(2)
print(my_list)
my_list.pop(3)
print(my_list)
```

**Sample output:**

```
[1, 2, 4, 5, 6]
[1, 2, 4, 6]
```

It's useful to remember that the method `pop` also returns the removed item:

```python
my_list = [4, 2, 7, 2, 5]

number = my_list.pop(2)
print(number)
print(my_list)
```

**Sample output:**

```
7
[4, 2, 2, 5]
```


## Remove 

The `remove` method, on the other hand, takes the value of the item to be removed as its argument. For example, consider this program:

```python
my_list = [1, 2, 3, 4, 5, 6]

my_list.remove(2)
print(my_list)
my_list.remove(5)
print(my_list)
```

The above code produces the following output:

```
[1, 3, 4, 5, 6]
[1, 3, 4, 6]
```

The `remove` method removes the **FIRST** occurrence of the value in the list, similar to how the string function `find` returns the index of the first occurrence of a substring. Here's another example:

```python
my_list = [1, 2, 1, 2]

my_list.remove(1)
print(my_list)
my_list.remove(1)
print(my_list)
```

The output of the above code is:

```
[2, 1, 2]
[2, 2]
```

# `in` vs `not in` 

### using `in` for `list`

If the specified item is not present in the list, the `remove` function will raise an error. Similar to working with strings, you can check for the presence of an item using the `in` operator. Here's an example:

```python
my_list = [1, 3, 4]

if 1 in my_list: ## returns true if word exist
    print("The list contains item 1")

if 2 in my_list:
    print("The list contains item 2")
```

The output of the above code is:

```
The list contains item 1
```


## Sorting Lists (`sort` vs `sorted`

To sort a list from smallest to greatest, you can use the `sort` method:

```python
my_list = [2, 5, 1, 2, 4]
my_list.sort()
print(my_list)
```

To create a new sorted copy of the list without modifying the original, you can use the `sorted` function:

```python
my_list = [2, 5, 1, 2, 4]
print(sorted(my_list))
```

Remember, `sort` modifies the original list, while `sorted` creates a new sorted list.

```python
original = [2, 5, 1, 2, 4]
in_order = sorted(original)
print(original)
print(in_order)
```

## Example of sort vs sorted issue
```python
# Write your solution here
def distinct_numbers(my_list : list):
    this_list = []
    for i in my_list:
        if i not in this_list: 
            this_list.append(i)

    #this_list.sort()  
    #return this_list.sort() ## doesn't work. Recall what sort() does. It doesn't return anything. 
    return sorted(this_list)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list))
```

### Use of in-range
```python
def list_sum(my_list1 : list, my_list2 : list):
    this_list = []
    for i in range(0, len(my_list1)): # recall that it doens't include 3
        result = my_list1[i] + my_list2[i]
        this_list.append(result)
    
    return this_list
```

## Add two lists with the same index, use `zip`

**zip function is used to iterate over two or more lists (and not only lists, but any iterables) in parallel.**
```python
# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)

```


# Print Statement Formatting

We have learned three methods for formatting the arguments in the `print` statement.

1. The first method is using the `+` operator for string concatenation:

```python
name = "Mark"
age = 37
print("Hi " + name + " your age is " + str(age) + " years")
```

2. The second method is separating the segments with commas:

```python
print("Hi", name, "your age is", age, "years")
```

3. To remove the automatically added spaces, you can use the `sep` keyword argument:

```python
print("Hi", name, "your age is", age, "years", sep="")
```

You can specify any string as the separator. For example, using `"\n"` as the separator will print each argument on a separate line:

```python
print("Hi", name, "your age is", age, "years", sep="\n")
```

You can also modify the end of the line using the `end` keyword argument. Setting `end=""` removes the newline character:

```python
print("Hi ", end="")
print("there!")
```

---
# `.f` modifier in formatted values

The third method to prepare strings is f-strings. The previous example with the name and the age would look like this formulated with f-strings:

```python
name = "Erkki"
age = 39
print(f"Hi {name} your age is {age} years")
```

The output is:

```
Hi Erkki your age is 39 years
```

Thus far, we have only used very simple f-strings, but they can be very versatile in formatting string-type content. One very common use case is setting the number of decimals that are printed out with a floating-point number. By default, the number is quite high:

```python
number = 1/3
print(f"The number is {number}")
```

The output is:

```
The number is 0.3333333333333333
```

The specific format we want the number to be displayed in can be set within the curly brackets of the variable expression. Let's add a colon character and a format specifier after the variable name:

```python
number = 1/3
print(f"The number is {number:.2f}")
```

The output is:

```
The number is 0.33
```

The format specifier `.2f` states that we want to display 2 decimals. The letter `f` at the end means that we want the variable to be displayed as a float, i.e., a floating-point number.

### White-Space Format

Here's another example, where we specify the amount of whitespace reserved for the variable in the printout. Both times the variable name is included in the resulting string, it has a space of 15 characters reserved. First, the names are justified to the left, and then they are justified to the right:

```python
names = ["Steve", "Jean", "Katherine", "Paul"]
for name in names:
    print(f"{name:15} centre {name:>15}")
```

**{name:15}: Here, :15 means that 15 spaces are reserved for the variable name. If the name is less than 15 characters, the extra spaces will be filled with whitespace. By default, the text is left-justified, meaning the extra spaces will be on the right side of the name.

**{name:>15}: This is similar to the previous one, but with an extra > character. The > means that the text should be right-justified. So if the name is less than 15 characters, the extra spaces will be on the left side of the name.**

The output is:

```
Steve           centre           Steve
Jean            centre            Jean
Katherine       centre       Katherine
Paul            centre            Paul
```

The uses of f-strings are not restricted to `print` commands. They can be assigned to variables and combined with other strings:

```python
name = "Larry"
age = 48
city = "Palo Alto"
greeting = f"Hi {name}, you are {age} years of age"
print(greeting + f", and you live in {city}")
```

The output is:

```
Hi Larry, you are 48 years of age, and you live in Palo Alto
```

You can think of an f-string as a sort of function that creates a normal string based on the "arguments" within the curly brackets.

----------------------------------------

#### Format int list to str list with 2 decimal places

```python
def formatted(my_list : list[float]) -> list[str]:
    str_list = []
    for num in my_list:
        str_list.append(f"{num:.2f}")

    return str_list
```


## More String and List


## Slicing Strings

You are already familiar with the `[]` syntax for accessing a part of a string:

```python
my_string = "exemplary"
print(my_string[3:7])
```

The output is:

```
mpla
```

## Slicing Lists

The same syntax works with lists. Lists can be sliced just like strings:

```python
my_list = [3, 4, 2, 4, 6, 1, 2, 4, 2]
print(my_list[3:7])
```

The output is:

```
[4, 6, 1, 2]
```

## Slicing with Step

In fact, the `[]` syntax works very similarly to the `range` function, which means we can also give it a step:

```python
my_string = "exemplary"
print(my_string[0:7:2])
my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(my_list[6:2:-1])
```

The output is:

```
eepa
[7, 6, 5, 4]
```

## Reverse a String (easy)

If we omit either of the indexes, the operator defaults to including everything. Among other things, this allows us to write a very short program to reverse a string:

```python
my_string = input("Please type in a string: ")
print(my_string[::-1])
```

Sample output:

```
Please type in a string: exemplary
yralpmexe
```


## Count Method

The `count` method counts the number of times the specified item or substring occurs in the target. The method works similarly with both strings and lists:

```python
my_string = "How much wood would a woodchuck chuck if a woodchuck could chuck wood"
print(my_string.count("ch"))

my_list = [1, 2, 3, 1, 4, 5, 1, 6]
print(my_list.count(1))
```

The output is:

```
5
3
```

The method will not count overlapping occurrences. For example, in the string "aaaa", the method counts only two occurrences of the substring "aa", even though there would actually be three if overlapping occurrences were allowed.

## Replace Method

### Basic Replacement

The `replace` method creates a new string where a specified substring is replaced with another string:

```python
my_string = "Hi there"
new_string = my_string.replace("Hi", "Hey")
print(new_string)
```

The output is:

```
Hey there
```

The method will replace all occurrences of the substring.

### Multiple Replacements

```python
sentence = "sheila sells seashells on the seashore"
print(sentence.replace("she", "SHE"))
```

The output is:

```
SHEila sells seaSHElls on the seashore
```

### Immutable Strings and Variable Assignment

When using the `replace` method, a typical mistake is forgetting that strings are immutable. If the old string is no longer needed, the new string can be assigned to the same variable:

```python
my_string = "Python is fun"

# Replaces the substring and stores the result in the same variable
my_string = my_string.replace("Python", "Java")
print(my_string)
```

The output is:

```
Java is fun
```

If the old string is not assigned to a new variable or the updated string is not stored, the original string remains unchanged.


----------------------------------------

## `in` Operator

The `in` operator is used to check if a value exists in a sequence, such as a string or a list. It returns `True` if the value is present and `False` otherwise.

### Example 1: Checking Membership in a String

```python
my_string = "Hello, World!"
print('l' in my_string)
print('z' in my_string)
```

The output is:

```
True
False
```

In the first example, `'l'` is present in the string, so `True` is returned. In the second example, `'z'` is not found in the string, so `False` is returned.

### Example 2: Checking Membership in a List

```python
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)
print(6 in my_list)
```

The output is:

```
True
False
```

In the first example, `3` is present in the list, so `True` is returned. In the second example, `6` is not found in the list, so `False` is returned.

## `not in` Operator

The `not in` operator is used to check if a value does not exist in a sequence. It returns `True` if the value is not present and `False` if it is.

### Example 1: Checking Non-Membership in a String

```python
my_string = "Hello, World!"
print('z' not in my_string)
print('o' not in my_string)
```

The output is:

```
True
False
```

In the first example, `'z'` is not found in the string, so `True` is returned. In the second example, `'o'` is present in the string, so `False` is returned.

### Example 2: Checking Non-Membership in a List

```python
my_list = [1, 2, 3, 4, 5]
print(6 not in my_list)
print(3 not in my_list)
```

The output is:

```
True
False
```

In the first example, `6` is not found in the list, so `True` is returned. In the second example, `3` is present in the list, so `False` is returned.

----------------------------------------

# `if` vs. `if not` 

## `if` variant
```python
def no_shouting(my_list : list[str]) -> list[str]: 
    pruned_list = []
    for word in my_list:
        if word.isupper():
            continue
        else:
            pruned_list.append(word)
    
    return pruned_list
```

## `if not` variant (concise) 

```python
def no_shouting(my_list: list):
    without_upper = []
 
    for string in my_list:
        if not string.isupper():
            without_upper.append(string)
 
    return without_upper
```