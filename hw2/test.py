#---------------------------------------------------------
# Jong-Kai Yang
# jong-kai.yang@berkeley.edu
# Homework #2
# September 15, 2015
# test.py
# test
#---------------------------------------------------------

from BST import *
from hw2 import *

T = BSTree()
T.add("batman")
T.add("forreal?")
T.add("daniel")
T.add("kahnneman")
T.add("leroyJenkins")
T.add("sodaHall")
T.add("april")
T.add("hello")
T.add("goodbye")
T.add("april")
T.add("summer")
T.add("april")
T.add("goodbye")
T.add("hello")
T.add("summer")
T.add("summer")
T.add("summer")

F = load_file()
L = word_process(F)
for word in L:
    T.add(word)

T.inOrderPrint()
T.size()
T.height()
T.find("summer")


# T.find("april")
# T.find("hello")
# T.find("goodbye")
# T.find("shit")
