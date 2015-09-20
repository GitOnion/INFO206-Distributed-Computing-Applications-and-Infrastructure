#---------------------------------------------------------
# <NAME>
# <EMAIL>
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------


class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right = None
        self.left = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root
    
    #These are "external functions" that will be called by your main program - I have given these to you =)
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)
    
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    #Print in order entire tree
    def inOrderPrint(self):
        _inOrderPrint(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)


#These are "internal functions" in the BSTree class - You need to create these!!!

#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count +=1
        return
    if root.word > word:
        if root.left == None:
            root.left = Node(word)
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word)
        else:
            _add(root.right, word)
    
#Function to find word in tree
def _find(root, word):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE

#Get number of nodes in tree
def _size(root):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE

#Get height of tree
def _height(root):
    #YOU FILL THIS IN
    self.placeholder = None #REMOVE
    
#Function to print tree in order
def _inOrderPrint(root):
    if not root:
        return
    _inOrderPrint(root.left)
    print root.word
    print root.count
    _inOrderPrint(root.right)
