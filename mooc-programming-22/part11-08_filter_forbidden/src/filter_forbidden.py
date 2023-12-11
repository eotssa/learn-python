# WRITE YOUR SOLUTION HERE
def filter_forbidden(string: str, forbidden: str):
    return "".join([char for char in string if not char in forbidden])