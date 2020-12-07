IP = "192.33.5.1"
if IP == "255.255.255.255":
    print("local broadcast")
if IP == "0.0.0.0":
    print("unassigned")
firstNum = IP.split(".")[0]
if 224 < int(firstNum) < 239:
    print("multicast")
if int(firstNum) < 223:
    print("unicast")


