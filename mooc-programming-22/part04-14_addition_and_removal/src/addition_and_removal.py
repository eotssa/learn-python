# Write your solution here

listA = []
counter = 1
print("The list is now", listA)

while True:
    user_input = input()

    if user_input.lower() == "d":
        listA.append(counter)
        print("The list is now", listA)
        counter += 1
    elif user_input.lower() == "r":
        listA.remove(counter - 1)
        print("The list is now", listA)
        counter -= 1
    elif user_input.lower() == "x":
        print("Bye!")
        break