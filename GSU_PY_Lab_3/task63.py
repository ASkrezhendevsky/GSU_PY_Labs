import re

inputFile = open("CAM_table.txt", "r")
inputFileLines = inputFile.readlines()
for line in inputFileLines:
    if re.fullmatch(r".*\S{4}\.\S{4}\.\S{4}.*\n", line):
        print(line, end="")
