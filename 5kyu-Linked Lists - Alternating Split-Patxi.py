class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if not head or not head.next:
        raise ValueError('Invalid list')
    node = head
    first = None
    second = None
    odd_p = True
    while node:
        if odd_p:
            new_first_node = Node(node.data)
            if first:
                first.next = new_first_node
            else:
                first_new = new_first_node
            first = new_first_node
            odd_p = False
        else:
            new_second_node = Node(node.data)
            if second:
                second.next = new_second_node
            else:
                second_new = new_second_node
            second = new_second_node
            odd_p = True
        node = node.next
    return Context(first_new, second_new)
