mac = [' aabb: cc80: 7000', ' aabb: dd80: 7340', ' aabb: ee80: 7000', ' aabb: ff80: 7000']
mac_cisco = []
for singleMac in mac:
    newMacArray = [i.strip() + "." for i in singleMac.split(":")]
    newMacArray[-1] = newMacArray[-1].replace(".", "")
    mac_cisco.append(''.join(newMacArray))
print(mac_cisco)
