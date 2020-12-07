inputFile = open("ospf.txt", "r")
outputFile = open("ospfOutput.txt", "w")

fileLines = inputFile.readlines()
for line in fileLines:
    stringParts = line.split()
    outputFile.write(
        "Protocol: OSPF Prefix: " + stringParts[1] + " AD/Metric: " + stringParts[2].strip() + " Next-Hop: " +
        stringParts[4].replace(",", "") + " Last update: " + stringParts[5].replace(",", "") + " Outbound Interface: " +
        stringParts[6].replace('Fast', 'Gigabit') + "\n")

