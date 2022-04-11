""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""


def sorted_insert(head, data):
    def r(node, data):
        if not node:
            return Node(data)
        if node.data > data:
            node_new = Node(data)
            node_new.next = node
            return node_new
        node.next = r(node.next, data)
        return node

    return r(head, data)
