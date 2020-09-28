ospf_route = 'O     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'
ospf_routeArray = ospf_route.split();
prefix = ospf_routeArray[1];
adMetric = ospf_routeArray[2].strip();
nextHop = ospf_routeArray[4].strip();
lastUpdate = ospf_routeArray[-2].strip();
outboundInterface = ospf_routeArray[-1];
print(
    'Protocol:\t\t\tOSPF\n'
    'Prefix:\t\t\t\t'+prefix+'\n'+
    'AD/Metric:\t\t\t'+adMetric+'\n'+
    'Next-Hop:\t\t\t'+nextHop+'\n'+
    'Last update:\t\t'+lastUpdate+'\n'+
    'Outbound Interface:\t'+outboundInterface
)