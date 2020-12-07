
import re

ignore = ['duplex', 'alias', 'Current configuration']
print("Enter file name:")
defaultFileName = "config_sw1.txt"
fileName = input()
if fileName == "":
    fileName = defaultFileName
inputFile = open(fileName, "r")
fileLines = inputFile.readlines()
for line in fileLines:
    if re.fullmatch(r'!.*\n', line):
        continue
    isContinue = False
    for ignoreCommand in ignore:
        if line.find(ignoreCommand) != -1:
            isContinue = True
            continue
    if isContinue:
        continue
    print(line, end="")
