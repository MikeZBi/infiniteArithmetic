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

        toInsert = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver) % 10
        #print(toInsert)
        #print(carryOver)
        carryOver =(listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver)//10
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
            toInsert = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver) % 10
            carryOver = (listA[whichNode][numberInNode] + listB[whichNode][numberInNode] + carryOver)//10
            listC.insert(0,toInsert)
            #print(listC)
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













# assume listA is the longer list
# assume listB is the shorter list
# for now lets jsut consider that list A and B are of same length, and we padded them with 0's
# whichNodeA is set to len(listA)-1
# whichNodeB is set to len(listB)-1
# indexA, indexB; initially set to nodeSize

#listC must be of size listA + n * len(listB)-1, intialize to all 0's
#need some indexC to keep track of which index in listC, initialize i to the last element in listC as first
#then when we finish up an index in B, change i to be the len(listC)-2 and then -3 (in the recursion this will just be indexC-1

#also need a carryOver for adding, called carryOverAdd, initially set to 0


#for now i have a list of 0's so we need to make sure the first if statement is interting into the correct place
def toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, indexC, carryOver, carryOverAdd, n):
    if(whichNodeA == 0 and whichNodeB == 0 and indexA == 0 and indexB == 0):
        print("if")
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10
        #listC.insert(0, toInsert)
        print("this is the value to insert", toInsert)
        print("value of carryOver", carryOver)
        print("value of carryOverAdd", carryOverAdd)
        toAdd = listC[indexC]
        print("value of listC: " , listC)
        print("value of indexC", indexC)
        print("value of listC at indexC", listC[indexC])
        listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10

        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10
        print("value of carryOverAdd", carryOverAdd)
        listC[indexC-1] = carryOverAdd + carryOver




    #for some list B with one node and one item, and be able to multiply through listA that has one node and many items
    elif(whichNodeB >= 0 and indexB >= 0 and whichNodeA > -1 and indexA > 0 and indexC >= 0):
        print("elif1: traversing the current node")
        print("here is indexC", indexC, " and value at indexC", listC[indexC])
        print("which NodeA:", whichNodeA, "which indexA: ", indexA, " number mult: ", listA[whichNodeA][indexA])
        print("which NodeB:", whichNodeB, "which indexB: ", indexB, " n mult: ", listB[whichNodeB][indexB])
        print("current carry over: ", carryOver)
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB]+carryOver) // 10
        print("new carry over: ", carryOver)
        print("number toInsert: ", toInsert)
        #listC.insert(0, toInsert)
        toAdd = listC[indexC]
        listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        print("number in listC: ", listC[indexC])
        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10
        print("carryOverAdd: ", carryOverAdd)
        print("numbers in listC: ", listC)

        toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA-1, indexB, indexC-1, carryOver, carryOverAdd,n)


    #this is to loop through nodes in listA
    elif (whichNodeB >= 0 and indexB >= 0  and whichNodeA > 0 and indexA == 0):
        print("elif2: the max of a node has been reached, we multiplying the last index of current node")
        print("then after this, we should have changed to the next node of listA")
        print("which NodeA:", whichNodeA, "which indexA: ", indexA, " number mult: ", listA[whichNodeA][indexA])
        print("which NodeB:", whichNodeB, "which indexB: ", indexB, " n mult: ", listB[whichNodeB][indexB])

        print("current carry over: ", carryOver)
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] +carryOver)% 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10
        print("new carry over: ", carryOver)
        print("number toInsert: ", toInsert)
        print("value of index C" ,indexC)

        toAdd = listC[indexC]
        listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        print("number in listC: ", listC[indexC])
        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10
        print("carryOverAdd: ", carryOverAdd)

        whichNodeA-= 1
        indexA = len(listA[whichNodeA])-1
        # if(whichNodeA == -1 and indexA == 1 and carryOver != 0):
        #     print("elif2 if")
        #     listC.insert(indexC, carryOver)
        #     carryOver = 0

        print("numbers in listC", listC)
        print("which NodeA:", whichNodeA, "which indexA: ", indexA, " number mult: ", listA[whichNodeA][indexA])
        print("which NodeB:", whichNodeB, "which indexB: ", indexB, " n mult: ", listB[whichNodeB][indexB])
        toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, indexC-1, carryOver, carryOverAdd,n)


    #loop through index in listB; this happens when we are on the last index of the last node in listA
    elif (whichNodeB >=0 and indexB > 0 and whichNodeA == 0 and indexA == 0):
        print("elif3: this will process the 0th index of the 0th node in listA")
        print("it will also change nodeA back to the left most once it has finished")
        print("which NodeA:", whichNodeA, "which indexA: ", indexA)
        print("which NodeB:", whichNodeB, "which indexB: ", indexA)

        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10

        #this is attempting that, since the carryOver will be max of 8 (ie. 9*9 = 81) and max of carryOverAdd = 1
        #we can just add them together and even if both are 0, it will be bad since its at the very end, and
        #will be the largest current number, as indexC will constantly be pushed to the left each elif3
        toAdd = listC[indexC]
        listC[indexC] = (toAdd + toInsert + carryOverAdd) % 10
        carryOverAdd = (toAdd + toInsert + carryOverAdd) // 10

        listC[indexC-1] = carryOverAdd + carryOver
        #Need to reset the carryOver and carryOverAdd back to 0
        carryOver =0
        carryOverAdd = 0
        #reset node back to the furthest left element
        whichNodeA = len(listA)-1
        #reset the indexA to the size of the next node value
        indexA = len(listA[whichNodeA])-1
        #move the index of B left one
        indexB = indexB-1
        #to move where we are adding by left 1 index each time we traverse an index of B
        indexC = len(listC)-(n+1)
        #change the value of n so that we subtract a larger n
        n +=1
        print("A entire multiplication has finished, reseting whichNodeA back to right most node:", whichNodeA)

        print("indexA:" , indexA)
        print("whichNodeA", whichNodeA)
        print(listC)
        toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, indexC, carryOver, carryOverAdd, n )


    #finally need to be able to change the node in B
    elif(whichNodeB > 0 and indexB == 0 and whichNodeA == 0 and indexA == 0):
        print("elif4: the last item in listA has been reached, and it is the last item in current nodeB")
        print("we process the current item, and will reset back to furthest A, and onto the next node when this is done")
        toInsert = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) % 10
        carryOver = (listA[whichNodeA][indexA] * listB[whichNodeB][indexB] + carryOver) // 10

        toAdd = listC[indexC]
        listC[indexC] = (toInsert+ toAdd+ carryOverAdd) %10
        carryOverAdd = (toInsert+ toAdd+ carryOverAdd) // 10
        #since this is still the end of a listA multiplication, we need to make sure the carryOver and carryOverAdd are just inserted to the front most of the current index
        
        listC[indexC - 1] = carryOverAdd + carryOver
        carryOverAdd = 0
        carryOver = 0

        #finished a lsitA multiply, so reset back to last node and right most element in that node
        whichNodeA = len(listA)-1
        indexA = len(listA[whichNodeA])-1

        #change the node for B
        whichNodeB-=1
        #change the index to the right most index of that list
        indexB = len(listB[whichNodeB])-1

        #need to reset where the indexC, as we have finished a multiply and need to start a new line, the index must start one left since we have to add a 0 in signifigance
        indexC = len(listC) - (n + 1)
        n+=1
        print("here is listC: ", listC)
        toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, indexC, carryOver, carryOverAdd, n)












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
myString = "990349"
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


listA = [[7,8],[9,9]]
listB = [[1,1],[9,9]]
listC = [0,0,0,0,0,0,0,0,0,0]
whichNodeA = len(listA)-1
whichNodeB = len(listB)-1
indexA = len(listA[0])-1
indexB = len(listB[0])-1
indexC = len(listC)-1
n=1
#nodeSize = 1
carryOver = 0;
carryOverAdd = 0;
#def toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, nodeSize, carryOver):
toMultiply(listA, listB, listC, whichNodeA, whichNodeB, indexA, indexB, indexC, carryOver, carryOverAdd, n)
print(listC)














