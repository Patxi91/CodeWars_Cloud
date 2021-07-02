class MyTree:

    def __init__(self, rootObj):
        self.key = rootObj
        self.childs = None

    def insert_child(self, newNode):
        if self.childs:
            self.childs.append(MyTree(newNode))
        else:
            self.childs = [MyTree(newNode)]

    def get_childs(self):
        return self.childs

    def set_root_val(self, value):
        self.key = value

    def get_root_val(self):
        return self.key


def pre_count(tree):
    count = 0
    if tree:
        count += 1
        if tree.childs:
            for child in tree.childs:
                print(f'Reached Node:{tree.key}')
                return count + pre_count(child)
        else:
            return 0


def count_nodes(node):
    # Handles empty node input
    if not node:
        return 0
    count = 1
    if node.childs:
        for child in node.childs:
            count += count_nodes(child)

    return count


def phone_number(phone_numbers):
    root = MyTree('')
    for num in phone_numbers:
        currNode = root
        for digit in num:
            if currNode.get_childs():
                if digit not in [child.get_root_val() for child in currNode.get_childs()]:
                    currNode.insert_child(digit)
                    currNode = currNode.childs[-1]
                else:
                    currNode = currNode.childs[[child.get_root_val() for child in currNode.get_childs()].index(digit)]
            else:
                currNode.insert_child(digit)
                currNode = currNode.childs[-1]
    return count_nodes(root)-1
