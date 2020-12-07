import re

inputFile = open("CAM_table.txt", "r")
inputFileLines = inputFile.readlines()
outputLines = []
for line in inputFileLines:
    if re.fullmatch(r".*\S{4}\.\S{4}\.\S{4}.*\n", line):
        outputLines.append(line)
outputLines.sort()

print("Enter vlan number:")
vlanNumber = input()

for line in outputLines:
    if line.split()[0] == vlanNumber:
        print(line, end="")
