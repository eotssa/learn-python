# Write your solution here
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
