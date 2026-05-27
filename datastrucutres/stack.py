from linked_list import *
class Stack(LinkedList):
    def __init__(self):
        super().__init__(self)

    def pop(self):
        return self.delitem(self.numItems-1)

    

def stack_test():
    stack = Stack()
    stack.append(2)
    stack.append("dsds")
    stack.append(3)
    tnp = stack.pop()
    print(stack)
    a = stack.pop()
    print(stack)
    a = stack.pop()
    print(a,tnp)
    print(stack)

if __name__ == "__main__":
    stack_test()