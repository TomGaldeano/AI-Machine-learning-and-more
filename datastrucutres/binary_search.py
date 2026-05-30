import random
import time
def binary_search(elements,element):
    if elements == []:
        return -1
    if elements[0] > element or elements[-1]< element:
        return -1
    maximum = len(elements)
    minimum = 0
    get_index = lambda x, y: (x+y)//2
    while (maximum-minimum)>0:
        index = get_index(maximum,minimum)
        if element == elements[index]:
            return element
        if element>elements[index]:
            minimum = index
        else:
            maximum = index
    if elements[minimum]==element:
        return minimum
    if elements[maximum]==element:
        return maximum
    return -1


def test():
    lst = [i for i in range(10)]
    if(binary_search(lst,4)==4):
       print("test1 solved")
    else:
       print("test1 failed")
    if(binary_search(lst,23) == -1):
       print("found not in list")
    else:
        print("mistake")

def timer():
    lst = [i for i in range(10)]
    start =time.perf_counter()
    for _ in range(1000):
        a = random.randint(0,10)
        binary_search(lst,a)
    end = time.perf_counter()
    print("size 10: ",end-start)
    lst = [i for i in range(1000)]
    start =time.perf_counter()
    for _ in range(1000):
        a = random.randint(0,1000)
        binary_search(lst,a)
    end = time.perf_counter()
    print("size 1000: ",end-start)
    lst = [i for i in range(10000)]
    start =time.perf_counter()
    for _ in range(1000):
        a = random.randint(0,100000)
        binary_search(lst,a)
    end = time.perf_counter()
    print("size 100000: ",end-start)

if __name__=="__main__":
    test()
    timer()
    