CONFIG = 'switchport trunk allowed vlan 1,3,10,20,30,100'
array = CONFIG.split()
print(array[-1].split(','))

