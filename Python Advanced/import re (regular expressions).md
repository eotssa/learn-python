## **Regular Expressions**

Regular expressions (often abbreviated as regex) are a powerful tool for pattern matching in strings. They're like a mini-programming language for string manipulation and are used across many programming languages.

- **Basics**: 
  - They have a specific syntax to define patterns in strings.
  - Use the `re` module in Python for regex operations.

- **Key Functions**:
  - `re.search()`: Search for a pattern in a string.
  - `re.findall()`: Return all matches of a pattern in a string.

- **Syntax Highlights**:
  - **`|`**: Matches either side of the pipe, e.g., `aa|ee` matches strings with "aa" or "ee".
  - **`[...]`**: Matches any one of the characters inside the brackets, e.g., `[aeio]` matches any vowel.
  - **`-`**: Specifies a range, e.g., `[0-6]` matches any digit from 0 to 6.
  - **`*`**: Matches the preceding character 0 or more times.
  - **`+`**: Matches the preceding character 1 or more times.
  - **`.`**: Matches any single character.
  - **`^`**: Specifies start of a string.
  - **`$`**: Specifies end of a string.
  - **`\`**: Escapes special characters, e.g., `1\+` matches the string "1+".
  - **`(...)`**: Groups patterns, e.g., `(ab)+` matches one or more occurrences of "ab".

- **Usage Examples**:
  - To find words starting with "P" and ending with "on": `^P.*on$`.
  - To find numbers in a string: `\d+`.
  - To match only strings with numbers 1, 2, or 3: `^[123]*$`.

---

Of course! Let's summarize the content with included coding examples:

---

## **Regular Expressions in Python**

### **Examples**
1. **Matching words starting with "P" and ending with "on"**:
   ```python
   words = ["Python", "Pantone", "Pontoon", "Pollute", "Pantheon"]
   for word in words:
       if re.search("^P.*on$", word):
           print(word, "found!")
   ```
   Output: Python, Pontoon, Pantheon

2. **Finding numbers in a string**:
   ```python
   sentence = "First, 2 !#third 44 five 678xyz962"
   numbers = re.findall("\d+", sentence)
   for number in numbers:
       print(number)
   ```
   Output: 2, 44, 678, 962

### **Syntax Guide**
- **`|`**: Matches either side (e.g., `aa|ee` matches "aa" or "ee").
- **`[...]`**: Matches any character inside (e.g., `[aeio]` matches any vowel).
- **`-`**: Specifies a range (e.g., `[0-6]` matches any digit from 0 to 6).
- **`*`**: 0 or more times (e.g., `ba+b` matches "bab", "baab", etc.).
- **`+`**: 1 or more times.
- **`.`**: Matches any single character.
- **`^` and `$`**: Start and end of a string, respectively.
- **`\`**: Escapes special characters.
- **`(...)`**: Groups patterns.

### **Advanced Examples**
1. **Matching strings with only numbers 1, 2, or 3**:
   ```python
   expression = "^[123]*$"
   input_string = "1221"
   if re.search(expression, input_string):
       print("Found!")
   else:
       print("Not found.")
   ```
   Output: Found!

2. **Matching "jabba" followed by any characters and ending with "hut"**:
   ```python
   expression = "^(jabba).*(hut)$"
   input_string = "jabba the hut"
   if re.search(expression, input_string):
       print("Found!")
   ```



### **Programming Exercise: Regular expressions**

**Introduction:**
In this exercise, you will be familiarizing yourself with regular expression syntax.

---

**1. Days of the week:**

Implement a function named `is_dotw`:

```python
def is_dotw(my_string: str) -> bool:
    pass
```

- **Input:** A string `my_string`.
- **Output:** Return `True` if the string passed as an argument contains an abbreviation for a day of the week (Mon, Tue, Wed, Thu, Fri, Sat, Sun), otherwise return `False`.

**Sample Usage:**
```python
print(is_dotw("Mon"))  # Expected Output: True
print(is_dotw("Fri"))  # Expected Output: True
print(is_dotw("Tui"))  # Expected Output: False
```

---

**2. Check for vowels:**

Implement a function named `all_vowels`:

```python
def all_vowels(my_string: str) -> bool:
    pass
```

- **Input:** A string `my_string`.
- **Output:** Return `True` if all characters in the given string are vowels, otherwise return `False`.

**Sample Usage:**
```python
print(all_vowels("eioueioieoieou"))  # Expected Output: True
print(all_vowels("autoooo"))         # Expected Output: False
```

---

**3. Time of day:**

Implement a function named `time_of_day`:

```python
def time_of_day(my_string: str) -> bool:
    pass
```

- **Input:** A string `my_string`.
- **Output:** Return `True` if the string is in the format XX:YY:ZZ and is a valid time in the 24-hour format, with two digits each for hours, minutes, and seconds, otherwise return `False`.

**Sample Usage:**
```python
print(time_of_day("12:43:01"))  # Expected Output: True
print(time_of_day("AB:01:CD"))  # Expected Output: False
print(time_of_day("17:59:59"))  # Expected Output: True
print(time_of_day("33:66:77"))  # Expected Output: False
```

---

**Solution Space:**
```python
# Add your solutions here
import re

def is_dotw(my_string: str):
    if re.search("(Mon)|(Tue)|(Wed)|(Thu)|(Fri)|(Sat)|(Sun)", my_string):
        return True
    return False


def all_vowels(my_string: str):
    if len(re.findall("[aeiou]", my_string)) == len(my_string):
        return True
    return False

def time_of_day(my_string: str):
    if re.search("^([01]?[0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string):
        return True
    return False

```

```python
#model Solution
def is_dotw(my_string: str):
    return re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string) is not None
 
def all_vowels(my_string: str):
    return re.search("^[aeiou]*$", my_string) is not None
 
def time_of_day(my_string: str):
    return re.search("^([01][0-9]|2[0-3]):[0-5][0-9]:[0-5][0-9]$", my_string) is not None
 
```