import time
import matplotlib.pyplot as plt
import random
REPETITIONS = 1000
def ej2():
    """
    2. Conduct an experiment to prove that the product of two numbers does not depend
    on the size of the two numbers being multiplied. Write a program that plots the
    results of multiplying numbers of various sizes together. HINT: To get a good
    reading you may want to do more than one of these multiplications and time
    them as a group since a multiplication happens pretty quickly in a computer.
    Verify that it truly is a O(1) operation. Do you see any anomalies? It might be
    explained by Python’s support of large integers. What is the cutoff point for
    handling multiplications in constant time? Why?   
    """
    vars = [100,100000,8**10,9**20,7**30,8**50]
    sizes = [];times=[]
    for i in vars:
        print("calculating",i)
        j=0
        sizes.append(len(str(i)))
        start = time.perf_counter()
        while j<REPETITIONS:
            i*i
            j +=1
        j=0
        end = time.perf_counter()
        times.append(end-start)
    plt.plot(sizes, times, marker='o')
    plt.xlabel("number size")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.grid(True)
    plt.show()
    

def ej3():
    """
    3. Write a program to gather experimental data about comparing integers. Compare
    integers of different sizes and plot the amount of time it takes to do those com-
    parisons Is thecomparison operation always O(1)? If not, can you theorize why? HINT: You
    may want to read about Python’s support for large integers.
    """
    vars = [100,100000,10**10,8**20,9**30,8**173]
    sizes = [];times=[]
    for i in vars:
        print("calculating",i)
        j=0
        sizes.append(len(str(i)))
        start = time.perf_counter()
        while j<REPETITIONS:
            j +=1
            i==i
        j=0
        end = time.perf_counter()
        times.append(end-start)
    plt.plot(sizes, times, marker='o')
    plt.xlabel("number size")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.grid(True)
    plt.show()

def index_tom(element,list):
    j=0
    while j<len(list):
        if list[j] == element:
            return j
        j +=1

def ej4():
    """
    4. Write a short function :hat searches for a particular value in a list and returns the
    position of that value in the list (i.e. its index). Then write a program that times
    how long it takes to search for an item in lists of different sizes. The size of the
    list is your n.  What is the complexity of this algorithm? Answer this
    question in a comment in your program and verify that the experimental results
    match your prediction. Then, compare this with the index method on a list. Which
    is more efficient in terms of computational complexity? HINT: You need to be
    careful to consider the average case for this problem, not just a trivial case.
    """
    times_ind = []
    times_tom = []
    sizes = [100,10000,1000000]
    element=105
    for i in sizes:
        elements = []
        j=0
        print("finding in size",i)
        while j<i:
            elements.append(random.randint(1,100))
            j +=1
        j=0
        start = time.perf_counter()
        print("index")
        while j<REPETITIONS:
            var = random.randint(1,i-1)
            elements[var] = element
            elements.index(element)
            elements[var] = random.randint(1,100)
            j +=1
        j=0
        end = time.perf_counter()
        times_ind.append(end-start)
        start = time.perf_counter()
        print("tom")
        while j<REPETITIONS:
            var = random.randint(1,i-1)
            elements[var] = element
            index_tom(element,elements)
            elements[var] = random.randint(1,100)
            j +=1
        j=0
        end = time.perf_counter()
        times_tom.append(end-start)
    plt.plot(sizes, times_tom, 'b+', sizes, times_ind,"g+")
    plt.xlabel("number size")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.grid(True)
    plt.show()

def list_sum(list1):
    j = 0
    acum = 0
    while j<len(list1):
        acum+=list1[j]
        j+=1



def ej5():
    """
    5. Write a short function that given a list, adds together all the values in the list and
    returns the sum. Write your program so it does this operation with varying sizes
    of lists. Record the time it takes to find the sum for various list sizes. What complexity is this
    algorithm? Answer this in a comment at the top of your program and verify it
    with your experimental data. Compare this data with the built-in sum function in
    Python that does the same thing. Which is more efficient in terms of computational
    complexity? HINT: You need to be careful to consider the average case for this
    problem, not just a trivial case.
    """
    
    sizes = [100,10000,1000000];times1=[];times2=[]
    for i in sizes:
        print(i)
        elements = [random.randint(1,100) for _ in range(i)]
        start = time.perf_counter()
        print("sum")
        for _ in range(REPETITIONS):
            sum(elements)
        end = time.perf_counter()
        times1.append(end-start)
        start = time.perf_counter()
        print("tom")
        for _ in range(REPETITIONS):
            list_sum(elements)
        end = time.perf_counter()
        times2.append(end-start)
    plt.plot(sizes, times1, "r+",sizes,times2,"g+")
    plt.xlabel("number size")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.grid(True)
    plt.show()

class cl():
    def __init__(self,size):
        self.size = size
        self.items = 0
        self.values = [None for _ in range(size)]
    
    def __getitem__(self,element):
        return self.values[element]
    
    def append(self,element):
        if self.items==self.size:
            self.values = [None for _ in range(self.size)]
            self.items = 0
        else:
            self.values[self.items]=element
            self.items += 1


def ej6():
    """
    6. Assume that you have a datatype called the Clearable type. This data type has a
    fixed size list inside it when it is created. So Clearable(10) would create a clearable
    list of size 10. Objects of the Clearable type should support an append operation
    and a lookup operation. The lookup operation is called __getitem__(item). 
    If cl is a Clearable list, then writing cl[item] will return the item if it is in the list and return, 
    None otherwise. Writing cl[item] results in a method call of cl.__getitem__(item).
    Unlike the append operation described in Sect. 2.10.1, when the Clearable object
    fills up the list is automatically cleared or emptied on the next call to append
    by setting all elements of the list back to None. The Clearable object should
    always keep track of the number of values currently stored in the object. Form a
    theory about the complexity of the append operation on this datatype. Then write
    a test program to test the Clearable object on different initial sizes and numbers
    of append operations. Create one sequence for each different initial size of the
    Clearable datatype and write your results in the plot format described in this
    chapter. Then comment on how your theory holds up or does not hold up given
    your experimentation results.
    """
    sizes = [100,10000,100000,1000000];times=[]
    for i in sizes:
        start = time.perf_counter()
        print(i)
        for _ in range(REPETITIONS):
            item = cl(i)
            item.append(3)
        end = time.perf_counter()
        times.append(end-start)
    plt.plot(sizes, times, marker='o')
    plt.xlabel("number size")
    plt.ylabel("Average Comparison Time (microseconds)")
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
   ej6()
