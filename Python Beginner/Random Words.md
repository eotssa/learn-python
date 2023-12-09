```
Programming exercise:
Random words
Points:
1

/

1

The exercise template contains the file words.txt, which contains some English language words, one on each line.

Please write a function named words(n: int, beginning: str), which returns a list containing n random words from the words.txt file. All words should begin with the string specified by the second argument.

The same word should not appear twice in the list. If there are not enough words beginning with the specified string, the function should raise a ValueError exception.

An example of the function in action:

word_list = words(3, "ca")
for word in word_list:
    print(word)
Sample output
cat
car
carbon
```

```python
from random import sample

def words(n: int, beginning: str):
    words = []
    with open(r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part07-08_random_words\src\words.txt", "r") as file:
        for word in file:
            words.append(word.strip())

    match_words = []
    for word in words:
        check_begin = word[:len(beginning)]
        #print(check_begin)
        if beginning == check_begin:
            match_words.append(word)
    

    if len(match_words) < n:
        raise ValueError("Not enough matches")

    return sample(match_words, n)

```


## using beginswith()

```python
import random
 
def words(n: int, beginning: str):
    word_list = []
    with open("words.txt") as file:
        for word in file:
            word = word.replace("\n","")
            if word.startswith(beginning):
                word_list.append(word)
    if len(word_list) < n:
        raise ValueError("Not enough suitable words can be found!")
    return random.sample(word_list, n)
```
