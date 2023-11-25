class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Pre-order traversal
def pre_order(node):
    if node is not None:
        result = [node.data]
        result += pre_order(node.left)
        result += pre_order(node.right)
        return result
    else:
        return []

# In-order traversal
def in_order(node):
    if node is not None:
        result = in_order(node.left)
        result.append(node.data)
        result += in_order(node.right)
        return result
    else:
        return []

# Post-order traversal
def post_order(node):
    if node is not None:
        result = post_order(node.left)
        result += post_order(node.right)
        result.append(node.data)
        return result
    else:
        return []
