balanced binary tree search

1. Write an AVL tree implementation that maintains balances in each node and
implements insert iteratively. Write a test program to thoroughly test your program
on some randomly generated data.

2. Write an AVL tree implementation that maintains balances in each node and
implements insert recursively. Write a test program to thoroughly test your pro-
gram on some randomly generated data.

3. Write an AVL tree implementation that maintains heights in each node and implements insert recursively. Write a test program to thoroughly test your program on
some randomly generated data.

4. Write an AVL tree implementation that maintains heights in each node and implements insert iteratively. Write a test program to thoroughly test your program on
some randomly generated data.

5. Complete programming problem 3. Then implement the delete operation for AVL
Trees. Finally, write a test program to thoroughly test your data structure. As
values are inserted and deleted from your tree you should test your code to make
sure it maintains all heights correctly and the ordering of all values in the tree.

6. Implement two of the programming problems 1–4 in this chapter and then write
a test program that generates a random list of integers. Time inserting the values
into the first implementation and then time inserting each value into the second
implementation. Record all times in the XML format needed by the PlotData.py
program from chapter two. Plot the timing of the two algorithms to compare their
relative efficiency.

7. Write a splay tree implementation with recursive insert and lookup functions.
Implement an AVL tree either iteratively or recursively where the height of each
node is maintained. Run a test where trees are built from the same list of values.
When you generate the list of values, duplicate values should be considered a
lookup. Write the data file with an L or an I followed by a value which indicates
either a lookup or insert operation should be performed. Generate an XML file in
the format used by the PlotData.py program to compare your performance results.

8. Write a splay tree implementation with recursive insert and lookup functions.
Compare it to one of the other balanced binary tree implementations detailed in
this chapter. Run a test where trees are built from the same list of values. When
you generate the list of values, duplicate values should be considered a lookup.
Write the data file with an L or an I followed by a value which indicates either
a lookup or insert operation should be performed. Generate an XML file in the
format used by the PlotData.py program to compare your performance results.

B trees

1. Write a B-Tree class and a B-Tree node class. Implement the insert and delete
algorithms described in this chapter. Implement a lookup method as well. Use
this implementation to efficiently run the join operation presented in Sect. 11.2.7.
Compare the time this algorithm takes to run to the time the non-indexed join,
from Sect. 11.2.5, takes to run. Write the two methods recursively.

2. Write the B-Tree class with iterative, non-recursive, implementations of insert
and delete. In this case the insert and delete methods of the B-Tree class don’t
necessarily have to call insert and delete on B-Tree nodes.

3. Since the example tables in this chapter are rather small, after completing exer-
cise 1 or 2, run the query code again using a dictionary for the index. Compare
the amount of time taken to implement the query in this way with the B-tree
implementation. Comment on the experiment results

Heuristic Search

1. Write a program that uses the five search algorithms in this chapter to search a
maze as shown in the examples. Construct sample mazes by writing a text file
where each space represents an open location in the maze and each non-space
character represents a wall in the maze. Start the maze with the number of rows
and columns of the maze on the first two lines of the file. Assume that you search
the maze from top to bottom to find a way through it. There should be only one
entry and one exit from your maze. Compare and contrast the different algorithms
and their performance on your sample mazes. Be sure to download the maze
searching front-end from the text’s website so you can visualize your results. The
architecture for communication between the front-end and your back-end code
is provided in the front-end program file.

2. Write a program to solve the Knight’s Tour problem. Be sure to use a heuristic in
your search to narrow the search space. Make sure you can solve the tour quickly
for an 8 × 8 board. Draw your solution using turtle graphics.

3. Write a program to solve the N-Queens problem. Use forward checking and a
heuristic to solve the N-Queens problem for an 8 × 8 board. For an extra challenge
try to solve it for a 25 × 25 board. The program will likely need to run for a while (a
half hour?) to solve this one. Be sure to use the N-Queens front-end code provided
on the text’s website to visualize your result. The back-end code you write should
follow the architecture presented at the top of the front-end program file.

4. Write the connect four program to challenge another student’s connect four. You
both must write programs that have a pass button. A flip of a coin can determine
who goes first. The one who goes first should begin by pressing their pass button.
Then you and the other student can flip back and forth while your computer pro-
grams compete. To keep things moving, your game must make a move within 30 s
or it forfeits. You can use the front-end code presented in Sect. 20.6 as your front-
end. You must write the back-end code. Follow the architecture to communicate
with the front-end code presented at the top of the front-end program file.

5. For an extra challenge, write the connect four program and beat the program
provided by the authors on text website. To run the author’s code you must have