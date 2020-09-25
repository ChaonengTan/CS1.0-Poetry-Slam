import random
def getFileLines(fileName):
    fileLines=open(fileName, "r").readlines()
    for line in (fileLines):
        print(line.rstrip())
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
    for line in (fileLines):
        print(line.rstrip())
    for line in reversed(fileLines):
        print(line.rstrip())

selectedFile = input("Which file do you wish to execute on? : ")
print("Options: 1) Print poem 2) Print poem backwards 3) Print shuffled poem 4) Print EPIC CUSTOM poem layout")
executeFunction = input("Select choice from above (numerical): ")

if executeFunction=="1":
    getFileLines(selectedFile)
elif executeFunction=="2":
    linesPrintedBackwards(selectedFile)
elif executeFunction=="3":
    linesPrintedRandom(selectedFile)
elif executeFunction=="4":
    linesPrintedCustom(selectedFile)
else:
    print("Function not found")