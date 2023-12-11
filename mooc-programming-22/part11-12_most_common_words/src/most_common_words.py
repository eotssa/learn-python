from string import punctuation

def most_common_words(filename: str, lower_limit: int):
    with open(filename, 'r') as file:
        content = file.read()

        content = content.replace("\n", " ") # remove all new-line char
        
        # removes all punctuation in the text
        for symbol in punctuation: 
            content = content.replace(symbol, "")

        words = content.split(" ")
        return {word: words.count(word) for word in words if words.count(word) >= lower_limit}
        




if __name__ == "__main__":
    # Creating the sample file with the provided content
    filename = r"C:\Users\Wilson\AppData\Local\tmc\vscode\mooc-programming-22\part11-12_most_common_words\src\comprehensions.txt"

    # Testing the function with the sample file and limit 3
    most_common_words_result = most_common_words(filename, 3)
    print(most_common_words_result)
