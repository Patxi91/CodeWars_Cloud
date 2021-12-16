class Node():
    def __init__(self):
        self.next = None



def loop_size(node):
    b = True
    nodes = []
    while b:
        if node not in nodes:
            nodes.append(node)
            node = node.next
        else:
            b= False

    return len(nodes[nodes.index(node):])

node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

print(loop_size(node1)) #3
