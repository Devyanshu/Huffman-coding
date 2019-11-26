from binarytree import Node

data = {
    1: 14,
    2: 20,
    3: 89,
    4: 10
}

total = sum(list(data.values()))


def get_max_key(dict):
    max_key = max(dict, key=dict.get)
    return max_key, dict[max_key]


def add_nodes(node, data):
    global total
    while True:
        if len(data.values()) == 1:
            break
        key, val = get_max_key(data)
        print(key, val)
        node.left = Node(val)
        del data[key]
        total = total - val
        node.right = Node(total)
        add_nodes(node.right, data)


def print_tree(data):
    root = Node(total)
    add_nodes(root, data)

    print(root)


print_tree(data)
