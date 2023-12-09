Here is a recursive algorithm for a binary search:

```python
def binary_search(target: list, item: int, left : int, right : int):
    """ The function returns True if the item is contained in the target list, False otherwise """
    # If the search area is empty, item was not found
    if left > right:
        return False

    # Calculate the centre of the search area, integer result
    centre = (left+right)//2

    # If the item is found at the centre, return
    if target[centre] == item:
        return True

    # If the item is greater, search the greater half
    if target[centre] < item:
        return binary_search(target, item, centre+1, right)
    # Else the item is smaller, search the smaller half
    else:
        return binary_search(target, item, left, centre-1)


if __name__ == "__main__":
    # Test your function
    target = [1, 2, 4, 5, 7, 8, 11, 13, 14, 18]
    print(binary_search(target, 2, 0, len(target)-1))
    print(binary_search(target, 13, 0, len(target)-1))
    print(binary_search(target, 6, 0, len(target)-1))
    print(binary_search(target, 15, 0, len(target)-1))
```
```
True
True
False
False
```

## Binary Search

The `binary_search` function takes four arguments:

1. The target list
2. The item being searched for
3. Left edge of the search area
4. Right edge of the search area

When the function is first called, the search area covers the entire target list. The left edge is at index `0` and the right edge is at index `len(target)-1`. The function calculates the central index and checks that position on the list. Either the item was found, or the search continues to the smaller or greater half of the target list.

## Linear Search vs. Binary Search

### Linear Search

In a **linear search**:
- The search area is traversed from the beginning onwards.
- The search continues until either the item is found or we run out of the search area.
- The number of steps needed grows linearly with the size of the search area.
- Each search step covers only one search candidate from the beginning.
  
> **Example:** If the search area is a million items long and the item is not found, we would have to take a million search steps to make sure the item is not in the search area.

### Binary Search

In a **binary search**:
- The number of steps needed grows logarithmically.
- The search area is cut in half with each step.
- We determine if the item is either smaller or greater than the current search candidate at the centre.

> **Example:** If the item searched for is not found, and the search area has a million items, it will take at most 20 steps for binary search. This is because \(2^{20}\) is well over 1 million. Thus, with sorted search areas, binary search is much more efficient than linear search.
