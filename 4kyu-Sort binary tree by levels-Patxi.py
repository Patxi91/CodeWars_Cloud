def tree_iterator(node: Node):
    # create a list to loop through
    nodes = [node]
    # loop
    while nodes:
        # yield from the list
        yield from nodes
        # internal loop
        for n in nodes[:]:
            # add to list if exists
            if n.left: nodes.append(n.left)
            if n.right: nodes.append(n.right)
            # remove from teh main list loop
            nodes.remove(n)

def tree_by_levels(node):
    # return a list of values from our helper function
    # otherwise return `[]` if node is empty
    return [n.value for n in tree_iterator(node)] if node else []
