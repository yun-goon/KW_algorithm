import random
from timeit import default_timer as timer

class Node(object):
    def __init__(self,key, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent
        self.color = "RED"

def insert(node, key, parent=None): #키값을 가진 노드를 부모에
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

def delete(node, root):
    if node == root:
        root = delete_node(node)
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

def right_rotate(x):
    y = x.left
    x.left = y.right
    if y.right != None:
        y.right.parent=x
    y.parent = x.parent
    if x.parent == None:
        root = y
    elif x == x.parent.right:
        x.parent.right = y
    else:
        x.parent.left = y
    y.right = x
    x.parent = y

def left_rotate(node):
    y = x.right
    x.right = y.left
    if y.left != None:
        y.left.parent = x

    y.parent = x.parent
    if x.parent == None:
        root = y
    elif x == x.parent.left:
        x.parent.left = y
    else:
        x.parent.right = y
    y.left =x
    x.parent = y

def rb_insert(node):
    insert(node) #일단 노드 삽입
    while node.parent.color == "RED":
        if node.parent == node.parent.parent.right: # p 가 오른쪽 자식일 때
            U = node.parent.parent.left
            if U.color == "RED": #case 3-1
                U.color = "BLACK"
                node.parent.color = "BLACK"
                node.parent.parent.color = "RED"
                node = node.parent.parent
            elif node == node.parent.left: #case 3-2-2
                node = node.parent
                right_rotate(node)
            node.parent.color = "BLACK"
            node.parent.parent.color = "RED"
            left_rotate(node.parent.parent)
        else: # p가 왼쪽 자식일 때
            U = node.parent.parent.right
            if U.color == "RED": #case 3-1
                U.color = "BLACK"
                node.parent.color = "BLACK"
                node.parent.parent.color ="RED"
                node = node.parent.parent
            elif node == node.parent.right: #p가 왼쪽자식, N이 오른쪽 자식 case 3-2-4
                node = node.parent
                left_rotate(node)
            node.parent.color = "BLACK"
            node.parent.parent.color = "RED"
            right_rotate(node.parent.parent)




x = random.sample(range(5000),10)
value = x[8]

root = None
for i in x:
    root=insert(root,i)
start =timer()

found = search(root, value)
print(timer() - start)

if found is not None:
    print('value', value, 'found', found.key)
    print(True if found.key == value else False)




# asciitree로 트리 그리기
from asciitree.drawing import BoxStyle, BOX_LIGHT
from asciitree import LeftAligned
from collections import OrderedDict

class NodeRenderer:
    def __init__(self):
        self.box_style = BoxStyle(gfx=BOX_LIGHT, horiz_len=1)

    def __call__(self, node):
        return f"[{node.key}]"

def draw_tree_asciitree(root):
    if root is None:
        return ""
    tree = OrderedDict()
    node_renderer = NodeRenderer()  # NodeRenderer 인스턴스 생성
    _draw_tree_asciitree(tree, root, node_renderer)  # node_renderer 인자로 전달
    return LeftAligned(draw=node_renderer.box_style)(tree)

def _draw_tree_asciitree(tree, node, node_renderer):
    if node is None:
        return
    tree[node_renderer(node)] = subtree = OrderedDict()
    _draw_tree_asciitree(subtree, node.left, node_renderer)
    _draw_tree_asciitree(subtree, node.right, node_renderer)


print(draw_tree_asciitree(root))