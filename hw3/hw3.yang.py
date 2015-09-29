#Imports
import urllib2
import re
import operator
#Body
def ReadCatalogue(filename):
    raw_catalog = open(filename, 'r').readlines()
    Books = {}
    Titles = []
    for index, book in enumerate(raw_catalog):
        if book != "\r\n" and book != "\n" and book != "\r":
            titleInfo = raw_catalog[index].split(",")
            Books[titleInfo[0]] = [index, titleInfo[1].rstrip('\r\n')]
            Titles.append(titleInfo[0])
    return (Books, Titles)


def word_process(word):
    char_holder = ""
    for char in word:
        if ord(char) > 96 and ord(char) < 123:
            char_holder += char
    return char_holder


def UpdateWords(word, bookIndex, WordCounts, Words):
    if Words.has_key(word):
        Words[word][bookIndex] = Words[word][bookIndex] + 1
    else:
        count = []
        for i in range(WordCounts):
            count.append(0)
        Words[word] = count
        Words[word][bookIndex] = 1
    return Words


def ReadBook(Titles, Books, Words):
    WordCounts = len(Titles)
    for book in Titles:
        bookIndex = Books[book][0]
        bookUrl = Books[book][1]
        try:
            raw_content = urllib2.urlopen(bookUrl).read().lower().split()
            for word in raw_content:
                if not word.rstrip('\r\n').isdigit():
                    UpdateWords(word_process(word), bookIndex, WordCounts, Words)
        except Exception:
            print("oops, the url of " + book + " seems broken.")
    return Words


def PrintAnswer(query, index, order, Titles, Books):
    if order[1] > 1:
        print(str(index+1) + ".  The word " + query + " appears " + str(order[1]) + " times in " + Titles[order[0]] + " (link:  " + Books[Titles[order[0]]][1] + ")")
    elif order[1] == 1:
        print(str(index+1) + ".  The word " + query + " appears " + str(order[1]) + " time in " + Titles[order[0]] + " (link:  " + Books[Titles[order[0]]][1] + ")")


def Search(Words, Books, Titles):
    while True:
        query = raw_input("Search Terms? ")
        if query == "<terminate>":
            break
        elif query == "<catalog>":
            for index,i in enumerate(Titles):
                print(Books.items()[index][0]),
                print(":"),
                print(Books.items()[index][1])
        elif query =="<titles>":
            for i in Titles:
                print(i)
        elif not Words.has_key(query):
            print("The word " + query + " does not appear in any books in the library")
        else:
            ref = sorted(enumerate(Words[query]), key=operator.itemgetter(1), reverse=True)
            for index,order in enumerate(ref):
                PrintAnswer(query, index, order, Titles, Books)


# Main
def main():
    Catalogue = ReadCatalogue("hw3localcatalog.txt")
    Books = Catalogue[0]
    Titles = Catalogue[1]
    Words = {}
    Words = ReadBook(Titles, Books, Words)
    Search(Words, Books, Titles)


if __name__ == "__main__":
    main()
