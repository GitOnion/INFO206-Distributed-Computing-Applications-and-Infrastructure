#---------------------------------------------------------
# Jong-Kai Yang
# jong-kai.yang@berkeley.edu
# Homework #2
# September 15, 2015
# hw2.py
# Main
#---------------------------------------------------------
# Imports
from BST import *

# Body
def load_file():
    text_file = False
    while text_file == False:
        file_name = raw_input("Please enter the name of the file to read: ")
        try:
            text_file = open(file_name, 'r')
            return text_file
        except Exception:
            print("sorry, no such file, try again!")

def word_process(txtfile):
    text_read = txtfile.read()
    text_lower = text_read.lower()
    text_split = text_lower.split()
    text_processed = []
    for word in text_split:
        char_holder = ""
        for char in word:
            if ord(char) == 32 or (ord(char) > 96 and ord(char) < 122):
                char_holder += char
        text_processed.append(char_holder)
    print(text_processed)
    return text_processed

# main function
def main():
    t = load_file()
    word_process(t)


if __name__ == "__main__":
    main()
