def serpentine_traversal(root):
    global globvar
    globvar = ''

    if not root:
        return []
    else:
        globvar += str(root.data)
    h = height(root)

    ltr = False
    for i in range(1, h + 1):
        printGivenLevel(root, i, ltr)
        ltr = not ltr

    try:
        return [int(s) for s in globvar.split()]
    except:
        return globvar.split()


def printGivenLevel(root, level, ltr):
    global globvar

    if (root == None):
        return []
    if (level == 0):
        globvar += ' ' + str(root.data)
    elif (level > 0):

        if (ltr):
            printGivenLevel(root.left, level - 1, ltr)
            printGivenLevel(root.right, level - 1, ltr)
        else:
            printGivenLevel(root.right, level - 1, ltr)
            printGivenLevel(root.left, level - 1, ltr)


def height(node):
    if (node == None):
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)

        if (lheight > rheight):
            return (lheight + 1)
        else:
            return (rheight + 1)
