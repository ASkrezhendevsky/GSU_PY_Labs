# -*- coding: utf-8 -*-

'''
Задание 9.3

Создать функцию parse_cfg, которая ожидает как аргумент имя файла,
в котором находится конфигурация устройства.

Функция должна обрабатывать конфигурацию и возвращать IP-адреса и маски,
которые настроены на интерфейсах, в виде списка кортежей:
* первый элемент кортежа - IP-адрес
* второй элемент кортежа - маска

Например (взяты произвольные адреса):
[('10.0.1.1', '255.255.255.0'), ('10.0.2.1', '255.255.255.0')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.


Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды, а не ввод пользователя.

'''
import re


def parch_cfg(file_name):
    input_file = open(file_name, mode="r")
    input_lines = input_file.readlines()
    interface_regex = "^interface"
    new_comand_block = "^\w"
    ip_address_pattern = "(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
    is_interface_block = False
    result_lines = []
    for line in input_lines:
        if re.search(new_comand_block, line):
            is_interface_block = False
            if re.search(interface_regex, line):
                is_interface_block = True
            continue
        if is_interface_block:
            match = re.search(ip_address_pattern, line)
            if match:
                result_lines.append((match[1], match[2]))
    return result_lines


print(parch_cfg("config_r1.txt"))