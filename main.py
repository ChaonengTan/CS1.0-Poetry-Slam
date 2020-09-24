import random
def linesPrintedBackwards(fileName):
    fileLines=open(fileName, "r").readlines()
    for line in reversed(fileLines):
        print(line.rstrip())
def linesPrintedRandom(fileName):
    fileLines=open(fileName, "r").readlines()
    linesList=[]
    for line in fileLines:
        linesList.append(line)
    random.shuffle(linesList)
    for line in linesList:
        print (line)
def linesPrintedCustom(fileName):
    fileLines=open(fileName, "r").readlines()
    linesList=[]
    for line in fileLines:
        linesList.append(line)
    print (lineList.size)
linesPrintedCustom("poem.txt")