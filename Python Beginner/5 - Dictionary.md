In a dictionary, items are indexed by `keys`, and each `key` maps to a `value`. 

```python
my_dictionary = {}          # creates empty dictionary

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

print(len(my_dictionary))
print(my_dictionary)
print(my_dictionary["apina"])
```

```
3
{'apina': 'monkey', 'banaani': 'banana', 'cembalo': 'harpsichord'}
monkey
```

#### Dictionary with User Input

```python
word = input("Please type in a word: ")
if word in my_dictionary:
    print("Translation: ", my_dictionary[word])
else:
    print("Word not found")
```

#### What can be stored in a dictionary?
- Looks to me like any data type. Here are a few examples

1. string -> int
```python
results = {}
results["Mary"] = 4
results["Alice"] = 5
results["Larry"] = 2
```

2. int -> `int[list]`
```python
lists = {}
lists[5] = [1, 2, 3]
lists[42] = [5, 4, 5, 4, 5]
lists[100] = [5, 2, 3]
```

#### Keys are unique 

If you use an existing key, the value mapped to that key is replaced with the new value. 

```python
my_dictionary["suuri"] = "big"
my_dictionary["suuri"] = "large"
print(my_dictionary["suuri"])
```

```
large
```


#### Keys must be immutable! 

This means that keys CANNOT be lists. 

```python
my_dictionary[[1, 2, 3]] = 5
```

```
TypeError: unhashable type: 'list'
```


#### Traversing a dictionary

Use `for item in collection` as we have been to traverse a dictionary.

```python
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key in my_dictionary:
    print("key:", key)
    print("value:", my_dictionary[key])
```

```
key: apina
value: monkey
key: banaani
value: banana
key: cembalo
value: harpsichord
```

A more pythonic way to achieve this is to use the `.items()` method. In this case, we're returning a view of an object that displays a list of dictionary key-value tupule pairs, which is unpacked into key and value. 
- This is more efficient and readable because unlike the `for item in collection`, we don't need to do a key lookup to access each value. 

```python
my_dictionary = {}

my_dictionary["apina"] = "monkey"
my_dictionary["banaani"] = "banana"
my_dictionary["cembalo"] = "harpsichord"

for key, value in my_dictionary.items():
    print("key:", key)
    print("value:", value)
```

```
key: apina
value: monkey
key: banaani
value: banana
key: cembalo
value: harpsichord
```

**As the keys are processed based on a hash value, the order should not usually matter in applications. In fact, in many older versions of Python the order is not guaranteed to follow the time of insertion.**


#### Some more advanced ways to use dictionaries

#### Count the number of times a word appears in a list
```python
def counts(my_list: list):
    this_dict = {} 

    for word in my_list:
        if word not in this_dict:     # if word (key) is not in dictionary, add it
            this_dict[word] = 0
        
        this_dict[word] += 1          # increment 
    
    return this_dict


word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

print(counts(word_list))
```

```
{'banana': 1, 'milk': 1, 'beer': 3, 'cheese': 2, 'sourmilk': 3, 'juice': 1, 'sausage': 2, 'tomato': 1, 'cucumber': 1, 'butter': 2, 'margarine': 1, 'chocolate': 1}
```

#### What if we wanted to categorize the words based on the initial letter in each word? One way to accomplish this would be to use dictionaries:

```python
def categorize_by_initial(my_list: list):
    this_dict = {} 

    for word in my_list: 
        initial = word[0]

        if initial not in this_dict:
            this_dict[initial] = []

        this_dict[initial].append(word)

    
    return this_dict



word_list = [
  "banana", "milk", "beer", "cheese", "sourmilk", "juice", "sausage",
  "tomato", "cucumber", "butter", "margarine", "cheese", "sausage",
  "beer", "sourmilk", "sourmilk", "butter", "beer", "chocolate"
]

#print(counts(word_list))

groups = categorize_by_initial(word_list)

for key, value in groups.items():
    print(f"words beginning with {key}:")
    
    for word in value:             # value here is a list 
        print(word)
```

```
words beginning with b:
banana
beer
butter
beer
butter
beer
words beginning with m:
milk
margarine
words beginning with c:
cheese
cucumber
cheese
chocolate
words beginning with s:
sourmilk
sausage
sausage
sourmilk
sourmilk
words beginning with j:
juice
words beginning with t:
tomato
```

#### Phone Book that can store multiple numbers for one name

```python
# Write your solution here
def search(my_dict : dict):
    name = input("name: ")
    if name in my_dict: 
        for item in my_dict[name]:  # prints out all values in a given key
            print(item)
    else:
        print("no number")    

def add(my_dict : dict): 
        name = input("name: ")
        number = input("number: ")
        # accomodate multiple numbers by storing list values 
        if name not in my_dict:
            my_dict[name] = []
    
        my_dict[name].append(number)
        print("ok!")

def main():
    my_dict = {}

    while True: 
        val = int(input("command (1 search, 2 add, 3 quit): "))
        if val == 1: 
            search(my_dict)
        elif val == 2: 
            add(my_dict)
        elif val == 3: 
            break

    print("quitting...")

main()
```


#### Removing keys and values from a dictionary (Two Methods)

1. **Method One** : `del`

```python
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["David"]
print(staff)
```

```
{'Alan': 'lecturer', 'Emily': 'professor'}
```

If you try and use `del` on a key that does not exisit in the dictionary, 

```python
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
del staff["Paul"]
```

```
>>> del staff["Paul"]
Traceback (most recent call last):
  File "", line 1, in 
KeyError: 'Paul'
```

**So, before deleting a key you should check if it is present in the dictionary:**

```python
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
if "Paul" in staff:
  del staff["Paul"]
  print("Deleted")
else:
  print("This person is not a staff member")
```

2. **Method Two:**  `pop()`
	Unlike `del`, `pop` returns the value removed from dictionary 

```python
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("David")
print(staff)
print(deleted, "deleted")
```

```
{'Alan': 'lecturer', 'Emily': 'professor'}
lecturer deleted
```

By default, pop will also cause an error if you try to delete a key which is not present in the dictionary. It is possible to avoid this by giving the method a second argument, which contains a default return value. This value is returned in case the key is not found in the dictionary. The special Python value `None` will work here:

```python
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
deleted = staff.pop("Paul", None)
if deleted == None:         ### return value is None == None
  print("This person is not a staff member")
else:
  print(deleted, "deleted")
```

```
This person is not a staff member
```

##### NB: if you need to delete the contents of the entire dictionary, and try to do it with a for loop, like so

```python
staff = {"Alan": "lecturer", "Emily": "professor", "David": "lecturer"}
for key in staff:
  del staff[key]
```

```
RuntimeError: dictionary changed size during iteration
```

**Why?**
When you iterate over a dictionary, Python creates an iterator that expects the dictionary to stay the same size. If you modify the dictionary's size (by adding or removing items), Python loses track of the size and raises an error.
	**When traversing a collection with a for loop, the contents may not change while the loop is in progress.**
	
Instead, use **`clear()`** 

```
staff.clear()
```

#### Invert a Dictionary 

So my original approach was as follows:

```python
    for key, value in dictionary.items():
        del dictionary[key]
        dictionary[value] = key
```

The above did not work because I was deleting (therefore, changing size) of the dictionary, while I used the iterator of the same structure I was deleting. 

To avoid this, the model code made a copy first. So the iterator is of the copy, which means we can freely change the dictionary. Recall that dictionaries, like lists, are referenced. 

```python
def invert(dictionary: dict):
	copy = {}
	for key in dictionary:        # copies the same dictionary 
		copy[key] = dictionary[key]
	for key in copy:              # iterator is copy, while delete key 
		del dictionary[key]
	for key in copy:              # invert key-value pair  
		dictionary[copy[key]] = key
```

My original approach: 
- I just stored both keys and values in seperate lists, and then deleted the dictionary using `clear()`
```python
def invert(dictionary: dict):
    list_key = []
    list_value = []
    for key, value in dictionary.items():
        list_key.append(key)
        list_value.append(value)

    dictionary.clear()

    for key, value in zip(list_key, list_value):
        dictionary[value] = key
```


# Movie Database - Structured Data 

The advantage of a dictionary is that it is a collection. It collects related data under one variable, so it is easy to access the different components. This same advantage is offered by a list. However, as a programmer, the index `[1], [2], etc` do not tell us anything about what is stored. When using a dictionary this problem is avoided, as each bit of data is accessed through a named key.

```python
person1 = {"name": "Pippa Python", "height": 154, "weight": 61, "age": 44}
person2 = {"name": "Peter Pythons", "height": 174, "weight": 103, "age": 31}
person3 = {"name": "Pedro Python", "height": 191, "weight": 71, "age": 14}

people = [person1, person2, person3]

for person in people:
    print(person["name"])

combined_height = 0
for person in people:
    combined_height += person["height"]

print("The average height is", combined_height / len(people))
```

```python
def add_movie(database: list, name: str, director: str, year: int, runtime: int):
    # a list of dictonaries? 
    movie = {
        "name": name, 
        "director": director, 
        "year": year, 
        "runtime": runtime
        }
    database.append(movie)

movie_database = []
```

### Search for a movie title, case-insensitive (since `in` is case-sensitive)
```python
# Write your solution here
def find_movies(database: list, search_term: str):
    movie_list = []
    for movie in database: # for each object 
        if search_term.lower() in movie["name"].lower():    # search for the specific term in this dictionary object...?
            movie_list.append(movie)
    return movie_list

if __name__ == "__main__":

    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
    {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
    {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)
```