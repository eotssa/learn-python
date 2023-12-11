from random import choice 
from string import ascii_lowercase
from string import digits
from random import shuffle


def generate_strong_password(length: int, if_num: bool, if_spch: bool):
    
    spec_chrs = "!?=+-()#"
    pwd = []

    # ensures 1 char
    pwd.append(choice(ascii_lowercase))

    # ensures 1 digit if true
    if if_num:
        pwd.append(choice(digits))

    # ensures 1 spch if true
    if if_spch:
        pwd.append(choice(spec_chrs))

    # populates list randomly
    while len(pwd) < length:
        if not if_num and not if_spch:
            pwd.append(choice(ascii_lowercase))
        elif if_num and not if_spch: 
            pwd.append(choice(ascii_lowercase + digits))
        elif not if_num and if_spch:
            pwd.append(choice(ascii_lowercase + spec_chrs))
        elif if_num and if_spch:
            pwd.append(choice(ascii_lowercase + digits + spec_chrs))

    # shuffles the list, shuffle is the reason why we used a list instead of string 
    shuffle(pwd)
    
    return ''.join(pwd)
    


if __name__ == "__main__":
    for i in range(10):
        print(generate_strong_password(8, True, True))
