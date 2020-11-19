def get_int_vlan_map(file_name):
    commands_dict = {}

    with open(file_name, 'r') as file_lines:
        current_command = "none"
        for line in file_lines:

            if line[0] == "!" or line[0] == "\n":
                continue
            if line[0] == " ":
                commands_dict[current_command].append(line)
                continue
            current_command = line
            commands_dict[current_command] = []
    return commands_dict


commands_dict = get_int_vlan_map('config_sw1.txt')
print(commands_dict)
