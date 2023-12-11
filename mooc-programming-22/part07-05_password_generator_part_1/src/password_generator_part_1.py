# Write your solution here
from random import choice
from string import ascii_lowercase


def generate_password(length: int):
    
    pwd = ""
    for i in range(length):
        pwd += choice(ascii_lowercase)

    return pwd

