# Write your solution here
def first_word(sentence): 
    index = sentence.find(" ")
    return sentence[:index]

def second_word(sentence): 
    index = sentence.find(" ")
    sentence = sentence[index + 1:]
    #print("Print:", sentence)
    if sentence.find(" ") != -1: 
        index = sentence.find(" ")
        return sentence[:index]
    else:
        return sentence

def last_word(sentence):
    while sentence.find(" ") != -1:
        index = sentence.find(" ")
        sentence = sentence[index + 1:]
        
    return sentence

    #return first_word(first_word(sentence))

# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))