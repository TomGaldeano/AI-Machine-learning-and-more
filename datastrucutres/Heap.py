import random
import time
import quicksort

class Heap:
    class _Node:
        def __init__(self,val,index,left = None, right = None, parent = None):
            self.setVal(val)
            self.right = right
            self.left = left
            self.parent = parent
            self.index = index

        def getVal(self):
            return self.val

        def getRightChildIndex(self):
            return self.index*2 + 2

        def getParentIndex(self):
            return (self.index-1)//2

        def getLeftChildIndex(self):
            return self.index*2 + 1
        
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
                    return node.right.val
                
            def parent(node):
                if node.parent == None:
                    return
                else:
                    return node.getParent().val
            return f"parent: {parent(self)}, hash: {self.hash}, value: {self.val}, left: {left(self)}, right: {right(self)}"

    def __init__(self,LargeTop = True):
        self.array = []
        self.numItems = 0
        self.root = None
        self.LargeTop = LargeTop

    def __len__(self):
        return self.numItems
        
    def buildFrom(self, aSequence):
        for i in aSequence:
            self.add_element(i)

    def __siftUpFrom(self, node):
        if node == self.root:
            return
        parent = node.parent
        if self.LargeTop:            
            if parent.val < node.val:
                tmp = node.val
                node.val = parent.val
                parent.val = tmp
                self.__siftUpFrom(parent)
        else:
            if parent.val > node.val:
                tmp = node.val
                node.val = parent.val
                parent.setVal(tmp)
                self.__siftUpFrom(parent)

    def add_element(self, element):
        node = self.__Node(element,self.numItems)
        if self.root == None:
            self.root = node
            self.array.append(node)
        else:
            parent = self.array[node.getParentIndex()]
            node.parent = parent
            self.array.append(node)
            if node.index % 2 == 0:
                parent.right = node
            else:
                parent.left = node
        self.numItems +=1       
        self.__siftUpFrom(node)

    def remove(self, index):
        node = self.array[index]
        last = self.array[-1]
        if last != node: 
            val = node.val
            node.setVal(last.val)
            parent = last.getParent()
            if parent.left == last:
                parent.left = None
            else:
                parent.right = None          
            self.array.remove(last)
            self.__shiftDown(node)
        self.numItems -= 1
        return node

    def __shiftDown(self,node):
        if node.hasChildren(): 
            if node.left == None:
                child = node.right
            elif node.right == None:
                child = node.left
            else:
                if self.LargeTop:
                    if node.left.val > node.right.val:
                        child = node.left
                    else:
                        child = node.right
                else:
                    if node.left.val < node.right.val:
                        child = node.left
                    else:
                        child = node.right
            if self.LargeTop:
                if child.val > node.val:
                    temp = node.val
                    node.val = child.val
                    child.val = temp
                else:
                    return
            else:
                if child.val < node.val:
                    temp = node.val
                    node.val = child.val
                    child.val = temp
                else:
                    return
            self.__shiftDown(child)
        else:
            return

    def heapsort(self):
        temp = []
        for i in range(self.numItems):
            temp.append(self.array[0].val)
            self.remove(0)
                     
        self.root = None
        self.numItems = 0
        self.array=[]
        self.buildFrom(temp)
        return temp

    def __contains__(self, item):
        node = self.getNode(item)
        if node == None:
            return False
        return True
    
    def getNode(self,val):
        def __getNode(val,node):
            if node.val == val:
                return node
            if not node.hasChildren():
                return None
            if node.getLeft() == None:
                if node.getHash() <= val:
                    return __getNode(val,node.getRight())
                else:
                    return None
            if node.getRight() == None:
                if node.getHash() >= val:
                    return __getNode(val,node.getLeft())
                else:
                    return None
            if node.getHash() <= val:
                return __getNode(val,node.getRight())
            else:
                return __getNode(val,node.getLeft())
        if self.root == None:
            raise IndexError("no nodes in tree")
        return __getNode(val,self.root)

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

    def printNodes(self):
        if not self.array:
            print("<empty heap>")
            return

        levels = []
        level_start = 0
        level_size = 1
        while level_start < self.numItems:
            level_end = min(level_start + level_size, self.numItems)
            levels.append(self.array[level_start:level_end])
            level_start = level_end
            level_size *= 2

        value_width = max(len(str(node.getVal())) for node in self.array)
        slot_width = max(3, value_width + 2)
        tree_width = (2 ** len(levels)) * slot_width

        def node_position(level, position):
            slot_count = 2 ** level
            return round((position * 2 + 1) * tree_width / (slot_count * 2))

        for level, nodes in enumerate(levels):
            node_line = [" "] * tree_width
            positions = [node_position(level, index) for index in range(len(nodes))]
            for node, position in zip(nodes, positions):
                value = str(node.getVal()).center(slot_width)
                start = position - slot_width // 2
                node_line[start:start + len(value)] = value
            print("".join(node_line).rstrip())

            if level < len(levels) - 1:
                connector_line = [" "] * tree_width
                for index, node in enumerate(nodes):
                    parent_position = node_position(level, index)
                    left_position = node_position(level + 1, index * 2)
                    right_position = node_position(level + 1, index * 2 + 1)
                    if node.getLeft() is not None:
                        connector_line[(parent_position + left_position) // 2] = "/"
                    if node.getRight() is not None:
                        connector_line[(parent_position + right_position) // 2] = "\\"
                print("".join(connector_line).rstrip())

class PriorityQueueHeap(Heap):
    class _Node(Heap._Node):
        def __init__(self, val, index, value):
            super().__init__(val,index)
            self.value = value

    def __init__(self, LargeTop=False):
        super().__init__(LargeTop)

    def add_element(self, val, value):
        node = self._Node(val, self.numItems, value)
        if self.root is None:
            self.root = node
            self.array.append(node)
        else:
            parent = self.array[node.getParentIndex()]
            node.parent = parent
            self.array.append(node)
            if node.index % 2 == 0:
                parent.right = node
            else:
                parent.left = node
        self.numItems += 1
        self.__siftUpFrom(node)

    def heapsort(self):
        temp = []
        for i in range(self.numItems):
            temp.append((self.array[0].val, self.array[0].value))
            self.remove(0)

        self.root = None
        self.numItems = 0
        self.array = []
        for val, value in temp:
            self.add_element(val, value)
        return temp

    def buildFrom(self, aSequence):
        for val, value in aSequence:
            self.add_element(val, value)

    def __shiftDown(self, node):
        if node.hasChildren():
            if node.left is None:
                child = node.right
            elif node.right is None:
                child = node.left
            else:
                if self.LargeTop:
                    child = node.left if node.left.val > node.right.val else node.right
                else:
                    child = node.left if node.left.val < node.right.val else node.right

            if self.LargeTop:
                if child.val > node.val:
                    node.val, child.val = child.val, node.val
                    node.value, child.value = child.value, node.value
                    self.__shiftDown(child)
            else:
                if child.val < node.val:
                    node.val, child.val = child.val, node.val
                    node.value, child.value = child.value, node.value
                    self.__shiftDown(child)

    def __siftUpFrom(self, node):
        if node == self.root:
            return
        parent = node.parent
        if self.LargeTop:
            if parent.val < node.val:
                node.val, parent.val = parent.val, node.val
                node.value, parent.value = parent.value, node.value
                self.__siftUpFrom(parent)
        else:
            if parent.val > node.val:
                node.val, parent.val = parent.val, node.val
                node.value, parent.value = parent.value, node.value
                self.__siftUpFrom(parent)

    def remove(self, index):
        node = self.array[index]
        last = self.array[-1]
        if last != node:
            node.val, last.val = last.val, node.val
            node.value, last.value = last.value, node.value
            parent = last.getParent()
            if parent.left == last:
                parent.left = None
            else:
                parent.right = None          
            self.__shiftDown(node)
        self.array.remove(last)
        self.numItems -= 1
        return last

    def queue(self, val, value):
        self.add_element(val, value)

    def dequeue(self):
        if self.numItems == 0:
            raise IndexError("dequeue from empty priority queue")
        node = self.root
        ans = (node.val, node.value)
        self.remove(0)
        return ans
    
def test_v1():
    test = [random.randint(-10000, 10000) for _ in range(10)]
    test1 = list(test)
    test2 = list(test)
    hp = Heap(False)
    hp.buildFrom(test1)
    quicksort.quicksort(test2)
    test1 = hp.heapsort()
    print(test1)
    print(test2)
    if test1 == test2:
        print("it works")
        print("WWEEEEEEEEEEEEEEEEE!!!")

def queue_test():
    pq = PriorityQueueHeap(False)
    
    pq.queue(5, "five")
    pq.queue(3, "three")
    pq.queue(8, "eight")
    pq.queue(1, "one")
    pq.queue(4, "four")
    lst = pq.heapsort()
    print(lst)
    pq.printNodes()
    while len(pq) > 0:
        val, value = pq.dequeue()
        print(f"Dequeued: {val}, {value}")


def compare_sorting(sequence):
    heap_input = list(sequence)
    quicksort_input = list(sequence)

    heap = Heap(False)
    start = time.perf_counter()
    heap.buildFrom(heap_input)
    heap_result = heap.heapsort()
    heap_time = time.perf_counter() - start

    start = time.perf_counter()
    quicksort.quicksort(quicksort_input)
    quicksort_time = time.perf_counter() - start

    if len(sequence) <= 20:
        print(f"Heap sort result: {heap_result}")
        print(f"Quick sort result: {quicksort_input}")
    else:
        print(f"Heap sort result (first 10): {heap_result[:10]}")
        print(f"Quick sort result (first 10): {quicksort_input[:10]}")
    print(f"Input size: {len(sequence)}")
    print(f"Results match: {heap_result == quicksort_input}")
    print(f"Heap sort time: {heap_time:.8f} seconds")
    print(f"Quick sort time: {quicksort_time:.8f} seconds")
    return heap_result, quicksort_input

def speed_test():
    for size in (10, 100, 1000):
        random_values = [random.randint(-10000, 10000) for _ in range(size)]
        compare_sorting(random_values)

if __name__ == "__main__":
    #heap_test()
    #test_v1()
    #speed_test()
    queue_test()