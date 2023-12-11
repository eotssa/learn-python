# Write your solution here:

# parameter - list of tupules (name, price, remaining stock) -> list items are sorted by lowest remaining stock
def sort_by_remaining_stock(items: list):
    return sorted(items, key=lambda x : x[2])