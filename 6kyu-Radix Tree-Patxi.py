def radix_tree(*input_words):
    unique_words = set(input_words)
    root_node = {}

    def insert_word(word, node):
        if word[0] not in node:
            node[word[0]] = {}
        if word[1:]:
            insert_word(word[1:], node[word[0]])

    def compress_tree(node, current=''):
        for key, value in node.items():
            compress_tree(value, current + key)
        for key, value in list(node.items()):
            if len(value) == 1 and (current + key) not in unique_words:
                node[key + list(value.keys())[0]] = list(value.values())[0]
                del node[key]

    for word in unique_words:
        if word:
            insert_word(word, root_node)
    compress_tree(root_node)
    return root_node
