# Write your solution here
def create_tuple(x: int, y: int, z: int):
    big = max(x, y, z)
    small = min(x, y, z)
    sum = x + y + z

    return (small, big, sum)