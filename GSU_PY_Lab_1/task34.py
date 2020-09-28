command1 = 'switchport trunk allowed vlan 1,3,10,20,30,100'
command2 = 'switchport trunk allowed vlan 1,3,100,200,300'

setVlans = set(((command1.split())[-1]).split(',') + ((command2.split())[-1]).split(','))

print(list(setVlans))
