# Write your solution here

listA = [1, 2, 3, 4, 5]

while True: 
    index = int(input())
    if index == -1:
        break    
    value = int(input())

    listA[index] = value
    print(listA)



