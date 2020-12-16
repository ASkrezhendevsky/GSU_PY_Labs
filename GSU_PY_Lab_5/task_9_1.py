import re

file_name = input()
reg = input()
input_file = open(file_name, mode="r")
fileLines = input_file.readlines()
for line in fileLines:
    if re.search(reg, line):
        print(line)

