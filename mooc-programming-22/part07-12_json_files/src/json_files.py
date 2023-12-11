# Write your solution here
import json

def print_persons(filename: str):
    with open(filename, "r") as my_file:
        data = my_file.read()
    

    data_read = json.loads(data)

    
    for person in data_read:
        print(f"{person['name']} {person['age']} years ({', '.join(person['hobbies'])})")




