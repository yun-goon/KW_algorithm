import random

class Node():
    def __init__(self,val):
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1


class RB_Tree():
    def __init__(self):
        self.NULL = Node (0)
        self.NULL.color =0
        self.NULL.left =None
        self.NULL.right =None
        self.root = self.NULL

    def insertNode(self, key):
        node = Node(key)
        node.parent = None
        node.val = key
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   
        y = None
        x = self.root
        while x != self.NULL:                           
            y = x
            if node.val < x.val:
                x = x.left
            else:
                x = x.right
        node.parent = y                                  
        if y == None:           
            self.root = node
        elif node.val < y.val:  
            y.left = node
        else:
            y.right = node
        if node.parent == None:
            node.color = 0
            return
        if node.parent.parent == None:
            return
        self.RB_Insert (node)

    def LR ( self , x ) :
        y = x.right
        x.right = y.left
        if y.left != self.NULL :
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left :
            x.parent.left = y
        else :
            x.parent.right = y
        y.left = x
        x.parent = y

    def RR (self, x) :
        y = x.left
        x.left = y.right
        if y.right != self.NULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right :
            x.parent.right = y
        else :
            x.parent.left = y
        y.right = x
        x.parent = y

    def RB_Insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.RR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.LR(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.LR(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.RR(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    # print test
    def __printCall (self, node, indent, last) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.val ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )
    def print_tree ( self ) :
        self.__printCall ( self.root , "" , True )




if __name__ == "__main__":
    test = RB_Tree()

    x = random.sample(range(5000),50)
    for i in x:
        test.insertNode(i)
    test.print_tree()

    test.insertNode(1999)
    test.print_tree()