from preloaded import Node
import operator
import collections
import itertools


# Traverse and map keys to levels
def inorder(tree, level, tree_vals=None):
    if tree != None:
        inorder(tree.left, level + 1, tree_vals)
        tree_vals[tree.data] = level
        inorder(tree.right, level + 1, tree_vals)
    return tree_vals


def serpentine_traversal(tree: Node) -> list:
    if not tree:
        return []
    tree_vals = inorder(tree, 0, {})  # Start in root == level 0
    order = []
    o = 1
    tmp = []
    for i in range(tree_vals[max(tree_vals.items(), key=operator.itemgetter(1))[0]] + 1):
        for j in tree_vals:
            if tree_vals[j] == i:
                tmp.append(j)
        order.append(tmp[::o])
        tmp = []
        o *= -1

    try:
        # if all([int(s) for s in list(itertools.chain.from_iterable(order)) if s.isdigit()]) and [int(s) for s in list(itertools.chain.from_iterable(order)) if s.isdigit()]:
        #    return [int(s) for s in list(itertools.chain.from_iterable(order)) if s.isdigit()]
        if all([int(s) for s in list(itertools.chain.from_iterable(order))]) and [int(s) for s in [int(s) for s in list(
                itertools.chain.from_iterable(order))]:
            return [int(s) for s in list(itertools.chain.from_iterable(order))]
    except:
        return list(itertools.chain.from_iterable(order))
