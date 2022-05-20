# -*- coding: utf-8 -*-
"""
Задание 5.1b

Переделать скрипт из задания 5.1a таким образом, чтобы, при запросе параметра,
отображался список возможных параметров. Список параметров надо получить из словаря,
а не прописывать вручную.

Вывести информацию о соответствующем параметре, указанного устройства.

Пример выполнения скрипта:
$ python task_5_1b.py
Введите имя устройства: r1
Введите имя параметра (location, vendor, model, ios, ip): ip
10.255.0.1

$ python task_5_1b.py
Введите имя устройства: sw1
Введите имя параметра (location, vendor, model, ios, ip, vlans, routing): ip
10.255.0.101

Ограничение: нельзя изменять словарь london_co.

Все задания надо выполнять используя только пройденные темы. То есть эту задачу можно
решить без использования условия if.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

name = input('input hostname r1/r2/sw1: ') #выбираем первый ключ (устройство)
keys_names = ', '.join(list(london_co[name].keys())) #получаем строку(список(ключи) *
param_reqest = ''.join(['input parameter (', keys_names, '): ']) #получаем строку со списком ключей в значении для ключа name
param = input(param_reqest) #получаем ключ в списке name_keys 

print(london_co[name][param]) # **

'''
*список ключей выдается аргументе dict_keys, списком
In [28]: london = {'name': 'London1', 'location': 'London Str', 'vendor': 'Cisco'}
In [29]: keys = london.keys()
In [30]: print(keys)
dict_keys(['name', 'location', 'vendor'])
    
    для получаения только списка, нужно явно указать это в запросе
    In [33]: list_keys = list(london.keys())
    In [34]: list_keys
    Out[34]: ['name', 'location', 'vendor', 'ip']
    
        чтобы из списка сделать строку, используем ''.join()
        Метод join собирает список строк в одну строку с разделителем, который указан перед join:
        In [16]: vlans = ['10', '20', '30']
        In [17]: ','.join(vlans)
        Out[17]: '10,20,30'

**
Получить значения из вложенного словаря можно так:
In [7]: london_co['r1']['ios']
Out[7]: '15.4'
'''