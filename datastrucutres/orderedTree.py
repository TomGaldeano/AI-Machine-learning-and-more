class OrderedTreeSet:
    class __Node:
        def __init__(self,val,left = None, right = None, parent = None):
            self.setVal(val)
            self.right = right
            self.left = left
            self.parent = parent

        def getVal(self):
            return self.val
        
        def setVal(self, val):
            self.val = val
            try:
                self.hash=hash(val)
            except TypeError:
                self.hash = hash(str(val))
        
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
        
        def getHash(self):
            return self.hash
        
        def __hash__(self):
            return self.hash

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
            return f"parent: {parent(self)}, hash: {self.hash}, value: {self.val}, left: {left(self)}, right: {right(self)}"
        
    def __init__(self):
        self.root = None
        self.numItems = 0
    
    def insert(self,val):
        """
        The __insert function is recursive and is not a passed a self parameter. It is a
        static function (not a method of the class) but is hidden inside the insert
        function so users of the class will not know it exists
        """
        def __insert(root,val):
            hashVal = hash(val)
            if root == None:
                if type(val)== OrderedTreeSet.__Node:
                    return val
                return OrderedTreeSet.__Node(val)
            if root.getHash() == hashVal:
                raise TypeError
            if hashVal < root.getHash():
                root.setLeft(__insert(root.getLeft(),val))
                root.getLeft().setParent(root)
            else:
                root.setRight(__insert(root.getRight(),val))
                root.getRight().setParent(root)
            return root
        try:
            self.root = __insert(self.root,val)
            self.numItems += 1
        except TypeError:
            pass

    def __len__(self):
        return self.numItems

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
    
    def __contains__(self, item):
        node = self.getNode(item)
        if node == None:
            return False
        return True
    
    def delete(self,val):
        node = self.getNode(val)
        if node == None:
            raise ValueError("item not in OrderedTreeSet")
        print(node)
        def __delete(node):
            if node == None:
                raise IndexError("Element does not exist")
            if not node.hasChildren():
                if node == self.root:
                    self.root = None
                else:
                    parent = node.getParent()
                    if parent.getLeft() == node:
                        parent.setLeft(None)
                    else:
                        parent.setRight(None)
            elif node.getLeft() == None:
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

        def __getrightmost(node):
            if node.getRight() == None:
                return node
            return __getrightmost(node.getRight())

        if node.getLeft() != None and node.getRight() != None:
            left = node.getLeft()
            if left.getRight()==None:
                node.setVal(left.getVal())
                node.setLeft(left.getLeft())
            else:
                right = __getrightmost(left)
                if right.hasChildren():
                    node.setVal(right.getVal())
                    __delete(right)
                else:
                    node.setVal(right.getVal())
                    right.getParent().setRight(None)
        else:
            __delete(node)
        node = self.getNode(val)
        self.numItems -= 1

    def getNode(self,val):
        def __getNode(val,node):
            try:
                hashVal = hash(val)
            except TypeError:
                hashVal = hash(str(val))
            if node.getHash() == hashVal:
                return node
            if not node.hasChildren():
                return None
            if node.getLeft() == None:
                if node.getHash() <= hashVal:
                    return __getNode(val,node.getRight())
                else:
                    return None
            if node.getRight() == None:
                if node.getHash() >= hashVal:
                    return __getNode(val,node.getLeft())
                else:
                    return None
            if node.getHash() <= hashVal:
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
    tree = OrderedTreeSet()
    for i in ["aa",4,[2],44.3,{2},4]:
        tree.insert(i)
    print(tree)
    tree.delete(4)
    print(tree)

if __name__ == "__main__":
    main()