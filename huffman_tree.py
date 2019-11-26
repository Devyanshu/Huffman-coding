from binarytree import Node


class HuffmanCoding:

    def __init__(self, data):
        self.data = data
        self.total = sum(list(self.data.values()))

    def get_max_key(self):
        max_key = max(self.data, key=self.data.get)
        return max_key, self.data[max_key]

    def add_nodes(self, node):
        while True:
            if len(self.data.values()) == 1:
                break
            key, val = self.get_max_key()
            node.left = Node(val)
            del self.data[key]
            self.total = self.total - val
            node.right = Node(self.total)
            self.add_nodes(node.right)

    def print_tree(self):
        root = Node(self.total)
        self.add_nodes(root)

        print(root)


data = {
    1: 144,
    2: 20,
    3: 89,
    4: 10,
    5: 2
}


hc = HuffmanCoding(data)
hc.print_tree()
