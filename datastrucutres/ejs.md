9. Implement the radix sort algorithm described in the chapter. Use the algorithm to
sort a list of words you find on the internet or elsewhere. Write a main program
that tests your radix sort algorithm.

10. Searching a sequence of items for a particular item takes O(n) time on average
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
search correctly.