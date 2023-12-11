# Write your solution here
def same_chars(word, index1, index2):
    if (len(word) <= index1) or (len(word) <= index2):
        return False

    if word[index1] == word[index2]:
        return True
    else:
        return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 10))


"""
def same_chars(str, a, b):
    if a >= len(str) or b >= len(str):
        return False
    return str[a] == str[b]
# Write your solution here
 """