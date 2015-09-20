#---------------------------------------------------------
# Jong-Kai Yang
# jong-kai.yang@berkeley.edu
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------
# Imports
# Body
class Node:
    #Constructor Node() creates node
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root = None):
        self.root = root

    # def add(self, word):
    #     if self.root == None:
    #         self.root = Node(word)
    #         return
    #     if word == self.root.word:
    #         self.root.count +=1
    #         return
    #     if word > self.root.word:
    #         if self.root.right == None:
    #             self.root.right = Node(word)
    #         else:
    #             self.add(self.root.right, word)
    #     else:
    #         if self.root.left == None:
    #             self.root.left = Node(word)
    #         else:
    #             self.add(self.root.left, word)

    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)

    def find(self, word):
        return _find(self.root, word)

    def inOrderPrint(self):
        _inOrderPrint(self.root)

    def size(self):
        count = 0
        count = _size(self.root, count)
        print(count)

    def height(self):
        return _height(self.root)


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

def _find(root, word):
    if root.word == word:
        _find_result(root, word, "yes")
        return
    if root.word > word:
        if root.left == None:
            _find_result(root, word, "no")
        else:
            _find(root.left, word)
    elif root.word < word:
        if root.right == None:
            _find_result(root, word, "no")
        else:
            _find(root.right, word)

def _find_result(root, word, result):
    if result == "yes":
        print(str(word) + " appears " + str(root.count) + " times in the tree.")
    else:
        print(str(word) + " is not in the tree.")

def _size(root, count):
    if root == None:
        print("None")
        return count
    print(root.word)
    _size(root.left, count)
    count += 1
    print(count)
    _size(root.right, count)

# def _height(root):



def _inOrderPrint(root):
    if root == None:
        return
    _inOrderPrint(root.left)
    print(str(root.word) + " " + str(root.count))
    _inOrderPrint(root.right)
