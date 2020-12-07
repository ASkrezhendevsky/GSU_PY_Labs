import re

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
    print(line, end="")
