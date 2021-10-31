# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный
файл коммутатора и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов,
  а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов,
  а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент
имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
def get_int_vlan_map(config_filename):
    """
    обрабатывает конфигурационный файл коммутатора и возвращает кортеж из двух словарей:
    * словарь портов в режиме access, где ключи номера портов,
    а значения access VLAN (числа):
    {'FastEthernet0/12': 10,
    'FastEthernet0/14': 11,
    'FastEthernet0/16': 17}

    * словарь портов в режиме trunk, где ключи номера портов,
    а значения список разрешенных VLAN (список чисел):
    {'FastEthernet0/1': [10, 20],
    'FastEthernet0/2': [11, 30],
    'FastEthernet0/4': [17]}
    """
    value = ['Fast', 'vlan', 'mode']
    access = {}
    trunk = {}
    result = [access, trunk]
    with open(config_filename) as file_:
        r_list = []

        for line in file_:
            if len(r_list) == 3:
                r_list.sort() #>vlan, intf, mode
                r_list[0].split(',') #vlan ('100,200') > vlan ['100', '200']
                if r_list[2] == 'access':
                    access[r_list[1]] = r_list[0]
                else:
                    trunk[r_list[1]] = r_list[0]
                r_list = []
                            
            else:
                for item in value:
                    if item in line:
                        r_list.append(line.split()[-1])
            
    result = (access, trunk)
    return(result)

print(get_int_vlan_map('config_sw1.txt'))