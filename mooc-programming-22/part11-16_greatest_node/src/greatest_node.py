# WRITE YOUR SOLUTION HERE:
class Node:
    """ Class is modeling single node in binary tree """
    def __init__(self, value, left_child:'Node' = None, right_child:'Node' = None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root: Node):
    value = root.value

    if root.left_child:
        left_value = greatest_node(root.left_child)
    else:
        left_value = value

    if root.right_child:
        right_value = greatest_node(root.right_child)
    else:
        right_value = value
    
    return max(value, left_value, right_value)




"""
def greatest_node(root: Node) -> int:
    # Base case: if the node has no children, return the node's value
    if not root.left_child and not root.right_child:
        return root.value

    # If only the left child is present
    if root.left_child and not root.right_child:
        left_greatest_value = greatest_node(root.left_child)
        return left_greatest_value if left_greatest_value > root.value else root.value

    # If only the right child is present
    if root.right_child and not root.left_child:
        right_greatest_value = greatest_node(root.right_child)
        return right_greatest_value if right_greatest_value > root.value else root.value

    # If both children are present
    if root.left_child and root.right_child:
        left_greatest_value = greatest_node(root.left_child)
        right_greatest_value = greatest_node(root.right_child)

        # Return the greatest value among the three
        return max(left_greatest_value, right_greatest_value, root.value)



"""