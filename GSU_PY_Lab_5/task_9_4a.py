# -*- coding: utf-8 -*-

'''
Задание 9.4a

Создать функцию convert_to_dict, которая ожидает два аргумента:
* список с названиями полей
* список кортежей с результатами отработки функции parse_sh_ip_int_br из задания 9.4

Функция возвращает результат в виде списка словарей (порядок полей может быть другой):
[{'interface': 'FastEthernet0/0', 'status': 'up', 'protocol': 'up', 'address': '10.0.1.1'},
 {'interface': 'FastEthernet0/1', 'status': 'up', 'protocol': 'up', 'address': '10.0.2.1'}]

Проверить работу функции на примере файла sh_ip_int_br_2.txt:
* первый аргумент - список headers
* второй аргумент - результат, который возвращает функции parse_show из прошлого задания.

Функцию parse_sh_ip_int_br не нужно копировать.
Надо импортировать или саму функцию, и использовать то же регулярное выражение,
что и в задании 9.4, или импортировать результат выполнения функции parse_show.

Ограничение: Все задания надо выполнять используя только пройденные темы.

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

headers = ['interface', 'address', 'status', 'protocol']

settings = parse_sh_ip_int_br("sh_ip_int_br_2.txt")

result = []

for int_setting in settings:
    result_dict = {}
    for i in range(len(headers)):
        result_dict[i] = int_setting[i]
    result.append(result_dict)

print(result)