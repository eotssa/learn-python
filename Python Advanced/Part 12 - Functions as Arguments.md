# Functions as arguments

A sorting method or function usually accepts an optional second argument which allows you to bypass the default sorting criteria. This second argument is a function which defines how the value of each item on the list is determined. As the list is sorted, Python calls this function when it compares the items to each other.

```python
def order_by_price(item: tuple):
    # Return the price, which is the second item within the tuple
    return item[1]

if __name__ == "__main__":
    products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

    # Use the function order_by_price for sorting
    products.sort(key=order_by_price)

    for product in products:
        print(product)
```
```Sample output
('apple', 3.95)
('orange', 4.5)
('watermelon', 4.95)
('banana', 5.95)
```

## `products.sort(key=order_by_price)`


Here the `sort` method is called with a function as its argument. This is not a reference to the return value of the function, but a reference to the function itself. The sort method calls this function multiple times, using each item on the list as the argument in turn.

If we include an extra print statement in the function definition of order_by_price, we can verify that the function does indeed get called once per each item on the list:

```python
def order_by_price(item: tuple):
    # Print the item
    print(f"Function call: order_by_price({item})")

    # Return the price, which is the second item within the tuple
    return item[1]


products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

# Use the function order_by_price for sorting
products.sort(key=order_by_price)

#prints out sorted list
for product in products:
    print(product)
```

```
Function call: order_by_price(('banana', 5.95))
Function call: order_by_price(('apple', 3.95))
Function call: order_by_price(('orange', 4.5))
Function call: order_by_price(('watermelon', 4.95))
('apple', 3.95)
('orange', 4.5)
('watermelon', 4.95)
('banana', 5.95)
```

### The order can be reversed with another keyword argument: `reversed`

```python
products.sort(key=order_by_price, reverse=True)

t2 = sorted(products, key=order_by_price, reverse=True)
```

# A function definition within a function definition

```python
def order_by_price(item: tuple):
    return item[1]

def sort_by_price(items: list):
    # use the order_by_price function here
    return sorted(items, key=order_by_price)

products = [("banana", 5.95), ("apple", 3.95), ("orange", 4.50), ("watermelon", 4.95)]

for product in sort_by_price(products):
    print(product)
```

If we know that the helper function `order_by_price` is not used anywhere outside the s`ort_by_price` function, we can place the former function definition within the latter function definition:

```python
def sort_by_price(items: list):
    # helper function defined within the function
    def order_by_price(item: tuple):
        return item[1]

    return sorted(items, key=order_by_price)
```

### **Programming Exercise: Sort by Remaining Stock**

**Task**:
Write a function named `sort_by_remaining_stock(items: list)`. This function takes a list of tuples as its argument. Each tuple represents a product with its name, price, and remaining stock. Your task is to return a new list where the items are sorted by their remaining stock in ascending order (lowest value first). It's essential that the original list remains unmodified.

**Example**:

```python
products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22)]

for product in sort_by_remaining_stock(products):
    print(f"{product[0]} {product[2]} pcs")
```

**Sample output**:
```
orange 2 pcs
apple 3 pcs
banana 12 pcs
watermelon 22 pcs
```

---

**Your Solution**:

```python
# Place your solution here

# parameter - list of tupules (name, price, remaining stock) -> list items are sorted by lowest remaining stock
def sort_by_remaining_stock(items: list):
    return sorted(items, key=lambda x : x[2])
```


### **Programming Exercise: Sort by Number of Seasons**

**Task**:
Write a function named `sort_by_seasons(items: list)`. This function takes a list of dictionaries as its argument. Each dictionary contains the details of a TV show, including its name, rating, and the number of seasons. Your task is to return a new list where the TV shows are sorted by their number of seasons in ascending order. Ensure that the original list remains unmodified.

**Example**:

```python
shows = [
    { "name": "Dexter", "rating" : 8.6, "seasons":9 },
    { "name": "Friends", "rating" : 8.9, "seasons":10 },
    { "name": "Simpsons", "rating" : 8.7, "seasons":32 }
]

for show in sort_by_seasons(shows):
    print(f"{show['name']} {show['seasons']} seasons")
```

**Sample output**:
```
Dexter 9 seasons
Friends 10 seasons
Simpsons 32 seasons
```

---

**Your Solution**:

```python
# Place your solution here

# parameter - list of dictionaries with keys "name", "rating", and "seasons" -> list items are sorted by number of seasons in ascending order
def sort_by_seasons(items: list):
    return sorted(items, key=lambda x: x['seasons'])
```

### **Programming Exercise: Sort by Ratings**

**Task**:
Write a function named `sort_by_ratings(items: list)`. The function takes a list of dictionaries as its argument, with each dictionary containing details of a TV show, including its name, rating, and the number of seasons. Your task is to return a new list where the TV shows are sorted by their ratings in descending order. Ensure that the original list remains unmodified.

**Example**:

```python
shows = [
    { "name": "Dexter", "rating" : 8.6, "seasons":9 },
    { "name": "Friends", "rating" : 8.9, "seasons":10 },
    { "name": "Simpsons", "rating" : 8.7, "seasons":32 }
]

print("Rating according to IMDB")
for show in sort_by_ratings(shows):
    print(f"{show['name']}  {show['rating']}")
```

**Sample output**:
```
Rating according to IMDB
Friends 8.9
Simpsons 8.7
Dexter 8.6
```

---

**Your Solution**:

```python
# Place your solution here
def sort_by_ratings(items: list):
    return sorted(items, key=lambda x : x["rating"], reverse=True)
```

**Model Solution** 
```python
def sort_by_ratings(items: list):
    def rating_order(item):
        return item["rating"]
        
    return sorted(items, key=rating_order, reverse=True)
```


### **Programming Exercise: Sort by Ratings**

**Task**:
Write a function named `sort_by_ratings(items: list)`. The function takes a list of dictionaries as its argument, with each dictionary containing details of a TV show, including its name, rating, and the number of seasons. Your task is to return a new list where the TV shows are sorted by their ratings in descending order. Ensure that the original list remains unmodified.

**Example**:

```python
shows = [
    { "name": "Dexter", "rating" : 8.6, "seasons":9 },
    { "name": "Friends", "rating" : 8.9, "seasons":10 },
    { "name": "Simpsons", "rating" : 8.7, "seasons":32 }
]

print("Rating according to IMDB")
for show in sort_by_ratings(shows):
    print(f"{show['name']}  {show['rating']}")
```

**Sample output**:
```
Rating according to IMDB
Friends 8.9
Simpsons 8.7
Dexter 8.6
```

---

**Your Solution**:

```python
# Place your solution here
# list of dictionary (each dict has details on 1 TV show)
def sort_by_ratings(items: list):
    return sorted(items, key=lambda x : x["rating"], reverse=True)
```


### Sorting collections of your own objects

### **Programming Exercise: ClimbingRoute**

**Task**:

The exercise template contains the class definition for a `ClimbingRoute`. 

**Example**:

```python
route1 = ClimbingRoute("Edge", 38, "6A+")
route2 = ClimbingRoute("Smooth operator", 9, "7A")
route3 = ClimbingRoute("Synchro", 14, "8C+")

print(route1)
print(route2)
print(route3.name, route3.length, route3.grade)
```

**Sample output**:
```
Edge, length 38 metres, grade 6A+
Smooth operator, length 9 metres, grade 7A
Synchro 14 8C+
```

---

**Sort by Length**:

Please write a function named `sort_by_length(routes: list)` which returns a new list of routes, sorted by length from longest to shortest.

**Example**:

```python
r1 = ClimbingRoute("Edge", 38, "6A+")
r2 = ClimbingRoute("Smooth operator", 11, "7A")
r3 = ClimbingRoute("Synchro", 14, "8C+")
r4 = ClimbingRoute("Small steps", 12, "6A+")

routes = [r1, r2, r3, r4]

for route in sort_by_length(routes):
    print(route)
```

**Sample output**:
```
Edge, length 38 metres, grade 6A+
Synchro, length 14 metres, grade 8C+
Small steps, length 12 metres, grade 6A+
Smooth operator, length 9 metres, grade 7A
```

---

**Sort by Difficulty**:

Please write a function named `sort_by_difficulty(routes: list)` which returns a new list of routes, sorted by difficulty.

**Example**:

```python
# ca1, ca2 and ca3 declared as above
routes = [r1, r2, r3, r4]
for route in sort_by_difficulty(routes):
    print(route)
```

**Sample output**:
```
Synchro, length 14 metres, grade 8C+
Smooth operator, length 11 metres, grade 7A
Edge, length 38 metres, grade 6A+
Small steps, length 12 metres, grade 6A+
```

---

**Your Solution**: 
### sorting by multiple criteria 

```python
# Place your solution here
class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

# Write your solution here:

def sort_by_length(routes: list):
    def get_length(route: ClimbingRoute):
        return route.length 

    return sorted(routes, key=get_length, reverse=True)

def sort_by_difficulty(routes: list):
    def get_grade(route: ClimbingRoute):
        return (route.grade, route.length) # purpose: sort by grade, then length 
    
    return sorted(routes, key=get_grade, reverse=True)

if __name__ == "__main__":


    r1 = ClimbingRoute("Small steps", 13, "6A+")
    r2 = ClimbingRoute("Edge", 38, "6A+")
    r3 = ClimbingRoute("Bukowski", 9, "6A+")
    reply = sort_by_difficulty([r1, r2, r3])

    for route in reply:
        print(route)
```


---

### **Programming Exercise: Climbing Areas**

**Task**:

In addition to the `ClimbingRoute` from the previous exercise, the exercise template contains the class definition for a `ClimbingArea`.

**Example**:

```python
ca1 = ClimbingArea("Olhava")
ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

ca2 = ClimbingArea("Nummi")
ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

ca3 = ClimbingArea("Nalkkila slab")
ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

print(ca1)
print(ca3.name, ca3.routes())
print(ca3.hardest_route())
```

**Sample output**:
```
Olhava, 3 routes, hardest 6B
Nalkkila slab 4
Smooth operator, length 9 metres, grade 7A
```

---

**Sort by Number of Routes**:

Please write a function named `sort_by_number_of_routes` which sorts climbing areas in ascending order based on the number of routes they each have.

**Example**:

```python
# ca1, ca2 and ca3 declared as above
areas = [ca1, ca2, ca3]
for area in sort_by_number_of_routes(areas):
    print(area)
```

**Sample output**:
```
Nummi, 1 routes, hardest 8C+
Olhava, 3 routes, hardest 6B
Nalkkila slab, 4 routes, hardest 7A
```

---

**Sort by the Most Difficult Route**:

Please write a function named `sort_by_most_difficult` which sorts climbing areas in descending order based on the most difficult route in each area.

**Example**:

```python
# ca1, ca2 and ca3 declared as above
areas = [ca1, ca2, ca3]
for area in sort_by_most_difficult(areas):
    print(area)
```

**Sample output**:
```
Nummi, 1 routes, hardest 8C+
Nalkkila slab, 4 routes, hardest 7A
Olhava, 3 routes, hardest 6B
```

---

**Your Solution**:

```python
# Place your solution here
class ClimbingRoute:
    def __init__(self, name: str, length: int, grade: str):
        self.name = name
        self.length = length
        self.grade = grade

    def __str__(self):
        return f"{self.name}, length {self.length} metres, grade {self.grade}"

class ClimbingArea:
    def __init__(self, name: str):
        self.name = name
        self.__routes = []

    def add_route(self, route: ClimbingRoute):
        self.__routes.append(route)

    def routes(self):
        return len(self.__routes)

    def hardest_route(self):
        def by_difficulty(route):
            return route.grade

        routes_in_order = sorted(self.__routes, key=by_difficulty)
        # last route
        return routes_in_order[-1]

    def __str__(self):
        hardest_route = self.hardest_route()
        return f"{self.name} {self.routes()} routes, hardest {hardest_route.grade}"


# list of ClimbingAreas
def sort_by_number_of_routes(areas: list):
    def num_routes(area: ClimbingArea):
        return area.routes()

    return sorted(areas, key=num_routes)

# list of ClimbingAreas
def sort_by_most_difficult(areas: list):
    # first returns the ClimbingRoute, then we access ClimbingRoute route's grade. 
    def hardest(area: ClimbingArea):
        return area.hardest_route().grade

    return sorted(areas, key=hardest, reverse=True)


if __name__ == "__main__":
    ca1 = ClimbingArea("Olhava")
    ca1.add_route(ClimbingRoute("Edge", 38, "6A+"))
    ca1.add_route(ClimbingRoute("Great cut", 36, "6B"))
    ca1.add_route(ClimbingRoute("Swedish route", 42, "5+"))

    ca2 = ClimbingArea("Nummi")
    ca2.add_route(ClimbingRoute("Synchro", 14, "8C+"))

    ca3 = ClimbingArea("Nalkkila slab")
    ca3.add_route(ClimbingRoute("Small steps", 12, "6A+"))
    ca3.add_route(ClimbingRoute("Smooth operator", 11, "7A"))
    ca3.add_route(ClimbingRoute("Piggy not likey", 12 , "6B+"))
    ca3.add_route(ClimbingRoute("Orchard", 8, "6A"))

    print(ca1)
    print(ca3.name, ca3.routes())
    print(ca3.hardest_route())


    # ca1, ca2 and ca3 declared as above
    areas = [ca1, ca2, ca3]
    for area in sort_by_number_of_routes(areas):
        print(area)


    # ca1, ca2 and ca3 declared as above
    areas = [ca1, ca2, ca3]
    for area in sort_by_most_difficult(areas):
        print(area)
```