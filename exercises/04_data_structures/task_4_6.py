# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

result_value = ospf_route.split()
result_value[1] = result_value[1].strip('[]')
result_value[3] = result_value[3].strip(',')
result_value[4] = result_value[4].strip(',')
result_value.pop(2)

result_header = '''
Prefix              {:15}
AD/Metric           {:15}
Next-Hop            {:15}
Last update         {:15}
Outbound Interface  {:15}
'''

print(result_header.format(result_value[0],
                           result_value[1],
                           result_value[2],
                           result_value[3],
                           result_value[4]))

'''
https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/string_format.html
'''