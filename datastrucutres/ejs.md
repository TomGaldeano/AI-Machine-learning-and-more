hashmaps

2. Complete the HashSet class found in the chapter by implementing the methods
described in the two tables of set operations. Then, write a main function to test
these operations. Save the class in a file called hashset.py so it can be imported into
other programs. If you call your main function in hashset.py with the if __name__
== “__main__” statement, then when you import it into another program your
hashset.py main function will not be executed, but when you run hashset.py on
its own, its main function will run to test your HashSet class.

3. Memoize the tic tac toe program from Chap. 3 to improve its performance. To do
this each board must have a hash value. You should implement a __hash__ method
for the Board class. The hash value should be unique to a board’s configuration.
In other words, the X’s, O’s, and Dummy objects should factor into the hash
value for the board so that each board has its own unique hash value. Then
memoize the minimax function to remember the value found for a particular
board’s configuration. The minimax function should start by checking whether
or not the value for this board has already been computed and the function should
return it if it has.

4. Write a version of the HashSet class that allows you to specify the maximum and
minimum allowable load factor. Then run a number of tests where you plot the
average time taken to add an item to a set given different maximum load factors.
Also gather information about the average time it takes to test the membership of
an item in a set for different maximum load factors. From this information you
should be able to see some of the space/time trade-off in hash tables. Generate
XML data in the plot format from these experimental results and plot the data to
see what it tells you. From the gathered information, express your opinion about
the optimal load factor for the HashSet class. Comment on the optimal maximum
load factor at the top of the program that performs your tests

trees

Write a program that asks the user to enter a prefix expression. Then, the program
should print out the infix and postfix forms of that expression. Finally, it should
print the result of evaluating the expression. Interacting with the program should
look like this.
Please enter a prefix expression: + + * 4 5 6 7
The infix form is: (((4 * 5) + 6) + 7)
The postfix form is: 4 5 * 6 + 7 +
The result is: 33
If the prefix expression is malformed, the program should print that the expression
is malformed and it should quit. It should not try to print the infix or postfix forms
of the expression in this case.

2. Write a program that reads a list of numbers from the user and lets the user
insert, delete, and search for values in the tree. The program should be menu
driven allowing for inserting, searching, and deleting from a binary search tree.
Inserting into the tree should allow for multiple inserts as follows.
Binary Search Tree Program
--------------------------
Make a choice...
1. Insert into tree.
2. Delete from tree.
3. Lookup Value.
Choice? 1
insert? 5
insert? 2
insert? 8
insert? 6
insert? 7
insert? 9
insert? 4
insert? 1
insert?
Make a choice...
1. Insert into tree.
2. Delete from tree.
3. Lookup Value.
Choice? 3
Value? 8
Yes, 8 is in the tree.
This copy belongs to 'acha04'
6.9 Programming Problems 181
Make a choice...
1. Insert into tree.
2. Delete from tree.
3. Lookup Value.
Choice? 2
Value? 5
5 has been deleted from the tree.
Make a choice...
1. Insert into tree.
2. Delete from tree.
3. Lookup Value.
Choice? 2
Value? 3
3 was not in the tree.
The hardest part of this program is deleting from the tree. You can write a recursive
function to delete a value. In some ways, the delete from tree function is like the
insert function given in the chapter. You will want to write two functions, one that
is a method to call on a binary search tree to delete a value, the other would be a
hidden recursive delete from tree function. The recursive function should be given
a tree and a value to delete. It should return the tree after deleting the value from
the tree. The recursive delete function must be handled in three cases as follows.
• Case 1. The value to delete is in a node that has no children. In this case, the
recursive function can return an empty tree (i.e. None) because that is the tree
after deleting the value from it. This would be the case if the 9 were deleted
from the binary search tree in Fig. 6.12. In Fig. 6.13 the right subtree of the
node containing 8 is now None and therefore the node containing 9 is gone
from the tree.
• Case 2. The value to delete is in a node that has one child. In this case, the
recursive function can return the child as the tree after deleting the value. This
would be the case if deleting 6 from the tree in Fig. 6.13. In this case, to delete
Fig. 6.13 The Tree After Deleting 9
This copy belongs to 'acha04'
182 6 Trees
Fig. 6.14 The Tree After Deleting 6
the node containing 6 from the tree you simply return the tree for the node
containing 7 so it ends up being linked to the node containing 8. In Fig. 6.14
the node containing 6 is eliminated by making the left subtree of the node
containing 8 point at the right subtree of the node containing 6.
• Case 3. This is is hardest case to implement. When the value to delete is in
a node that has two children, then to delete the node we want to use another
function, call it getRightMost, to get the right-most value of a tree. Then you
use this function to get the right-most value of the left subtree of the node to
delete. Instead of deleting the node, you replace the value of the node with the
right-most value of the left subtree. Then you delete the right-most value of
the left subtree from the left subtree. In Fig. 6.15 the 5 is eliminated by setting
the node containing 5 to 4, the right-most value of the left subtree. Then 4 is
deleted from the left subtree.
Fig. 6.15 The Tree After Deleting 5

3. Complete the Sudoku program as described in Chap. 5 and augment it with the
depth first search described in Sect. 6.6.2 to complete a Sudoku program that
is capable of solving any Sudoku puzzle. It should solve these puzzles almost
instantly. If it is taking a long time to solve a puzzle it is likely because your
reduce function is not reducing the puzzle as described in Chap. 5.
To complete this exercise you will need two functions, the solutionOK func-
tion and the solutionViable function. The solutionViable function is given in the
chapter and returns True if none of the sets in the matrix are empty. The solutionOK
function returns True if the solution is a valid solution. This can be checked very
easily. If any of the sets in the matrix do not contain contain exactly 1 element
then the solution is not okay and False should be returned. If the union of any
group within a Sudoku puzzle does not contain 9 elements then the solution is
not okay and False should be returned. Otherwise, the solution is okay and True
should be returned.
After completing this program you should be able to solve Sudoku problems like
sudoku7.txt or sudoku8.txt which are available for download on the text’s website.

4. Design an OrderedTreeSet class which can be used to insert items, delete items,
and lookup items in an average case of O(log n) time. Implement the in operator
on this class for set containment. Also implement an iterator that returns the items
of the set in ascending order. The design of this set should allow items of any
type to be added to the set as long as they implement the __lt__ operator. This
OrderedTreeSet class should be written in a file called orderedtreeset.py. The main
function of this module should consist of a test program for your OrderedTreeSet
class that thoroughly tests your code. The main function should be called using
the standard if statement that distinguishes between the module being imported
or run itself.

5. Design an OrderedTreeMap class which uses an OrderedTreeSet class in its
implementation. To organize this correctly you should create two modules: an
orderedtreeset.py module and an orderedtreemap.py module. Have the Ordered
TreeMap class use the OrderedTreeSet class in its implementation the way Hash-
Set and HashMap were implemented in Chap. 5. Design test cases to thoroughly
test your OrderedTreeMap class.

graphs

1. Go to the text website and download the dictionary of words. Build a bloom filter
for this list of words and use it to spellcheck the declaration of independence,
printing all the misspelled words to the screen.

2. Go to the text website and download the dictionary of words. Build a trie datatype
for this list of words and use it to spellcheck the declaration of independence,
printing all misspelled words to the screen.

3. Create a trie as in the previous exercise, but also print suggested replacements for
all misspelled words. This is a tough assignment. Suggested replacements should
not differ from the original in more than one of the ways suggested in the chapter.

heaps

1. Implement version 2 of the heapsort algorithm. Run your own tests using heapsort
and quicksort to compare the execution time of the two sorting algorithms. Output
your data in the plot format and plot your data using the PlotData.py program
provided on the text website.

2. Implement version 1 and version 2 of the program and compare the execution
times of the two heapsort variations. Gather experimental data in the XML format
accepted by the PlotData.py program and plot that data to see the difference
between using version 1 and version 2 of the heap sort algorithm.

3. Implement a smallest on top heap and use it in implementing a priority queue. A
priority queue has enqueue and dequeue methods. When enqueueing an item on
a priority queue, a priority is provided. Elements enqueued on the queue include
both the data item and the priority. Write a test program to test your priority queue
data structure.

4. Use the priority queue from the last exercise to implement Dijkstra’s algorithm
from Chap. 7. The priority queue implementation of Dijkstra’s algorithm is more
efficient. The priority of each element is the cost so far of each vertex added
to the priority queue. By dequeueing from the priority queue we automatically
get the next lowest cost vertex from the queue without searching, resulting in a
O(|V |log|V |) complexity instead of O(|V |2).

5. Use the heapsort algorithm, either version 1 or version 2, to implement Kruskal’s
algorithm from Chap. 7. Use one of the sample graph XML files found on the text
website as your input data to test your program.

balanced binary tree search
1. Write an AVL tree implementation that maintains balances in each node and
implements insert iteratively. Write a test program to thoroughly test your program
on some randomly generated data.

2. Write an AVL tree implementation that maintains balances in each node and
implements insert recursively. Write a test program to thoroughly test your pro-
gram on some randomly generated data.

3. Write an AVL tree implementation that maintains heights in each node and imple-
ments insert recursively. Write a test program to thoroughly test your program on
some randomly generated data.

4. Write an AVL tree implementation that maintains heights in each node and imple-
ments insert iteratively. Write a test program to thoroughly test your program on
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