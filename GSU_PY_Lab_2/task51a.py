IP = "192.33.5.1"
isIpCorrect = True
if len(IP.split(".")) != 4:
    isIpCorrect = False

ipArray = IP.split(".")
for number in ipArray:
    if int(number) not in range(0, 255):
        isNumbersCorrect = False
        break
if isIpCorrect:
    if IP == "255.255.255.255":
        print("local broadcast")
        s
    if IP == "0.0.0.0":
        print("unassigned")
    firstNum = IP.split(".")[0]
    if 224 < int(firstNum) < 239:
        print("multicast")
    if int(firstNum) < 223:
        print("unicast")
else:
    print("Incorrect IPv4 address")






