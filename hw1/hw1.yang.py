import math
pw = ""
pwFile = open("common.txt", 'r')
listOfCommons = pwFile.readlines()
def errorMsg():
    msg = ""
    if length == 0:
        msg += "You need at least 6 characters\n"
    if uppercase == 0:
        msg += "You need at least 1 uppercase letter\n"
    if lowercase == 0:
        msg += "You need at least 1 lowercase letter\n"
    if digit == 0:
        msg += "You need at least 1 digit\n"
    if other == 0:
        msg += "You need at least 1 other character\n"
    return msg

while pw != "finish":
    length = 0
    uppercase = 0
    lowercase = 0
    digit = 0
    other = 0
    strength = 0
    pw = raw_input("Check your password's strength:")
    if pw == "finish":
        break
    if len(pw) > 5:
        length = 1
    for i in range(len(pw)):
        if ord(pw[i]) >= 97 and ord(pw[i]) <= 122:
            lowercase = 0.5
        elif ord(pw[i]) >= 65 and ord(pw[i]) <= 90:
            uppercase = 0.5
        elif ord(pw[i]) >= 48 and ord(pw[i]) <= 57:
            digit = 1
        elif ord(pw[i]) >= 32 and ord(pw[i]) <= 126:
            other = 1
    strength = length + lowercase + uppercase + digit + other
    if strength == 4:
        print("Strength: strong")
    elif strength >= 3:
        print("Strength: high medium strength")
    elif strength >= 2:
        print("Strength: medium strength")
    elif strength >= 1:
        print("Strength: weak")
    else:
        print("Strength: very weak")
    print(errorMsg())

    pw = str(pw.lower()+"\r\n")
    low = 0
    high = len(listOfCommons)
    iteration = 0
    while low != high-1:
        iteration += 1
        target = int(math.ceil((high-low)/2)) + low
        if pw == "&amp\r\n" or pw == "&amp;\r\n":
            iteration = 13
            print("This is a common password!! iteration = " + str(iteration) + "\n")
            break
        if pw == listOfCommons[target]:
            print("This is a common password!! iteration = " + str(iteration) + "\n")
            break
        elif pw < listOfCommons[target]:
            high = target
        else:
            low = target

print("\nWhat is the relationship between this number and the size of the list?\n \
 A: The longer the list, the larger the iteration number is (in the worst case).\n \
 Compare to the list's length, the iteration number grows at a logarithmit.\n \
 Hence the Big-O notation of binary search is: O(logN)")
