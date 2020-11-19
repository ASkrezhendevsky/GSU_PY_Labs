def get_access_list(interfaces, psecurity=False):
    access_template = ['switchport mode access ',
                       'switchport access vlan ',
                       'switchport nonegotiate ',
                       'spanning- tree portfast ',
                       'spanning- tree bpduguard enable ']
    port_security = ['switchport port-security maximum 2',
                     'switchport port-security violation restrict',
                     'switchport port-security']
    result = []
    for interface in interfaces.items():
        result.append("interface " + interface[0])
        result.append(access_template[0])
        result.append(access_template[1] + str(interface[1]))
        if psecurity:
            result.append(port_security[0])
            result.append(port_security[1])
    return result


access_dict = {'FastEthernet0/12': 10,
               'FastEthernet0/14': 11,
               'FastEthernet0/16': 17,
               'FastEthernet0/17': 150}
print(get_access_list(access_dict))

