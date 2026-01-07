import random
import matplotlib.pyplot as plt
import mergesort
import quicksort
import time

def ej1():
    """1. Write a program that times the quicksort, the merge sort, and the built-in sort
    algorithms in Python to discover which one is better and to see their relative
    speeds. 
    Be sure to randomize the elements in the sequence prior to sorting them using
    quicksort. The complexity of merge sort and
    quicksort is O(n log n) so by computational complexity the three algorithms are
    equivalent. """
    lst = [random.randint(1,50) for i in range(10)]
    start =time.perf_counter()
    for i in range(1000):
        random.shuffle(lst)
        mergesort.mergeSort(lst)
    end = time.perf_counter()
    print("mergesort: ",end-start)
    start =time.perf_counter()
    for i in range(1000):
        random.shuffle(lst)
        quicksort.quicksort(lst)
    end = time.perf_counter()
    print("quicksort: ",end-start)
    start =time.perf_counter()
    for i in range(1000):
        random.shuffle(lst)
        sorted(lst)
    end = time.perf_counter()
    print("timsort: ",end-start)

def ej2():
    """2. The merge sort algorithm is not as commonly used as the quicksort algorithm
    because quicksort is an inplace sort while merge sort requires at least space for
    one extra copy of the list. In fact, merge sort can be implemented with exactly
    one extra copy of the list. In this exercise you are to re-implement the merge sort
    algorithm to use one extra copy of the list instead of allocating a new list each
    time two lists are merged.
    The extra list is allocated prior to calling the recursive part of the merge sort
    algorithm. Then, with each alternating level of recursion the merge sort algorithm
    copies to the other list, flipping between the two lists. To accomplish this, the
    mergeSortRecursively function should be given a new list of lists called lists
    instead of the seq list. At lists [0] is the seq list and at lists [1] is the extra copy of
    the list. One extra parameter is given to the mergeSortRecursively function. The
    index of the list to merge from is also provided. This index will flip back and
    forth between 0 and 1 as each recursive call to mergeSortRecursively occurs. This
    flipping of 0 to 1 to 0 and so on can be accomplished using modular arithmetic
    by writing:
    listToMergeFromIndex = (listToMergeFromIndex + 1) % 2
    The percent sign is the remainder after dividing by 2. Adding 1 and finding the
    remainder after dividing by two means that listToMergeFromIndex flips between
    0 and 1. So, the call is made as mergeSortRecursively(listToMergeFromIndex,
    lists, start, stop). The mergeSortRecursively function must return the new index
    of the list to merge from.
    One part of this new mergeSortRecursively function is a little tricky. There may
    be one more level of recursion on the left or right side for the two recursive calls
    to mergeSortRecursively. If this is the case, then the result from either the left
    or right half must be copied into the same list as the other half before the two
    halves can be successfully merged.
    When mergeSortRecursively returns to the mergeSort function the result of sort-
    ing may be in the original sequence or it may be in the copy. If it is in the copy,
    then the result must be copied back to the original sequence before returning.
    Complete this two list version of merge sort as described in this exercise and test
    it thoroughly. Then time this version of merge sort and compare those timings
    with the version of merge sort presented in the chapter and with the quicksort
    implementation presented in this chapter."""

def ej3():
    """3. Complete the tic tac toe program described in the section on 2-dimensional
    matrices. Use the code from Sect. 20.5 as your starting point. Then complete the
    sections that say they are left as an exercise for the student."""

def ej4():
    """4. Complete the LinkedList datatype by implementing the delete, equality, iterate,
    length, and membership operations. Make sure they have the complexity given
    in the LinkedList complexities table. Then, implement a test program in your
    main function to thorougly test the operations you implemented. Call the module
    linkedlist.py so that you can import this into other programs that may need it."""

def ej5():
    """5. Implement a queue data type using a linked list implementation. Create a set of
    test cases to throroughly test your datatype. Place the datatype in a file called
    queue.py and create a main function that runs your test cases."""

def ej6():
    """6. Implement a priority queue data type using a linked list implementation. In a
    priority queue, elements on the queue each have a priority where the lower
    the number the higher the priority. The priorities are usually just numbers. The
    priority queue has the usual enqueue, dequeue, and empty methods. When a
    value is enqueued it is compared to the priority of other items and placed in
    front of all items that have lower priority (i.e. a higher priority number)."""

def ej7():
    """7. Implement a stack data type using a linked list implementation. Create a set of
    test cases to throroughly test your datatype. Place the datatype in a file called
    stack.py and create a main function that runs your test cases."""

def ej8():
    """8. Implement the infix evaluator program described in the chapter. You should
    accept input and produce output as described in that section of the text. The
    input tokens should will all be separated by blanks to make retrieval of the
    tokens easy. Don’t forget to convert your number tokens from strings to floats
    when writing the program."""

def ej9():
    """9. Implement the radix sort algorithm described in the chapter. Use the algorithm to
    sort a list of words you find on the internet or elsewhere. Write a main program
    that tests your radix sort algorithm."""

def ej10():
    """10. Searching a sequence of items for a particular item takes O(n) time on average
    where n is the number of items in the list. However, if the list is sorted first, then
    searching for an item within the list can be done in O(log n) time by using a divide
    and conquer approach. This type of search is called binary search. The binary
    search algorithm starts by looking for the item in the middle of the sequence. If
    it is not found there then because the list is sorted the binary search algorithm
    knows whether to look in the left or right side of the sequence. Binary search
    reports True or False depending on whether the item is found. It is often written
    recursively being given a sequence and the beginning and ending index values
    in which to search for the item. For instance, to search an entire sequence called
    seq, binary search might be called as binarySearch(seq,0,len(seq)-1). Write a
    program that builds a PyList or just a Python list of values, sorts them, and
    then looks up random values within the list. Compute the lookup times for lists
    of various sizes and record your results in the PlotData.py format so you can
    visualize your results. You should see a O(log n) curve if you implemented binary
    search correctly."""

if __name__ == "__main__":
    ej1()