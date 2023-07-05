class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_nth(head, index, data):
    if index < 0:
        raise ValueError("Index out of range")

    if index == 0:
        new_node = Node(data)
        new_node.next = head
        return new_node

    current = head
    prev = None
    count = 0

    while current is not None and count < index:
        prev = current
        current = current.next
        count += 1

    if count < index:
        raise ValueError("Index out of range")

    new_node = Node(data)
    prev.next = new_node
    new_node.next = current

    return head
