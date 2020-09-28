vlans = '10,10,20,30,40,20,50,70,70'
vlansList = list(set((vlans).split(',')))
vlansList.sort()
print(vlansList)
