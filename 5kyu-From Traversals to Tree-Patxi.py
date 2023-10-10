from preloaded import TreeNode


def build_tree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder.pop()
    root = TreeNode(root_val)

    root_index = inorder.index(root_val)

    root.right = build_tree(inorder[root_index + 1:], postorder)
    root.left = build_tree(inorder[:root_index], postorder)

    return root
