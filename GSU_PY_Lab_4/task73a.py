def get_int_vlan_map(file_name):
    access_dict = {}
    trunk_dict = {}

    with open(file_name, 'r') as file_lines:
        for line in file_lines:
            if 'interface' in line:
                interface = line.split()[1]
            elif 'access vlan' in line:
                vlan = int(line.split()[3])
                access_dict[interface] = vlan
            elif 'switchport mode access' in line:
                access_dict[interface] = 1
            elif 'allowed vlan' in line:
                vlans_list = [int(vlan) for vlan in line.split()[4].split(',')]
                trunk_dict[interface] = vlans_list

    return access_dict, trunk_dict


access_dict, trunk_dict = get_int_vlan_map('config_sw1.txt')
print(access_dict)
print(trunk_dict)
