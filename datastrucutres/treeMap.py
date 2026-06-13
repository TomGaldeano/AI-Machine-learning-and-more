import orderedTree
class TreeMap():
    class __KVPair:
        def __init__(self,key,value):
            self.key = key
            self.value = value
        
        def __eq__(self, value):
            if type(self) != type(value):
                return False
            
            return self.key == value.key
        
        def getKey(self):
            return self.key
        
        def getValue(self):
            return self.value
        
        def __hash__(self):
            return hash(self.key)
        
    def __init__(self):
        self.treeMap = orderedTree.OrderedTreeSet()

    def __len__(self):
        return len(self.treeMap)
    
    def __contains__(self, item):
        return TreeMap.__KVPair in self.treeMap

    def __getitem__(self,key):
        node = self.treeMap.getNode(self.__KVPair(key,None))
        if node == None:
            raise KeyError("Key " + str(key) + " not in TreeMap")
        return node.getVal().getValue()

    def __setitem__(self, key, value):
        self.treeMap.insert(TreeMap.__KVPair(key,value))

    def __iter__(self):
        for x in self.treeMap:
            yield x.getKey()
    
    def delete(self,key):
        self.treeMap.delete(TreeMap.__KVPair(key,None))

    def seeNodes(self):
        self.treeMap.printNodes()

def test():
    print("Treemap testing")
    tree = TreeMap()
    tree["ew"] = 2
    print(tree["ew"])
    tree.seeNodes()

if __name__ == "__main__":
    test()