access_template = [' switchport mode access',
                   ' switchport access vlan',
                   ' spanning- tree portfast',
                   ' spanning- tree bpduguard enable']
trunk_template = [' switchport trunk encapsulation dot1q',
                  ' switchport mode trunk',
                  ' switchport trunk allowed vlan',
                  ' switchport trunk allowed vlan remove',
                  ' switchport trunk allowed vlan add'
                  ]
fast_int = {'access': {'0/12': ' 10', ' 0/14': ' 11', ' 0/16': ' 17', ' 0/17': ' 150'},
            'trunk': {'0/1': ['add', ' 10', ' 20'],
                      '0/2': ['only', ' 11', ' 30'],
                      '0/4': ['del', ' 17']}}
for intf, vlan in fast_int['trunk'].items():
    print(' interface FastEthernet' + intf)
    print(trunk_template[1])
    if vlan[0] == "only":
        print("{} {} ".format(trunk_template[2], "".join(i for i in vlan[1:])))
    if vlan[0] == "add":
        print("{} {} ".format(trunk_template[4], "".join(i for i in vlan[1:])))
    if vlan[0] == "del":
        print("{} {} ".format(trunk_template[3], "".join(i for i in vlan[1:])))
