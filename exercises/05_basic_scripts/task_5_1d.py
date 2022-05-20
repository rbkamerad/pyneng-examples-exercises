# -*- coding: utf-8 -*-
"""
Задание 5.1d

Переделать скрипт из задания 5.1c таким образом, чтобы, при запросе параметра,
пользователь мог вводить название параметра в любом регистре.

Пример выполнения скрипта:
$ python task_5_1d.py
Введите имя устройства: r1
Введите имя параметра (ios, model, vendor, location, ip): IOS
15.4


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
keys_name = ', '.join(list(london_co[name].keys())) #получаем строку(список(ключи)
param_reqest = ''.join(['input parameter (', keys_name, '): ']) #получаем строку со списком ключей в значении для ключа name
param = input(param_reqest).lower() #получаем ключ в списке keys_name
                                    #.lower() = поиск без учета регистра, т.к. ключи записаны строчными буквами
hostname = london_co[name]

print(hostname.get(param, 'Такого параметра нет')) # *
