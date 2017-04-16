# The Enigma Cipher
# Himanshu Sharma

import os
os.system('title The Enigma Machine')
L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


def shuffle(l, first):
    tempList = []
    for j in range(len(l)):
        if l[0] == first:
            break
        else:
            i = l[0]
            l.remove(i)
            tempList.append(i)

    return l+tempList

def shuffleRight(l, last):

    tempList = []
    for j in range(len(l)):
        if l[len(l)-1] == last:
            break
        else:
            i = l[len(l)-1]
            l.remove(i)
            tempList.append(i)
    rev = []
    for q in range(-1, -len(tempList)-1, -1):
        rev.append(tempList[q])
##        print rev
    return rev + l
    
def shiftOneIndex(l, direction = "Left"):

    if direction == "Left":
        return shuffle(l, l[1])
    else:
        return shuffleRight(l, l[len(l)-2])
    
    
def enigma():
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    msg = raw_input("Enter a message: ")
    MSG = msg.upper()
    key_setting = raw_input("Enter a key setting: ").upper()
    #key_setting = key.upper()

    word1, word2, word3 = key_setting[0], key_setting[1], key_setting[2]
    
    l1 = shuffle(L, word1)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l2 = shuffle(L, word2)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l3 = shuffle(L, word3)

##    standardMoves = len(msg)/4
##    
##    rotor1moves = len(msg) #times
##    rotor2Moves = standardMoves #times
##    rotor3Moves = standardMoves/4 #times
##    
    count_for_rotor1, count_for_rotor2, count_for_rotor3 = 0, 0, 0
    code = ''

    for i in MSG:
        if i in l1:
            if count_for_rotor1 == 0 or count_for_rotor1 % 4 <> 0:
                ind = l1.index(i)

                code += l3[ind]
            else:
                l2 = shiftOneIndex(l2)
                count_for_rotor2 += 1


                if count_for_rotor2 % 4 == 0:
                    
                    l3 = shiftOneIndex(l3)
                    count_for_rotor3 += 1
                    ind = l1.index(i)

                    code += l3[ind]
                else:
                    ind = l1.index(i)

                    code += l3[ind]
            count_for_rotor1 += 1
            l1 = shiftOneIndex(l1)
        else:
            code += i

    print code
                
def decipher():

    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    code = raw_input("Enter the enigma code: ")
    key = raw_input("Enter the key settings: ")
    code = code.upper()
    internal_key = key[-1:-len(key)-1:-1].upper()
    
    word1, word2, word3 = internal_key[0], internal_key[1], internal_key[2]

    
    l1 = shuffle(L, word1)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l2 = shuffle(L, word2)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l3 = shuffle(L, word3)

    count_for_rotor1, count_for_rotor2, count_for_rotor3 = 0, 0, 0

    for i in code:
        if i in l1:
            if count_for_rotor1 == 0 or count_for_rotor1 % 4 <> 0:
                ind = l1.index(i)

                print l3[ind],
            else:
                l2 = shiftOneIndex(l2, "Right")
                count_for_rotor2 += 1


                if count_for_rotor2 % 4 == 0:
                    
                    l3 = shiftOneIndex(l3, "Right")
                    count_for_rotor3 += 1
                    ind = l1.index(i)

                    print l3[ind],
                else:
                    ind = l1.index(i)

                    print l3[ind],
            count_for_rotor1 += 1
            l1 = shiftOneIndex(l1, "Right")
        else:
            print i,
            

print "Type 'help' to know all commands."


def enigma__(key, address):

    f = open(address, 'r')
    s = f.read().upper()
    f.close()
    f1 = open('temp.txt', 'w')
    f1.write(s+'\nCREDITS ENIGMA MACHINE')
    f1.close()
    f2 = open('temp.txt', 'r')
    S = f2.read()
    f2.close()
    os.remove('temp.txt')
    MSG = S
    key_setting = key.upper()

    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    word1, word2, word3 = key_setting[0], key_setting[1], key_setting[2]
    
    l1 = shuffle(L, word1)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l2 = shuffle(L, word2)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l3 = shuffle(L, word3)

##    standardMoves = len(msg)/4
##    
##    rotor1moves = len(msg) #times
##    rotor2Moves = standardMoves #times
##    rotor3Moves = standardMoves/4 #times
##    
    count_for_rotor1, count_for_rotor2, count_for_rotor3 = 0, 0, 0

    code = ''
    for i in MSG:
        if i in l1:
            if count_for_rotor1 == 0 or count_for_rotor1 % 4 <> 0:
                ind = l1.index(i)

                code += l3[ind]
            else:
                l2 = shiftOneIndex(l2)
                count_for_rotor2 += 1


                if count_for_rotor2 % 4 == 0:
                    
                    l3 = shiftOneIndex(l3)
                    count_for_rotor3 += 1
                    ind = l1.index(i)

                    code += l3[ind]
                else:
                    ind = l1.index(i)

                    code += l3[ind]
            count_for_rotor1 += 1
            l1 = shiftOneIndex(l1)
        else:
            code += i

    return code

def decipher__(key, address):
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    f = open(address, 'r')
    s = f.read().upper()
    f.close()

    code = s

    internal_key = key[-1:-len(key)-1:-1].upper()

    word1, word2, word3 = internal_key[0], internal_key[1], internal_key[2]

    
    l1 = shuffle(L, word1)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l2 = shuffle(L, word2)
    L = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    l3 = shuffle(L, word3)

    count_for_rotor1, count_for_rotor2, count_for_rotor3 = 0, 0, 0
    decoded = ''
    for i in code:
        if i in l1:
            if count_for_rotor1 == 0 or count_for_rotor1 % 4 <> 0:
                ind = l1.index(i)

                decoded += l3[ind]
            else:
                l2 = shiftOneIndex(l2, "Right")
                count_for_rotor2 += 1


                if count_for_rotor2 % 4 == 0:
                    
                    l3 = shiftOneIndex(l3, "Right")
                    count_for_rotor3 += 1
                    ind = l1.index(i)

                    decoded += l3[ind]
                else:
                    ind = l1.index(i)

                    decoded += l3[ind]
            count_for_rotor1 += 1
            l1 = shiftOneIndex(l1, "Right")
        else:
            decoded += i
    return decoded
    

def whatisenigmamachine():

    f = open("About.txt", "r")
    s = f.read()
    print s
    f.close()

def bruteforce(address):

    d = {1: '0', 2: '1', 3: '2', 4: '3', 5: '4', 6: '5', 7: '6', 8: '7', 9: '8', 10: '9', 11: 'A', 12: 'B', 13: 'C', 14: 'D', 15: 'E', 16: 'F', 17: 'G', 18: 'H', 19: 'I', 20: 'J', 21: 'K', 22: 'L', 23: 'M', 24: 'N', 25: 'O', 26: 'P', 27: 'Q', 28: 'R', 29: 'S', 30: 'T', 31: 'U', 32: 'V', 33: 'W', 34: 'X', 35: 'Y', 36: 'Z'}
    for i in range(1, 37):
        for j in range(i, 37):
            for q in range(1, 37):
                l = [d[i], d[j], d[q]]
                key = ''
                for k in l:
                    key += k
                #print key

                decode = decipher__(key, address)

                if 'ENIGMA' in decode:
                    return key
                else:
                    pass
                del key

    

def run():


    x = raw_input("\n>>> ")

    if x == "enigma":
        enigma()
    elif x == "decipher":
        decipher()
    elif x == "q":
        quit()
    elif x == "about":
        whatisenigmamachine()
    elif x[0:7] == "enigma ":
        c = enigma__(x[7: 10], x[11:])
        print c
    elif x[0:9] == "decipher ":
        d = decipher__(x[9:12], x[13:])
        print d
    elif x[0:11] == "bruteforce ":
        revealed_key = bruteforce(x[11:])
        if revealed_key == None:
            print "Sorry Himanshu!!"
            print "Unable to bruteforce "+x[11:]+"."
        else:
            print "Welcome Himanshu!!"
            print "The alternative key for the file "+x[11:]+" is "+revealed_key+"."
    elif x == "help":
        print
        print "Type 'enigma' to encipher your text in enigma code."
        print "Type 'decipher' to decipher your enigma code."
        print "Type 'q' to close enigma machine."
        print "Type 'about' to know what is enigma machine and its history."
        print "Type 'enigma <key> <address of text file>' to code your text file in enigma."
        print "Type 'decipher <key> <address of coded file>' to decode your text file to normal text."
        print 
        print "You will be asked for a key while enciphering and deciphering. This key must be alphanumeric and must be of length 3. Otherwise enigma machine will not work."
        print
        print "Note that there is no feature to save a generated code or your decoded text. You must copy and paste the result in a proper editor to save your data."
    elif x == '':
        pass
    else:
        print "Invalid Command!!"

    run()

run()
