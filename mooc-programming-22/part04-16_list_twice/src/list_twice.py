# Write your solution here

num_list = []

while True:
    val = int(input())

    if val == 0:
        print("Bye!")
        break

    num_list.append(val)
    sorted_list = sorted(num_list)
    print("The list now:", num_list)
    print("The list in order:", sorted_list)
