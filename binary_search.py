import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self,key,parent):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent

def insert(node, key):
    if node is None:
        node = Node(key)
    elif key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right, key)
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

x = random.sample(range(5000),1000)
value = x[800]

root = None
for i in x:
    root=insert(root,i)
start =timer()

found = search(root, value)
print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)