def radix_tree(*words):
    def insert(word):
        node = tree
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        return tree

    def compress(node):
        while len(node) == 1 and list(node.values())[0]:
            key, value = list(node.items())[0]
            del node[key]
            new_key = key + list(value.keys())[0]
            node[new_key] = value[list(value.keys())[0]]
            compress(node)
        for sub_node in node.values():
            compress(sub_node)
        return node

    tree = {}
    for word in words:
        if word:  # Skip empty strings
            tree = insert(word)
    tree = compress(tree)
    return tree
