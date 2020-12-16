# -*- coding: utf-8 -*-

'''
Задание 9.3a

Переделать функцию parse_cfg из задания 9.3 таким образом, чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

Например (взяты произвольные адреса):
{'FastEthernet0/1':('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2':('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

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
    current_interface = ""
    result = {}
    for line in input_lines:
        if re.search(new_comand_block, line):
            is_interface_block = False
            int_match = re.search(interface_regex, line)
            if int_match:
                current_interface = int_match[0]
                is_interface_block = True
            continue
        if is_interface_block:
            match = re.search(ip_address_pattern, line)
            if match:
                result[current_interface] = (match[1], match[2])
    return result


print(parch_cfg("config_r1.txt"))