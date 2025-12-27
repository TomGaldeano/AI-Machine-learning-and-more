```
64 2 Computational Complexity
2.13 Programming Problems
1. Devise an experiment to discover the complexity of comparing strings in Python.
Does the size of the string affect the efficiency of the string comparison and if so,
what is the complexity of the comparison? In this experiment you might want to
consider a best case, worst case, and average case complexity. Write a program
that produces an XML file with your results in the format specified in this chapter.
Then use the PlotData.py program to visualize those results.
2. Conduct an experiment to prove that the product of two numbers does not depend
on the size of the two numbers being multiplied. Write a program that plots the
results of multiplying numbers of various sizes together. HINT: To get a good
reading you may want to do more than one of these multiplications and time
them as a group since a multiplication happens pretty quickly in a computer.
Verify that it truly is a O(1) operation. Do you see any anomalies? It might be
explained by Python’s support of large integers. What is the cutoff point for
handling multiplications in constant time? Why? Write a program that produces
an XML file with your results in the format given in this chapter. Then visualize
your results with the PlotData.py program provided in this chapter.
3. Write a program to gather experimental data about comparing integers. Compare
integers of different sizes and plot the amount of time it takes to do those com-
parisons. Plot your results by writing an XML file in the Ploy.py format. Is the
comparison operation always O(1)? If not, can you theorize why? HINT: You
may want to read about Python’s support for large integers.
4. Write a short function that searches for a particular value in a list and returns the
position of that value in the list (i.e. its index). Then write a program that times
how long it takes to search for an item in lists of different sizes. The size of the
list is your n. Gather results from this experiment and write them to an XML file
in the PlotData.py format. What is the complexity of this algorithm? Answer this
question in a comment in your program and verify that the experimental results
match your prediction. Then, compare this with the index method on a list. Which
is more efficient in terms of computational complexity? HINT: You need to be
careful to consider the average case for this problem, not just a trivial case.
5. Write a short function that given a list, adds together all the values in the list and
returns the sum. Write your program so it does this operation with varying sizes
of lists. Record the time it takes to find the sum for various list sizes. Record this
information in an XML file in the PlotData.py format. What complexity is this
algorithm? Answer this in a comment at the top of your program and verify it
with your experimental data. Compare this data with the built-in sum function in
Python that does the same thing. Which is more efficient in terms of computational
complexity? HINT: You need to be careful to consider the average case for this
problem, not just a trivial case.
6. Assume that you have a datatype called the Clearable type. This data type has a
fixed size list inside it when it is created. So Clearable(10) would create a clearable
list of size 10. Objects of the Clearable type should support an append operation
and a lookup operation. The lookup operation is called __getitem__(item). If cl is
This copy belongs to 'acha04'
2.13 Programming Problems 65
a Clearable list, then writing cl[item] will return the item if it is in the list and return
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
```