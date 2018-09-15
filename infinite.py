import math




#finds the total elements in a 2dlist
def lengthFinder(listA):
    length = 0
    for i in range(len(listA)):
        for j in range(len(listA[i])):
            length+=1
    return length

####################################################################################
# Function: To add two 2dlists that have been padded with 0's in the front if they are not of equal length.
#           The numbers are added from the right most digit to the left index by index. Assume that the lists have
#           both been manipulted by the method zeroPad
#
#
# listA; 2dlist that represents the number, where each element in the list represents a node of size nodeSize
# listB; 2dlist, same as above, represents the second number
# listC; a passed in list that keeps the running total of the numbers added; initiialize to empty list
# whichNode; keeps track of which node we are currently in during the adding process; initialized to the right most
#            list which is denoted by ceil(len(numberAsString) / nodeSize)
# numberInNode; keeps track of which index of the nodes we are adding, initialize to the right most index in the node
#           denoted by len(listA[0])
# nodeSize; denotes the size of the nodes we break the number into, given by command line argument
# carryOver; represents the number that is carried over from adding. Initialize to 0. for example 9+9, the carry
#            over is 1 calculated by (9+9)//10 and the modulus represents the remainder (9+9) % 10
####################################################################################
def recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize, carryOver):
    if(whichNode == -1):
        #print("if")
        listC.insert(0,carryOver)
        return
    elif(whichNode > -1 and numberInNode > -1):

        #print("elif1")
        #print(whichNode, numberInNode)

        toInsert = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode]) % 10 + carryOver
        #print(toInsert)
        #print(carryOver)
        carryOver =(listA[whichNode][numberInNode] + listB[whichNode][numberInNode])//10
        #print(carryOver)
        numberInNode-=1
        listC.insert(0, toInsert)
        #print(listC)
        recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize, carryOver)
    elif(whichNode >= -1 and numberInNode == -1):
        #print("elif2")
        whichNode-=1
        numberInNode = len(listA[0])-1
        #print(whichNode, numberInNode)
        if(whichNode == -1):
            recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize, carryOver)
        else:
            #print(whichNode, numberInNode)
            toInsert = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode]) % 10 + carryOver
            carryOver = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode])//10
            listC.insert(0,toInsert)
            print(listC)
            numberInNode -=1
            recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize, carryOver)





####################################################################################
# Function: To generate a 2d list from a string that represents a large number.
#           The number is broken into nodes of size nodeSize, where each index of the
#           list will represent a slice of the total string. Start from the left hand side
#           of the string and insert from the left hand side of the 2dlist. Uncomment print
#           to see how this works
#
# theString; The string the represents the very large number, passed in from file
# nodeSize; The size of the nodes given by the command line arguemnt
# numberInNode; keeps track of which index in the nodes we are in, initialize to 0.
#               used as a way to know when a node is full, and move on to the next node
# whichNode; keeps track of which node we are inserting number in
# listOfLists; a 2dlist where n = ceil( len(theString) / nodeSize), then there are n empty
#               lists within listOfLists
# i; used to traverse the string and keep track of which element we are appending to the node
#

####################################################################################
def recNodeBreak(theString, nodeSize, numberInNode, whichNode, listOfLists, i):
    if(len(theString) == 1):
        #print("if")
        listOfLists[whichNode].insert(0,(int(theString[i])))
        return listOfLists

    elif(i == -1):
        #print("elif")
        #print(listOfLists)
        return listOfLists

    elif(i > -1 and numberInNode < nodeSize):
        #print("elif2")
        listOfLists[whichNode].insert(0, (int(theString[i])))
        #print(listOfLists)
        recNodeBreak(theString, nodeSize, numberInNode+1, whichNode, listOfLists, i-1)

    elif(i > -1 and numberInNode == nodeSize):
        #print("elif3")

        whichNode-=1
        numberInNode = 0
        listOfLists[whichNode].insert(0,(int(theString[i])))
        #print(listOfLists)
        recNodeBreak(theString, nodeSize, numberInNode+1, whichNode, listOfLists, i-1)

####################################################################################
# Function: To ensure that both lists are of equal size, and that all nodes are filled.
#           This is done by either inserting empty list's and padding them with zero's,
#           padding nodes that are not of size nodeSize with zero's or both.
#
#
# whichNode; keeps track of which node we are inserting number in
#
#

####################################################################################


def zeroPad(whichNode, nodeSize, listA, listB):
    if(len(listA) == len(listB) and whichNode == len(listA)):
        #print("if")
        return

    #inserts empty 2dlists are not of equal length
    elif(len(listA) != len(listB)):
        #print("elif1")
        if(len(listA) < len(listB)):
            listA.insert(0, [])
            zeroPad(whichNode, nodeSize, listA, listB)
        else:
            listB.insert(0,[])
            zeroPad(whichNode, nodeSize, listA, listB)

    elif(len(listA[whichNode]) < nodeSize or len(listB[whichNode]) < nodeSize):
        #print("elif2", whichNode)
        #print(listA)
        #print(listB)

        if(len(listA[whichNode]) < nodeSize):
            #print("elif2 if")

            listA[whichNode].insert(0,0)
            #print(listA)
            zeroPad(whichNode, nodeSize, listA, listB)
        else:
            #print("elif2 else")

            listB[whichNode].insert(0, 0)
            #print(listB)
            zeroPad(whichNode, nodeSize, listA, listB)

    elif (len(listA[whichNode]) == nodeSize and len(listB[whichNode]) == nodeSize):
        #print("elif3")

        whichNode +=1
        zeroPad(whichNode, nodeSize, listA, listB)

def destroyLeadingZero(listA):
    if(listA[0] != 0):
        return
    else:
        del listA[0]
        destroyLeadingZero(listA)

def printAsString(listA, i, listALen, returnedString):
    if(i < listALen):
        print("if")
        print(returnedString)

        returnedString = str(listA[i]) + printAsString(listA, i+1, listALen, returnedString)
    elif(i == listALen):
        print("elif")
        done = ""
        return done

def recToString(listC, listLen, i):
    if(i == listLen-1):
        #print(i)
        theReturnedString = listC[i]
        #print(theReturnedString)
        return str(theReturnedString)
    elif(i < listLen):
        #print(i)
        theReturnedString = listC[i]
        #print(theReturnedString)
        return str(theReturnedString) + recToString(listC, listLen, i+1)


def toMultiply(listA, listB, listC):
    return


#######################################################
#
# main
#
#######################################################

#The nodeSize across all functions MUST be the same, it will be given and parsed from the cmd lin arg
#myString and myString1 will be the two numbers represented as numbers, we must parse these from the file

###########
#
# initialize list 1
#
###########
#Initialize driver variables
print("Here are the strings represented as 2dLists")
myString = "992349"
nodeSize = 3
numberInNode = 0
whichNode = (math.ceil(len(myString)/nodeSize))-1
#Initialize a 2dList, create another variable called numberOfNodes for ease of use
numberOfNodes = (math.ceil(len(myString)/nodeSize))
listOfLists = [0]*(numberOfNodes)
for i in range(numberOfNodes):
    listOfLists[i] = []
i = len(myString)-1
#this is the recursion driver method, uncommet the prints in the method to show the process
recNodeBreak(myString, nodeSize, numberInNode, whichNode, listOfLists, i)
print(listOfLists)



###########
#
# initialize list2
#
###########
#Initialize driver variables
myString1 = "999912"
nodeSize1 = 3
numberInNode1 = 0
whichNode1 = (math.ceil(len(myString1)/nodeSize1))-1
#Initialize a 2dList, create another variable called numberOfNodes for ease of use
numberOfNodes1 = (math.ceil(len(myString1)/nodeSize1))
listOfLists2 = [0]*(numberOfNodes1)
for i in range(numberOfNodes1):
    listOfLists2[i] = []
i1 = len(myString1)-1
#this is the recursion driver method, uncommet the prints in the method to show the process
recNodeBreak(myString1, nodeSize1, numberInNode1, whichNode1, listOfLists2, i1)
print(listOfLists2)


###########
#
# pad lists with zeros
#
###########
print("here are the lists padded with zero's:")
thisNode = 0
nodeSize = 3
#zeroPad(whichNode, nodeSize, listA, listB)
zeroPad(thisNode,nodeSize, listOfLists, listOfLists2 )
print(listOfLists2)
print(listOfLists)




###########
#
# add two lists
#
###########
#recAdd(listA, listB, listC, whichNode, numberInNode, nodeSize):
print("here is the result of adding the two lists: ")
listC = []
nodeSize = len(listOfLists[0])
whichNoderecAdd = max(len(listOfLists), len(listOfLists2))-1
numberInNoderecAdd = len(listOfLists[0])-1
carryOver = 0
recAdd(listOfLists, listOfLists2, listC ,whichNoderecAdd,numberInNoderecAdd , nodeSize, carryOver)
print(listC)



###########
#
# delete the leading zero's
#
###########
print("Here is the list with no leading zero's")
destroyLeadingZero(listC)
print(listC)


stringV = ""
i = 0
listCLength = len(listC)
#def printAsString(listA, i, listALen, returnedString):

#stringNew = printAsString(listC, i, listCLength, stringV)

#print(stringNew)
#recToString(listC, listLen, i, theReturnedString)
print("Here is the number converted back to a string")
print(recToString(listC, len(listC), 0))

