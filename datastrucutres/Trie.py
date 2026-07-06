class Trie:
    def __insert(node,item):
        pass

    def __contains(node, itme):
        pass

    class TrieNode:
        def __init__(self, item, next = None, follows = None):
            self.item = item
            self.next = next
            self.follows = follows
            
        def insert(self, item):
            if type(item) == str and len(item) == 1:
                if self.follows == None:
                    self.follows = dict()
                if item not in self.follows.keys():
                    self.follows[item] = Trie.TrieNode(item)
                return self.follows[item]    

            else:
                raise Exception("method only allows chars")

    def __init__(self):
        self.start = Trie.TrieNode(None)

    def insert(self, item):
        node = self.start.insert(item[0])
        for i in item[1:]:
            node = node.insert(i)

    def __contains(node, item):
        if node == None:
            return False
        if item == "":
            return True
        if node.follows == None:
            return False
        if item[0] in node.follows.keys():
            return Trie.__contains(node.follows[item[0]],item[1:])

    def __contains__(self, item):
        if item == "":
            return False
        return Trie.__contains(self.start,item)
    
def trie_test(filename):
    tri = Trie()
    with open(filename,"r") as f:
        data = f.readlines()
    for i in data:
        tri.insert(i[:-1])
    if "byte" in tri:
        print("found word")
    if "comemeloshuevos" in tri:
        print("hubo un problema")

if __name__ == "__main__":
    trie_test("AI-Machine-learning-and-more/datastrucutres/words/words2.txt")