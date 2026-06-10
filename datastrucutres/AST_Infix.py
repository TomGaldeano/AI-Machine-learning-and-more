import queues
"""
A Grammar
The Postfix Expression Grammar
G = (N , T , P,E) where
N = {E}
T = {identifier, number, +, ∗}
P is defined by the set of productions
E → E E + | E E ∗ | number
"""
class TimesNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() * self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + "*" + self.right.inorder() + ")"
    
    def postfix(self):
        return self.left.postfix() + " " + self.right.postfix() + " *"
    
class DivNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() / self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + "/" + self.right.inorder() + ")"

    def postfix(self):
        return self.left.postfix() + " " + self.right.postfix() + " /"
    
class PlusNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() + self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + "+" + self.right.inorder() + ")"
    
    def postfix(self):
        return self.left.postfix() + " " + self.right.postfix() + " +"
    
class MinusNode:
    def __init__(self,left,right):
        self.left = left
        self.right = right

    def eval(self):
        return self.left.eval() - self.right.eval()
    
    def inorder(self):
        return "(" + self.left.inorder() + "-" + self.right.inorder() + ")"

    def postfix(self):
        return self.left.postfix() + " " + self.right.postfix() + " -"

class NumNode:
    def __init__(self,num):
        self.num = num

    def eval(self):
        return self.num
    
    def inorder(self):
        return str(self.num)
    
    def postfix(self):
        return str(self.num)

def E(q):
    if q.isEmpty():
        raise ValueError("Invalid Prefix Expression")
    token = q.dequeue()
    if token == "+":
        return PlusNode(E(q),E(q))
    if token == "*":
        return TimesNode(E(q),E(q))
    if token == "-":
        return MinusNode(E(q),E(q))
    if token == "/":
        return DivNode(E(q),E(q))
    return NumNode(float(token))    


    
def top_down_parser():
    """
     top-down parser. Not all parsers are constructed
    this way. The prefix grammar presented in this text is a grammar where the top-down
    parser construction will work. In particular, a grammar cannot have any left-recursive
    rules if we are to create a top-down parser for it
    """
    #x = input("Please Enter a prefix expression")
    x = "+ * + 5 4 6 3"
    lst = x.split()
    q = queues.Queue()
    for token in lst:
        q.enqueue(token)
    root = E(q)
    
    print(f"The infix form is: {root.inorder()}")
    print(f"The postfix form is: {root.postfix()}")
    print(f"The result is: {root.eval()}")
    


if __name__ == "__main__":
    top_down_parser()