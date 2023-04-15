import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self, key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def insert(node, key, parent=None):
    if node is None:
        node = Node(key, parent)
    elif key < node.key:
        node.left = insert(node.left, key, node)
    else:
        node.right = insert(node.right, key, node)
    return node

def search(node, key):
    if node is None or node.key == key:
        return node
    if key < node.key:
        return search(node.left, key)
    return search(node.right, key)

def delete(node):
    if node == root:
        root = delete-node(node)
    elif node == node.parent.left:
        node.parent.left = delete_node(node)
    else:
        node.parent.right = delete_node(node)

def delete_node(r):
    if r.left == None and r.right == None:
        return None
    elif r.left != None and r.right == None:
        return r.left
    elif r.right != None and r.left == None:
        return r.right
    else:
        s = r.right
        while s.left != None:
            parent = s
            s = s.left
        r.key = s.key
        if s == r.right:
            r.right = s.right
        else:
            parent.left = s.right
        return r

x = random.sample(range(5000),100)
value = x[80]

root = None
for i in x:
    root=insert(root,i)
start =timer()

found = search(root, value)
print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)



node_to_delete = search(root, value)
delete(node_to_delete)

def print_tree(node, level=0):
    if node is not None:
        print_tree(node.right, level + 1)
        print(" " * 4 * level + "->", node.key)
        print_tree(node.left, level + 1)

print_tree(root)
