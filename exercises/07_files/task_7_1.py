# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
result = {}

#префикс 'r' для корректного чтения пути в windows
with open('ospf.txt') as f:
    for line in f:
        print('\n')
        line_list = line.split()
        result['Prefix'] = line_list[1]
        result['AD/Metric'] = line_list[2][1:-1]
        result['Next-Hop'] = line_list[4][:-1]
        result['Last update'] = line_list[5][:-1]
        result['Outbound Interface'] = line_list[6]
        for value, key in result.items():
            print('{:22}{:15}'.format(value, key))
print('\n')   