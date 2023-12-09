```python
class ShoppingList:
    def __init__(self):
        self.products = []

    def number_of_items(self):
        return len(self.products)

    def add(self, product: str, number: int):
        self.products.append((product, number))

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n < len(self.products):
            product = self.products[self.n]
            self.n += 1
            return product
        else:
            raise StopIteration


def products_in_shopping_list(shopping_list, amount: int):
    return [product[0] for product in shopping_list if product[1] >= amount]

if __name__ == "__main__":

    my_list = ShoppingList()
    my_list.add("bananas", 10)
    my_list.add("apples", 5)
    my_list.add("alcohol free beer", 24)
    my_list.add("pineapple", 1)

    print("the shopping list contains at least 8 of the following items:")
    for product in products_in_shopping_list(my_list, 8):
        print(product)
```

In Python, an iterator is an object that implements two methods: `__iter__()` and `__next__()`. The `__iter__` method should return the iterator object itself, and the `__next__` method should return the next value from the iterator.

When you define the `__iter__` method in a class and have it return `self`, you are saying that instances of the class are their own iterators. That means the object itself will be used to keep track of the iteration state (in this case, the `n` attribute), and the `__next__` method will be called on the object itself to get each successive value.

Here's a step-by-step explanation of what happens when you iterate over an instance of the `ShoppingList` class:

1. **Calling `__iter__`**: When you start a `for` loop (or a list comprehension) over a `ShoppingList` object, Python first calls the object's `__iter__` method to get an iterator.
2. **Returning `self`**: Inside the `__iter__` method, `self` is returned. This means that the `ShoppingList` object itself is the iterator. It's the object that the `for` loop will call `__next__` on to get the next value.
3. **Calling `__next__`**: The `for` loop then repeatedly calls the `__next__` method on the `ShoppingList` object (since it's the iterator) to get the next value.
4. **Using the `n` attribute**: Inside the `__next__` method, the `n` attribute is used to keep track of the current position in the iteration. It's incremented each time `__next__` is called.
5. **Returning the next value**: The `__next__` method returns the product tuple at the current position, and this is the value that the `for` loop (or list comprehension) uses.

By having the `__iter__` method return `self`, you are making the `ShoppingList` object responsible for its own iteration. It's a common pattern when you want an object to be iterable, and the object itself needs to keep track of the iteration state (like the current position).