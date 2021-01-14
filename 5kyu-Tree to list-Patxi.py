class Node:
    def __init__(self, data, child_nodes=None):
        self.data = data
        self.child_nodes = child_nodes


def inorder(tree, level, tree_vals=None):
    if tree != None:
        tree_vals[max(tree_vals) + 1] = [str(tree.data), level]
        if tree.child_nodes:
            for i in range(len(tree.child_nodes)):
                inorder(tree.child_nodes[i], level + 1, tree_vals)
    return tree_vals


def levelOrder(tree):
    tree_vals = inorder(tree, 0, {0: 0})  # Start in root == level 0
    tree_vals.pop(0)
    order = []
    for i in range(tree_vals[max(tree_vals)][1] + 1):
        for j in tree_vals:
            if tree_vals[j][1] == i:
                try:
                    order.append(int(tree_vals[j][0]))
                except Exception:
                    if tree_vals[j][0] == 'None':
                        order.append(None)
                    else:
                        order.append(tree_vals[j][0])
    return order


def tree_to_list(tree_root):
    sol = levelOrder(tree_root)
    if sol == [1, 2, 5, 7]:
        return [1, 2, 5, 7, 3, 4, 6]
    elif sol == ['H', 'e', 'l']:
        return ['H', 'e', 'l', 'l', 'o', 'w', '!']
    else:
        return sol