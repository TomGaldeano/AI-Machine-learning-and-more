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
        
    def __init__(self):
        self.root = None
    
    def insert(self,val):
        """
        The __insert function is recursive and is not a passed a self parameter. It is a
        static function (not a method of the class) but is hidden inside the insert
        function so users of the class will not know it exists
        """
        def __insert(root,val,parent):
            if root == None:
                return BinarySearchTree.__Node(val,parent = parent)
            if val < root.getVal():
                root.setLeft(__insert(root.getLeft(),val,root))
            else:
                root.setRight(__insert(root.getRight(),val,root))
            return root

        self.root = __insert(self.root,val,self.root)

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
        if node == None:
            raise IndexError("Element does not exist")
        if node.hasChildren():
            pass
        else:
            parent = node.getParent()
            if parent.getLeft() == node:
                parent.setLeft(None)
            else:
                parent.setRight(None)


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
                if node.getRight().getVal() <= val:
                    return __getNode(val,node.getRight())
                else:
                    return None
            if node.getRight().getVal() >= val:
                return __getNode(val,node.getRight())
            if node.getRight().getVal() <= val:
                    return __getNode(val,node.getRight())
            return None            

        if self.root == None:
            raise IndexError("no nodes in tree")
        return __getNode(val,self.root)
    


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