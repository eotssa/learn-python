# Write your solution here
def palindromes(str1 : str):
    i = len(str1) - 1
    for character in str1:
        if character == str1[i]:
            i -= 1
        else:
            return False
    
    return True

while True:
    input_str = input()
    
    if palindromes(input_str):
        print(f"{input_str} is a palindrome!")
        break
    else:
        print("that wasn't a palindrome")
