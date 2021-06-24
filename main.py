#Plagiarism Checker
import math,re
#Open and Read files
def openFile(fileName):
    return open(fileName,encoding='cp437')
def readFile(fileName):
    return fileName.read()
#Split File
def splitFile(fileName):
    return fileName.split()
#Rule1: Same file
def checkFile(readFile1,readFile2):
    if readFile1 == readFile2:
        #print("Same!")
        return True
    return False
#Read
def addData (newList):
    #If texts lengths are not the same
    if (len(sep1) > len(sep2)):
        while (len(sep1) != len(sep2)):
            sep2.append(" ")
    elif (len(sep2) > len(sep1)):
        while (len(sep1) != len(sep2)):
            sep1.append(" ")

    for index, item in enumerate(sep1, start=0):  # default is zero
        if (sep1[index] == sep2[index]):
            newList.append(index)
        # print(index, item)
    return newList
#Rule 2: 4 same words in a row
def consecutiveCounter(newList):
    countsOfFour = 0
    count2 = 0
    for i in range(len(newList) - 3): #loop through the list
        #check the conditions for 4 consecutive numbers in a row
        if (newList[i] == newList[i + 1] - 1 and newList[i] == newList[i + 2] - 2 and newList[i] == newList[i + 3] - 3):
            countsOfFour += 1 #increase counter
        if countsOfFour == 1: #if the counts of 4 is one make new counter to 1
            count2 = 1
            #print(countsOfFour)
        elif (countsOfFour % 2 == 0) and countsOfFour > 1: #Pattern [1 3 ...] use arthemetic series to solve for n
            count2 = ((countsOfFour - 1 + 2) / 2) - 0.5
        elif (countsOfFour % 2 != 0) and countsOfFour > 1: #Pattern [1 3 ...] use arthemetic series to solve for n
            count2 = (countsOfFour - 1 + 2) / 2
    return count2
#Check if there is citations
def checkCitations(tempList):
    for i in range(len(tempList)):  # (name,2)
        # if (sep1[i][0]=='('):
        if (re.search('([a-zA-z],[0-9]+)', tempList[i])):
            print("Citations Detected: ", tempList[i])
def percentage(a,b):
    return (a/b) * 100

#Get Files
getFile1 = openFile("p1.txt")
getFile2 = openFile("p2.txt")
readFile1 = readFile(getFile1)
readFile2 = readFile(getFile2)
sep1=splitFile(readFile1)
sep2=splitFile(readFile2)

#Read Data (addData) - Converts string into list
#Rule 1 (checkFile) - All words are the same
#Rule 2 (consecutiveCounter) - 4 consecutive words are the same
#Safe Case (checkCitations) - Citations in text detected (name,num)

newL = []
newList = addData(newL)

#Test
print(sep1)
print(sep2)
print(newList)

if(checkFile(readFile1,readFile2)==True): #Rule 1
    print("Detected 100%")
elif(consecutiveCounter(newList)>0):
    print("Detected: " + str(consecutiveCounter(newList)) + " consecutuve (4) words in a row!") #Rule 2
    print("Detected: " + str(round(percentage(len(newList),len(sep1)),2)) + "%")
else:
    print("Safe")
checkCitations(sep1)



