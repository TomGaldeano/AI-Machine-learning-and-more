from  BinarySearchTree import BinarySearchTree
def menu():
    print("Make a choice...")
    print("1. Insert into tree.")
    print("2. Delete from tree.")
    print("3. Lookup Value.")
    print("4: Show values")
    print("5. Exit.")
    return input("Choice? ")

def addElement(tree):
    num = input("insert? ")
    while num != "":
        tree.insert(float(num))
        num = input("insert?")

def looop():
    print("Binary Search Tree Program\n--------------------------")
    option = 0
    tree = BinarySearchTree()
    for i in [5,2,8,6,7,9,4,1]:
        tree.insert(float(i))
    while option != "5":
        option = menu()
        match option:
            case "1":
                addElement(tree)
            case "2":
                val = input("Value? ")
                tree.delete(float(val))
            case "3":
                val = float(input("Value? "))
                node = tree.getNode(float(val))
                if node!=None:
                    print(f"Yes, {val} is in the tree.")
                else:        
                    print(f"No, {val} is not in the tree.")
            case "4":
                print(tree)
        

looop()