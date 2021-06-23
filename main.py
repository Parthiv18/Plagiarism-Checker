#Plagiarism Checker

#Open and Read files
def openFile(fileName):
    return open(fileName,encoding='cp437')
def readFile(fileName):
    return fileName.read()
#Split File
def splitFile(fileName):
    return fileName.split(" ")
#Rule1: Same file
def checkFile(readFile1,readFile2):
    if readFile1 == readFile2:
        #print("Same!")
        return True
    return False
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
    #print(count2)
    #if count2 > 0: #plagiarism found
        #return (count2 / len(newList)) * 100 #Return Percentage fl
    return count2
    #else:
        #return 0

def percentage(a,b):
    return (a/b) * 100

getFile1 = openFile("p1.txt")
getFile2 = openFile("p2.txt")
readFile1 = readFile(getFile1)
readFile2 = readFile(getFile2)

sep1=splitFile(readFile1)
sep2=splitFile(readFile2)

print(sep1)
print(sep2)

newList = []
for index, item in enumerate(sep1, start=0):   # default is zero
    if (sep1[index]==sep2[index]):
        newList.append(index)
    #print(index, item)
#len(arr)
print(newList)
if(checkFile(readFile1,readFile2)==True): #Rule 1
    print("Detected 100%")
elif(consecutiveCounter(newList)>=0):
    print("Detected: " + str(consecutiveCounter(newList)) + " consecutuve (4) words in a word!") #Rule 2
print("Detected: " + str(percentage(len(newList),len(sep1))) + "%")




