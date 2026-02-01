class LinkedList:
    """
    List is better in performance but the linked list can take up gaps in memory
    """
    class __Node:
        def __init__(self,item,next=None):
            self.item = item
            self.next = next
        
        def getItem(self):
            return self.item
        
        def getNext(self):
            return self.next
        
        def setItem(self,item):
            self.item = item

        def setNext(self,next):
            self.next = next

    def __init__(self, contents=[]):
        self.first = LinkedList.__Node(None,None)
        self.last = self.first
        self.numItems=0
        for e in contents:
            self.append(e)
    
    def __getitem__(self,index):
        if index >= 0 and index < self.numItems:
            cursor = self.first.getNext()
            for i in range(index):
                cursor = cursor.getNext()

            return cursor.getItem()
        raise IndexError("LinkedList out of range")
    
    def __setitem__(self,index,val):
        if index >= 0 and index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()
            cursor.setItem(val)
            return
        raise IndexError("LinkedList assignement out of range")
    
    def __add__(self,other):
        """
        Docstring for __add__
        
        Returns LinkedList of both lists
        """
        if type(self) != type(other):
            raise TypeError(f"Concatenate undefined for {str(type(self))} + \
                            {str(type(other))}")
        
        result = LinkedList()
        cursor = self.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = self.append(cursor.getItem())

        cursor = other.first.getNext()
        while cursor != None:
            result.append(cursor.getItem())
            cursor = self.append(cursor.getItem())

        return result

    def append(self,item):
        node = LinkedList.__Node(item)
        self.last.setNext(node)
        self.last = node
        self.numItems += 1   
    
    def insert(self,index,item):
        cursor = self.first
        if index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()

            node = LinkedList.__Node(item, cursor.getNext())
            cursor.setNext(node)
            self.numItems += 1
        else:
            self.append(item)

    def __len__(self):
        return self.numItems
    
    
    def delitem(self,index):
        cursor = self.first
        if self.numItems == 1 and index == 0:
            self.first = LinkedList.__Node(None,None)
            self.last = self.first
            self.numItems=0
        elif index < self.numItems:
            for i in range(index):
                cursor = cursor.getNext()

            cursor2 = cursor.getNext()
            cursor.setNext(cursor2.getNext())
            self.numItems -= 1
        elif index == self.numItems:
            for i in range(index-2):
                cursor = cursor.getNext()
            self.last=cursor.getNext()
            self.items=0

    def __eq__(self, other):
         if type(self) != type(other):
            raise TypeError(f"Concatenate undefined for {str(type(self))} + \
                            {str(type(other))}")
         if self.numItems == other.numItems and self.numItems == 0:
             return True
         elif self.numItems != other.numItems:
             return False
         else:
            cursor = self.first
            cursor2 = other.first
            if cursor.getItem()==cursor2.getItem():
                for i in range(self.numItems):
                    cursor = cursor.getNext()
                    cursor2 = cursor2.getNext()
                    if cursor.getItem()!=cursor2.getItem():
                        return False
            return True

    def __iter__(self):
        self.cursor = self.first
        return self
    
    def __next__(self):
        if self.cursor == None:
            raise StopIteration
        self.cursor = self.cursor.getNext()
        if self.cursor == None:
            raise StopIteration
        return self.cursor.getItem()
    
    def __contains__(self,item):
        if self.numItems == 0:
            return False
        else:
            cursor = self.first
            if cursor.getItem()==item:
                return True
            else:
                for i in range(self.numItems):
                    cursor = cursor.getNext()
                    if cursor.getItem() == item:
                        return True
            return False
            