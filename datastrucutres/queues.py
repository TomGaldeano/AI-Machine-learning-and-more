import linked_list
import random
class Queue:
    def __init__(self):
        self.items = []
        self.frontIdx = 0

    def __compress(self):
        newlst = []
        for i in range(self.frontIdx,len(self.items)):
            newlst.append(self.items[i])
        self.items = newlst
        self.frontIdx = 0
    
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty queue")
            # When queue is half full, compress it. This
            # achieves an amortized complexity of O(1) while    
            # not letting the list continue to grow unchecked.
        if self.frontIdx * 2 > len(self.items):
            self.__compress()
        item = self.items[self.frontIdx]
        self.frontIdx += 1
        return item

    def enqueue(self,item):
        self.items.append(item)
    
    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to access front of empty queue")
        return self.items[self.frontIdx]

    def isEmpty(self):
        return self.frontIdx == len(self.items)

class LinkedQueue(linked_list.LinkedList):
    def __init__(self):
        super().__init__(self)

    def isEmpty(self):
        if self.numItems==0:
            return True
        return False
    
    def dequeue(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty linked queue")
        item = self.__getitem__(0)
        self.delitem(0)
        return item
    
    def enqueue(self,item):
        self.append(item)

    def front(self):
        if self.isEmpty():
            raise RuntimeError("Attempt to dequeue an empty linked queue")
        item = self.items[0]
        return item

class PriorityLinkedQueue(LinkedQueue):
    def __init__(self):
        super().__init__()
        self.max = 0
        self.min = 0
    
    def enqueue(self, item, priority:int ):
        if type(priority) != int:
            if self.numItems == 0:
                self.max = priority
                self.min = priority
                self.append[priority,item]
        else:
            raise TypeError("priority must be an int")
        

def LinkedQueueTest():
    test = LinkedQueue()
    for i in range(10):
        test.append(i)
    test.dequeue()
    test.enqueue(5)
    test.dequeue()
    for  i in test:
        print(i)

def Priority_test():
    test = PriorityLinkedQueue()
    for i in range(5):
        test.append(random.randin(1,5),random.randint(1,5))

if __name__== "__main__":
    LinkedQueueTest()
    Priority_test()