# -*- coding: utf-8 -*-

'''
Задание 9.4

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'up', 'up')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br_2.txt.

'''

import re


def parse_sh_ip_int_br(file_name):
    input_file = open(file_name, mode="r")
    input_lines = input_file.readlines()
    result = []
    for line in input_lines:
        if re.search("^\w+#", line) or re.search("^Interface", line):
            continue;
        row = re.split("\s+", line)
        result.append((row[0], row[1], row[4], row[5]))
    return result

print(parse_sh_ip_int_br("sh_ip_int_br_2.txt"))
