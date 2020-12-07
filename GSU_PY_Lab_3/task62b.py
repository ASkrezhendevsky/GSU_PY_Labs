import re

ignore = ['duplex', 'alias', 'Current configuration']
print("Enter file name:")

defaultFileName = "config_sw1.txt"
defaultOutputFileName = "config_sw1_cleared.txt"

fileName = input()
if fileName == "":
    fileName = defaultFileName

inputFile = open(fileName, "r")
outputFile = open(defaultOutputFileName, "w")

fileLines = inputFile.readlines()
for line in fileLines:
    isContinue = False
    for ignoreCommand in ignore:
        if line.find(ignoreCommand) != -1:
            isContinue = True
            continue
    if isContinue:
        continue
    outputFile.write(line)
