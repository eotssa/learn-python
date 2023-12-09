```python
def grade(points):
    boundary = [0, 15, 18, 21, 24, 28]   # fixed: small logic error, adjusted to fit the lower bounds 
    for i in range(5, -1, -1):
        if points >= boundary[i]:
            return i
```