# Write your solution here

listA = []
while True: 
    user_input = input("Word: ")
    
    if user_input in listA:         # returns true if word exists in list
        break

    listA.append(user_input)

print(f"You typed in {len(listA)} different words")