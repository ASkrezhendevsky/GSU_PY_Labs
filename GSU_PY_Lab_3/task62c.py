import re

ignore = ['duplex', 'alias', 'Current configuration']

defaultFileName = "config_sw1.txt"
defaultOutputFileName = "config_sw1_cleared.txt"

print("Enter input file name:")
inputFileName = input()
if inputFileName == "":
    inputFileName = defaultFileName
print("Enter output file name:")
outputFileName = input()
if outputFileName == "":
    outputFileName = defaultOutputFileName

inputFile = open(inputFileName, "r")
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
