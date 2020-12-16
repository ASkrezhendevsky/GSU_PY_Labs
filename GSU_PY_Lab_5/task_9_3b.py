# -*- coding: utf-8 -*-

'''
Задание 9.3b

Проверить работу функции parse_cfg из задания 9.3a на конфигурации config_r2.txt.

Обратите внимание, что на интерфейсе e0/1 назначены два IP-адреса:
interface Ethernet0/1
 ip address 10.255.2.2 255.255.255.0
 ip address 10.254.2.2 255.255.255.0 secondary

А в словаре, который возвращает функция parse_cfg, интерфейсу Ethernet0/1
соответствует только один из них (второй).

Переделайте функцию parse_cfg из задания 9.3a таким образом,
чтобы она возвращала список кортежей для каждого интерфейса.
Если на интерфейсе назначен только один адрес, в списке будет один кортеж.
Если же на интерфейсе настроены несколько IP-адресов, то в списке будет несколько кортежей.

Проверьте функцию на конфигурации config_r2.txt и убедитесь, что интерфейсу
Ethernet0/1 соответствует список из двух кортежей.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''

import re


def parch_cfg(file_name):
    input_file = open(file_name, mode="r")
    input_lines = input_file.readlines()
    interface_regex = "^interface\s+\S+"
    new_comand_block = "^\w"
    ip_address_pattern = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    is_interface_block = False
    ip_counter = 0;
    current_interface = ""
    result = {}
    for line in input_lines:
        if re.search(new_comand_block, line):
            is_interface_block = False
            int_match = re.search(interface_regex, line)
            if int_match:
                current_interface = int_match[0]
                is_interface_block = True
                ip_counter = 0
                result[current_interface] = []
            continue
        if is_interface_block:
            match = re.search(ip_address_pattern, line)
            if match:
                result[current_interface].append((match[1], match[2]))
                ip_counter += 1
    return result


print(parch_cfg("config_r2.txt"))