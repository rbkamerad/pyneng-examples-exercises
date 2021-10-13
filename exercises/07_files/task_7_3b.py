# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
with open('CAM_table.txt') as f:
    result = []
    for line in f:
        line_ = line.split()
        if line_ and line_[-1].startswith('Gi'):
            vlan = int(line_[0])
            mac = line_[1]
            intf = line_[-1]
            result.append([vlan, mac, intf])
        else:
            continue
    
    uvlan = int(input('Enter VLAN number: '))
    for list_ in result:
        if list_[0] == uvlan:
            print('{:<10}{:<20}{:<5}'.format(list_[0], list_[1], list_[2]))