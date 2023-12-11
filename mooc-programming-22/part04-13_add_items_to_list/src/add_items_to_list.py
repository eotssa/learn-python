# Write your solution here3

num_items = int(input())
listA = []

i = 1
while i <= num_items:
    value = int(input("Item " + str(i) + ": "))
    listA.append(value)
    i += 1

print(listA)