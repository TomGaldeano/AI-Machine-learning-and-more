class BinarySearchTree:
    class __Node:
        def __init__(self,val,left = None, right = None, parent = None):
            self.val = val
            self.right = right
            self.left = left
            self.parent = None

        def getVal(self):
            return self.val
        
        def setVal(self, val):
            self.val = val
        
        def getLeft(self):
            return self.left
        
        def setLeft(self,left):
            self.left = left
        
        def getRight(self):
            return self.right
        
        def setRight(self,right):
            self.right = right
        
        def getParent(self):
            return self.parent
        
        def setParent(self,parent):
            self.parent = parent

        def hasChildren(self):
            if self.right == None and self.left == None:
                return False
            return True

        def __iter__(self):
            """inorder traversal"""
            if self.left != None:
                for elem in self.left:
                    yield elem
            yield self.val
            if self.right != None:
                for elem in self.right:
                    yield elem

        def __str__(self):
            def left(node):
                if node.getLeft() == None:
                    return
                else:
                    return node.getLeft().getVal()
                
            def right(node):
                if node.getRight() == None:
                    return
                else:
                    return node.getRight().getVal()
                
            def parent(node):
                if node.getParent() == None:
                    return
                else:
                    return node.getParent().getVal()
            return f"parent: {parent(self)}, value: {self.val}, left: {left(self)}, right: {right(self)}"
        
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        """
        The __insert function is recursive and is not a passed a self parameter. It is a
        static function (not a method of the class) but is hidden inside the insert
        function so users of the class will not know it exists
        """
        def __insert(root,val):
            if root == None:
                return BinarySearchTree.__Node(val)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val))
                root.getLeft().setParent(root)
            else:
                root.setRight(__insert(root.getRight(),val))
                root.getRight().setParent(root)
            return root
        self.root = __insert(self.root,val)

    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()
        
    def __str__(self):
        ans = ""
        for i in self:
            ans = ans +str(i) + " - "
        return ans[:-3]
    
    def delete(self,val):
        node = self.getNode(val)
        def __delete(node):
            if node == None:
                raise IndexError("Element does not exist")
            if node.getLeft() == None:
                parent = node.getParent()
                if parent.getRight() == node:
                    parent.setRight(node.getRight())
                    parent.getRight().setParent(parent)
                else:
                    parent.setLeft(node.getRight())
                    parent.getLeft().setParent(parent)
            elif node.getRight() == None:
                parent = node.getParent()
                if parent.getRight() == node:
                    parent.setRight(node.getLeft())
                    parent.getRight().setParent(parent)
                else:
                    parent.setLeft(node.getLeft())
                    parent.getLeft().setParent(parent)
            else:
                if node == self.root:
                    self.root = None
                else:
                    parent = node.getParent()
                    if parent.getLeft() == node:
                        parent.setLeft(None)
                    else:
                        parent.setRight(None)

        def __getrightmost(node):
            if node.getRight() == None:
                return node
            return __getrightmost(node.getRight())

        if node.getLeft() != None and node.getRight() != None:
            left = node.getLeft()
            if left.getRight()==None:
                node.setVal(left.getVal())
                __delete(left)
            else:
                right = __getrightmost(left)
                if right.hasChildren():
                    node.setVal(right.getVal())
                    __delete(right)
                else:
                    node.setVal(right.getVal())
                    right.getParent().setRight(None)

        else:
            __delete()

    def getNode(self,val):
        def __getNode(val,node):
            if node.getVal() == val:
                return node
            if not node.hasChildren():
                return None
            if node.getLeft() == None:
                if node.getRight().getVal() >= val:
                    return __getNode(val,node.getRight())
                else:
                    return None
            if node.getRight() == None:
                if node.getLeft().getVal() <= val:
                    return __getNode(val,node.getLeft())
                else:
                    return None
            if node.getVal() <= val:
                return __getNode(val,node.getRight())
            else:
                return __getNode(val,node.getLeft())

        if self.root == None:
            raise IndexError("no nodes in tree")
        return __getNode(val,self.root)
    
    def printNodes(self):
        def nodePrint(node):
            if node.hasChildren():
                print(node)
                if node.getLeft() != None:
                    nodePrint(node.getLeft())
                if node.getRight() != None:
                    nodePrint(node.getRight())
            else:
                print(node)
            return
        nodePrint(self.root)

def main():
    s = input("Enter a list of numbers: ")
    lst = s.split()
    tree = BinarySearchTree()
    for i in lst:
        tree.insert(float(i))
    print(tree)
    for i in tree:
        print(type(i))

if __name__ == "__main__":
    main()