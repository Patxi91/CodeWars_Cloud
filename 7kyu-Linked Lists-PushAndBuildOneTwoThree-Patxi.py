from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

def push(head, data):
    # Create a new node with the given data
    new_node = Node(data)

    # If the head is None, the new node becomes the head
    if head is None:
        head = new_node
    else:
        # Otherwise, set the next of the new node to the current head
        new_node.next = head
        # Update the head to be the new node
        head = new_node

    return head

def build_one_two_three():
    # Initialize an empty linked list
    head = None

    # Push the values 3, 2, and 1 onto the linked list
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)

    return head
