import re

fileName = input()
reg = input()
inputFile = open(fileName, mode="r")
fileLines = inputFile.readlines()
for line in fileLines:
    if re.search(reg, line):
        print(line)

