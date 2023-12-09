
# .join() 

`.join()` is a string method in Python which concatenates (or "joins") all the elements of an iterable (like a list or a tuple) into a string. The string on which this method is called is used as a separator between the elements.

Here's an example:

```python
separator = ', '
words = ['apple', 'banana', 'cherry']
result = separator.join(words)
```

In this example, `result` will be `'apple, banana, cherry'`. The `', '` string is used to join the words in the `words` list.

Let's look at a few more examples:

1. **Joining a list of strings with no separator**:

```python
"".join(["H", "e", "l", "l", "o"])
```

This will result in the string `'Hello'`.

2. **Joining a list of numbers**:

```python
", ".join([str(num) for num in [1, 2, 3, 4, 5]])
```

This will result in the string `'1, 2, 3, 4, 5'`. Note that we had to convert the numbers to strings first, because `.join()` only works on iterables of strings.

3. **Joining a tuple of strings with a separator**:

```python
" - ".join(("apple", "banana", "cherry"))
```

This will result in the string `'apple - banana - cherry'`.

Let's execute these examples in Python to see the results.
```
# Example 1: Joining a list of strings with no separator
result_1 = "".join(["H", "e", "l", "l", "o"])

# Example 2: Joining a list of numbers
result_2 = ", ".join([str(num) for num in [1, 2, 3, 4, 5]])

# Example 3: Joining a tuple of strings with a separator
result_3 = " - ".join(("apple", "banana", "cherry"))

result_1, result_2, result_3
```
```OUTPUT
('Hello', '1, 2, 3, 4, 5', 'apple - banana - cherry')

```

Here are the results from our examples:

1. Joining a list of strings with no separator: `'Hello'`
2. Joining a list of numbers: `'1, 2, 3, 4, 5'`
3. Joining a tuple of strings with a separator: `'apple - banana - cherry'`

As you can see, the `.join()` method is quite versatile and can be used in various scenarios to combine elements of an iterable into a single string.