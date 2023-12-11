# DO NOT CHANGE CLASS Book!
# Write your solution after the class!

class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year

# -----------------------------
# Write your solution here
# -----------------------------


def older_book(book1: Book, book2: Book):
    if book1.year < book2. year:
        print(f"{book1.name} is older, it was published in {book1.year}")
    elif book1.year > book2.year:
        print(f"{book2.name} is older, it was published in {book2.year}")
    else:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")



"""
I can see why we would use "older" because it's less confusing when we access year variable 
here we use book1.year for both book1 and book2 year's. 


class Book:
    def __init__(self, name: str, author: str, genre: str, year: int):
        self.name = name
        self.author = author
        self.genre = genre 
        self.year = year
 
def older_book(book1: Book, book2: Book):
    same = True
    if book1.year < book2.year:
        older = book1
        same = False
    elif book1.year > book2.year:
        older = book2
        same = False
 
    if same:
        print(f"{book1.name} and {book2.name} were published in {book1.year}")
    else:
        print(f"{older.name} is older, it was published in {older.year}")
        
"""

