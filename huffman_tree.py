from binarytree import Node


class HuffmanCoding:

    def __init__(self, data):
        self.data = data
        self.total = sum(list(self.data.values()))
        self.table = {}
        self.temp = {i: v for i, v in data.items()}
        self.curr = ''

    def get_max_key(self):
        max_key = max(self.data, key=self.data.get)
        return max_key, self.data[max_key]

    def add_nodes(self, node):
        while True:
            if len(self.data.values()) == 1:
                self.table[list(self.data.keys())[0]] = self.curr
                break
            key, val = self.get_max_key()
            node.left = Node(val)
            self.table[key] = self.curr + '0'
            del self.data[key]
            self.total = self.total - val
            node.right = Node(self.total)
            # if self.total in self.data.values():
            #     self.table[key] = self.curr + '1'
            self.curr = self.curr + '1'
            self.add_nodes(node.right)

    def print_tree(self):
        root = Node(self.total)
        self.add_nodes(root)
        print(root)

    def print_table(self):
        for key in self.temp:
            print('{}: {}'.format(key, self.table[key]))

    def calculate_cr(self):
        original_bits = sum([self.temp[i] * 8 for i in self.temp])
        after_compression = sum(
            [len(self.table[i])*i for i in self.table])
        return original_bits/after_compression


data = {
    1: 144,
    2: 20,
    3: 8,
    4: 100,
    5: 25
}


hc = HuffmanCoding(data)
hc.print_tree()
hc.print_table()
print('Compression ratio: {}'.format(round(hc.calculate_cr(), 2)))
