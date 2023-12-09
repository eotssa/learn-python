# startswith()


------------

In Python, `all()` is a built-in function that returns `True` if all items in an iterable are true. If not, it returns `False`.

In the context of the code:
```
```python
return all(a == b or b == '.' for a, b in zip(word, search_term))
```
```
It's checking for every pair of characters (a, b) from the `word` and the `search_term` respectively (paired using `zip`), and it checks if either the two characters are the same (a == b) or the character from `search_term` is a dot (b == '.').

- If for every pair of characters, either the characters are the same or the character in `search_term` is a dot, then `all()` will return `True`, indicating that the `word` matches the `search_term` considering the '.' wildcard.
- If for any pair, the characters are not the same and the character in `search_term` is not a dot, then `all()` will return `False`, indicating that the `word` does not match the `search_term`.

The `all()` function is essentially a shorthand for a loop that checks every pair of characters and returns `False` as soon as it finds a pair that does not meet the criteria. If it checks all the pairs and they all meet the criteria, it returns `True`.
```


## CSV Reader 
```python
    # stores student start time 
    with open("start_times.csv") as file_one:
            students_start_time = {}
            # this line separates elements into a list based on the delimiter 
            for line in csv.reader(file_one, delimiter=";"):
                students_start_time[line[0]] = datetime.strptime(line[1], "%H:%M")
```