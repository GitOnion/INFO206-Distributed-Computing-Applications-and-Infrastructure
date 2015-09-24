#---------------------------------------------------------
# Jong-Kai Yang
# jong-kai.yang@berkeley.edu
# Homework #2
# September 15, 2015
# README.txt
# Read me
#---------------------------------------------------------

Test Case & Strategy:

1. Use the default test case given in the test.py
2. Alter the order of the test cases to see if the tree prints out differently.
3. Add more cases to see make sure the add, height, size, and find work properly.
4. Use the test_file.txt and save the output into a text file, examine the output and check the stats.

Questions:
(1) For the file http://www.gutenberg.org/cache/epub/1342/pg1342.txt what is the depth of your tree?
    What does that say about the number of operations to find a word?
A:  The depth is 28 (total 29, but the root start with 0).
    This means that the search for any words in the tree should not exceed 29 times.

(2) What would happen if the input to your program were sorted (as it was in HW 1)?
A:  The depth of the tree will be larger (the tree is more unbalanced), and the maximum search time
    will increase.

(3) What are applications for binary search tree?  In what ways are they superior to lists?  In what
    ways are they inferior to lists?
A:  Applications for BST could be implementing a fast search on any random data. It is faster (or
    equal to, in the worst case) to search through a BST than through a list, while it is slower to
    insert or delete an element than on a list.

(4) Did you implement the extra credit (listed below)?
A:  No.
