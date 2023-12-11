# Write your solution here
def read_input(sentence, lower, upper):

    while True:
        try:
            input_str = input(sentence)
            number = int(input_str)
            if number > lower and number < upper: 
                return number
        except ValueError:
            pass

        print(f"You must type in an integer between {lower} and {upper}")


