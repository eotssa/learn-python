## Binary Trees and Recursive Algorithms

A **binary tree** is a branched structure consisting of nodes, and each node can, at most, branch into two child nodes. Visually, a binary tree can be imagined as an inverted tree, where the root is at the top and branches extend downwards.

Recursive algorithms are well-suited for binary trees since they can naturally traverse and process the tree structure. A typical recursive traversal on a binary tree involves:

1. Processing the current node.
2. Calling the function recursively on the left child node.
3. Calling the function recursively on the right child node.

Both the left and right child nodes, known as "subtrees," can be considered as individual binary trees. 

Iterative solutions for tree traversal can be more complex, as they might need additional structures or logic to keep track of the visited nodes.

### Implementing a Binary Tree in Python

A binary tree can be represented using a class definition for a node. Each node has a value and pointers to its left and right child nodes.

```python
class Node:
    """ The class represents a single node in a binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child
```

For instance, to create the following tree:
You can use the following code:

```python
if __name__ == "__main__":
    tree = Node(2)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(5)
    tree.left_child.right_child = Node(8)

    tree.right_child = Node(4)
    tree.right_child.right_child = Node(11)
```

### Recursive Algorithms for Binary Trees

1. **Printing all nodes**:
   A simple recursive algorithm can be used to print all the nodes of a binary tree.

   ```python
   def print_nodes(root: Node):
       print(root.value)

       if root.left_child is not None:
           print_nodes(root.left_child)

       if root.right_child is not None:
           print_nodes(root.right_child)
   ```

   For the tree mentioned above, the output will be:
   ```
   2
   3
   5
   8
   4
   11
   ```

2. **Sum of all nodes**:
   You can calculate the sum of all values stored in the nodes of the tree using a recursive approach.

   ```python
   def sum_of_nodes(root: Node):
       node_sum = root.value

       if root.left_child is not None:
           node_sum += sum_of_nodes(root.left_child)

       if root.right_child is not None:
           node_sum += sum_of_nodes(root.right_child)

       return node_sum
   ```

### Sorted Binary Trees

Binary trees become especially powerful when they're sorted. One common type of sorted binary tree ensures that for any given node:
- The left child node is smaller than the current node.
- The right child node is greater than the current node.

![Sorted Binary Tree](11_4_1.png)

This sorting allows us to efficiently search for a node within the tree using a recursive approach similar to binary search. If the current node matches the desired value, the search is successful. Otherwise, the search continues in the left or right subtree depending on the desired value.

```python
def find_node(root: Node, value):
    if root is None:
        return False

    if value == root.value:
        return True

    if value > root.value:
        return find_node(root.right_child, value)

    return find_node(root.left_child, value)
```

In summary, recursive algorithms are particularly well-suited for processing binary trees due to the hierarchical and branched nature of trees. Whether it's traversing the tree, searching for a node, or performing some operation on each node, recursion provides an elegant and efficient approach.