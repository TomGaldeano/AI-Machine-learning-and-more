#The set method is implemented like this
class HashSet:
    def __init__(self,contents=[]):
        self.items = [None] * 10
        self.numItems = 0
        for item in contents:
            self.add(item)

    class _PlaceHolder:
        def __init__(self):
            pass

        def __eq__(self, value):
            return False
         
    def __add(item,items):
        idx = hash(item) % len(items)
        loc = -1
        while items[idx] != None:
            if items[idx]== item:
                #item already in set
                return False
            if loc < 0 and type(items[idx]) == HashSet._PlaceHolder:
                loc = idx
            idx = (idx +1) %len(items)
        if loc < 0:
            loc = idx
        items[loc] = item
        return True

    @classmethod
    def __rehash(cls,oldList,newList):
        """needed so that HasHset is never full so that search can be O(1). here 75% is chosen"""
        for x in oldList:
            if x != None:
                HashSet.__add(x,newList)
        return newList
        
    def add(self,item):
        if HashSet.__add(item,self.items):
            self.numItems+=1
            load = self.numItems/len(self.items)
            if load >= 0.75:
                self.items = HashSet.__rehash(self.items,[None]*2*len(self.items))
    
    @classmethod 
    def __remove(cls,item,items):
        idx = hash(item) % len(items)
        while items[idx] != None:
            if items[idx] == item:
                nextIdx = (idx+1) % len(items)
                if [nextIdx] == None:
                    items[idx] = None
                else:
                    items[idx] = HashSet._PlaceHolder()
                return True
            idx = (idx + 1) % len(items)
        return False
    
    def remove(self,item):
        if HashSet.__remove(item,self.items):
            self.numItems -= 1
            load = max(self.numItems, 10) / len(self.items)
            if load <= .25:
                self.item = HashSet.__rehash(self.items,[None]*(len(self.items))//2)
        else:
            raise KeyError("Item not in HashSet")
    
    def __contains__(self, item):
        """
        Finding an item results in O(1) amortized complexity as well. The chains are kept
        short as long as most hash values are evenly distributed and the load factor is kept
        from approaching 1.
        """
        idx = hash(item) % len(self.items)
        while self.items[idx] != None:
            if self.items[idx] == item:
                return True
            idx = (idx + 1) % len(self.items)
        return False
    
    def __eq__(self, value):
        if type(value) != HashSet:
            raise TypeError("Element must be a HashSet")
        return self.items == value.items
    
    def __len__(self):
        return self.numItems
    
    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] != None and type(self.items[i]) != HashSet._PlaceHolder:
                yield self.items[i]

    def difference_update(self,other):
        for item in other:
            self.remove(item)

    def differerence(self,other):
        result = HashSet(self)
        result.difference_update(other)
        return result
    
    def __getitem__(self, key):
        idx = hash(key) % len(self.items)
        while self.items != None:
            if self.items[idx] == key:
                return self.items[idx]
            idx = (idx + 1) % len(self.items)
        return None
    
    def update(self,other):
        if type(other) != HashSet:
            raise TypeError("Element must be a HashSet")
        for i in other:
            self.add(i)

    def union(self,other):
        if type(other) != HashSet:
            raise TypeError("Element must be a HashSet")
        ans = HashSet()
        for i in self:
            ans.add(i)
        for i in other:
            ans.add(i)
        return ans

    def intersection(self,other):
        ans = HashSet()
        for i in self:
            if i in other:
                ans.add(i)
        return ans
    
    def intersection_update(self,other):
        if type(other) != HashSet:
            raise TypeError("Element must be a HashSet")
        for i in self:
            if i not in other:
                self.discard(i)

    def discard(self,other):
        try:
            self.remove(self,other)
        except:
            pass
    
    def pop(self):
        a = 0
        for i in self:
            a = i
        self.remove(a)
        return a
    
    def clear(self):
        self.items = len(self.items)*[None]

    def issubset(self,other):
        if type(other) != HashSet:
            raise TypeError("Element must be a HashSet") 
        for i in self:
            if i not in other:
                return False
        return True
    
    def issuperset(self,other):
        if type(other) != HashSet:
            raise TypeError("Element must be a HashSet") 
        for i in other:
            if i not in self:
                return False
        return True
    
    def isdisjoined(self,other):
        if type(other) != HashSet:
            raise TypeError("Element must be a HashSet")
        disjoined = True
        for i in other:
            if i in self:
                disjoined = False
        return disjoined
    
    def symmetric_difference(self,other):
        ans = HashSet()
        for i in self:
            if i not in other:
                ans.add(i)
        for i in other:
            if i not in self:
                ans.add(i)
        return ans
    
    def symmetric_difference_update(self,other):
        items = []
        for i in self:
            if i not in other:
                items.append(i)
        for i in other:
            if i not in self:
                items.append(i)
        self.clear()
        for i in items:
            self.add(i)
                    

def tester():
    test = HashSet([23,"gr","ew",12,11,12,"geree"])
    test2 = HashSet([23,"gr","ew",12,"geree"])
    poped = test2.pop()
    if len(test2) == 4:
        print("pop works")
    if test2.issubset(test):
        print("subset works")
    if test.issuperset(test2):
        print("superset works")
    if not test.isdisjoined(test2):
        print("disjoined works")
    test.add(10)
    if len(test) == 6:
        print("create works")
        print("len works")
    test.clear()
    if test == HashSet():
        print("clear works")
        print("equal works")

def union_test():
    test = HashSet([23,"gr","ew",12,11,12,"geree"])
    test2 = HashSet([23,"gr","ew",12,"geree"])
    test3 = test.union(test2)
    if test3 == test:
        print("union works")
    test2.update(test)
    if test2 == test:
        print("update works")

def intersection_test():
    test = HashSet([23,"gr","ew",12,11,12,"geree"])
    test2 = HashSet([23,"gr","ew",12,"geree"])
    test3 = test.intersection(test2)
    if test3 == test2:
        print("intersection works")
    test3.intersection_update(test2)
    if test3 == test2:
        print("intersection update works")

def symetric_difference_test():
    test = HashSet([23,"gr","ew",12,11,12,"geree"])
    test2 = HashSet([23,"gr","ew",12,"geree"])
    test3 = test.symmetric_difference(test2)
    if test3 == HashSet([11]):
        print("symmetric difference works")
    test.symmetric_difference_update(test2)
    if test3 == test:
        print("symmetric difference update works")

if __name__ == "__main__":
    tester()
    union_test()
    intersection_test()
    symetric_difference_test()
