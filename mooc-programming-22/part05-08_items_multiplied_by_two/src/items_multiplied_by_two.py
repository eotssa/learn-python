# Write your solution here
def double_items(numbers: list[int]): 
    this_list = []
    for num in numbers: 
        this_list.append(num * 2)

    return this_list


if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)

"""Expected Method

def double_items(numbers: list):
    double = numbers[:]             # why won't "double = numbers" work here? -- would copy a reference, and change the original. 
    for i in range(len(double)):
        double[i] *= 2
    
    return double

"""