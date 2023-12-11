# Write your solution here

def new_person(name: str, age: int):
    if name == "" or len(name) > 40: 
        raise ValueError("name is an empty string")
    
    if " " not in name: 
        #word_count = name.split(' ')
        #two_words = True
        #if word_count[0].isalpha() and word_count[1].isalpha():
            #two_words = False
    
        #if two_words:
        raise ValueError("name contains less than two words")


    if age < 0 or age > 150:
        raise ValueError()

    return (name, age)


if __name__ == "__main__":

    """

    If the values stored in the parameter variables are not valid, 
    the function should throw a ValueError exception.



    Invalid parameters in this case include:

    name is an empty string
    name contains less than two words
    name is longer than 40 characters
    age is a negative number
    age is greater than 150
    """

    """
    def new_person(name: str, age: int):
    # Validate name
    if name == "" or (" " not in name) or len(name) > 40:
        raise ValueError("Invalid argument value for name: " + name)
 
    # Validate age
    if age < 0 or age > 150:
        raise ValueError("Invalid argument value for age:" + str(age))
 
    # Both ok
    return (name, age)
    """