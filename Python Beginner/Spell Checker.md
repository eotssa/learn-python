```python
my_input = input()
input_list = my_input.split(' ')

lst = [] 
with open("wordlist.txt") as new_file:
    for line in new_file:
        lst.append(line.strip())


new_sentence = ""
for i in range(0, len(input_list)):
    if input_list[i].lower() in lst:
        new_sentence += f"{input_list[i]} " 
    else: 
        new_sentence += f"*{input_list[i]}* "


print(new_sentence)


"""model solution
I like the pythonic 

"for word in sentence.split(' '):" since split will return a list of words that is iterable 
"""```