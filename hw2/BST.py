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
    def __init__(self, word, height):
        self.word = word
        self.left = None
        self.right = None
        self.count = 1
        self.height = height

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
            self.root = Node(word, 0)
            return
        height = 0
        _add(self.root, word, height)

    def find(self, word):
        return _find(self.root, word)

    def inOrderPrint(self):
        _inOrderPrint(self.root)

    def size(self):
        count = 0
        count = _size(self.root, count)
        print("The number of entries in the tree is: " + str(count))

    def height(self):
        holder = []
        _height(self.root, holder)
        print("The height of the tree is: " + str(max(holder)))


def _add(root, word, height):
    if root.word == word:
        root.count +=1
        return
    if root.word > word:
        height += 1
        if root.left == None:
            root.left = Node(word, height)
        else:
            _add(root.left, word, height)
    else:
        height += 1
        if root.right == None:
            root.right = Node(word, height)
        else:
            _add(root.right, word, height)

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
        return count
    else:
        count += 1
    count = _size(root.left, count)
    count = _size(root.right, count)
    return count

def _height(root, holder):
    if root == None:
        return
    else:
        holder.append(root.height)
        _height(root.left, holder)
        _height(root.right, holder)
    return holder

def _inOrderPrint(root):
    if root == None:
        return
    _inOrderPrint(root.left)
    # test = open("log.txt", "a")
    # print >> test, (str(root.word) + " " + str(root.count))
    # test.close()
    print(str(root.word) + ": count = " + str(root.count) + ", height = " + str(root.height))
    _inOrderPrint(root.right)
