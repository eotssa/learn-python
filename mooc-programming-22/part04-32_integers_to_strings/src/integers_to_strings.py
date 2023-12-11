# Write your solution here
def formatted(my_list : list[float]) -> list[str]:
    str_list = []
    for num in my_list:
        str_list.append(f"{num:.2f}")

    return str_list