```python
def match(word: str, search_term: str) -> bool:
    if '*' in search_term:
        if search_term.startswith('*'):
            return word.endswith(search_term[1:])
        else:  # search_term.endswith('*')
            return word.startswith(search_term[:-1])
    else:
        if len(word) != len(search_term):
            return False
        return all(a == b or b == '.' for a, b in zip(word, search_term))

def find_words(search_term: str) -> list:
    results = []

    with open("words.txt", "r") as file:
        for line in file:
            word = line.strip()  # Remove newline characters
            if match(word, search_term):
                results.append(word)

    return results
```

```plaintext
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

### More StraightForward Solution
```python
def find_words(search_term: str):
    results = []
 
    with open("words.txt") as file:
        # Tätä tarvitaan myöhemmin
        hakusana_ilman_tahtea = search_term.replace("*","")
 
        for word in file:
            word = word.replace("\n","")
            # Is there an asterisk?
            if "*" in search_term:
                # start or end?
                if search_term[0] == "*":
                    if word.endswith(hakusana_ilman_tahtea):
                        results.append(word)
                else:
                    if word.startswith(hakusana_ilman_tahtea):
                        results.append(word)
            # Is there a dot?
            elif "." in search_term:
                # same length?
                if len(search_term) == len(word):
                    found = True
                    for i in range(len(search_term)):
                        if search_term[i] != "." and search_term[i] != word[i]:
                            found = False
                            break
                    if found:
                        results.append(word)
            # No special characters, only whole word matches count
            else:
                if word == search_term:
                    results.append(word)
    return results
```