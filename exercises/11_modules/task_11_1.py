# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


from unittest import result
from urllib import request


def parse_cdp_neighbors(command_output):
    """
    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
    вместо имени файла, мы делаем функцию более универсальной: она может работать
    и с файлами и с выводом с оборудования.
    Плюс учимся работать с таким выводом.
    """
    result = {}
    cdp_table_start = False

    list_output_per_line =  command_output.split('\n')
    for string_line in list_output_per_line:
        remote_device_name = ''
        local_device_port = ''
        remote_device_port = ''
        if '>' in string_line:
            local_device_name = string_line.split('>')[0]
        if string_line.endswith('ID'):
            cdp_table_start = True
            continue
        if cdp_table_start:
            words_list_in_line = string_line.split()
            if not words_list_in_line:
                return result
            remote_device_name += words_list_in_line[0]
            remote_device_port += words_list_in_line[-2] + words_list_in_line[-1]
            local_device_port += words_list_in_line[1] + words_list_in_line[2]
            local_device = (local_device_name, local_device_port)
            remote_device = (remote_device_name, remote_device_port)
            result[local_device] = remote_device           


if __name__ == "__main__":
    with open('C:\\Users\\Krasnoborodko\\Documents\\pyneng-examples-exercises\\exercises\\11_modules\\sh_cdp_n_sw1.txt') as f:
        print(parse_cdp_neighbors(f.read()))
