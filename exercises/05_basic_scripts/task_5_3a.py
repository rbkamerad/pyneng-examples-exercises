# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

result_switchport = {
    'access': access_template,
    'trunk': trunk_template
    }

switchport_mode = '\n'.join(result_switchport[input('Введите режим работы интерфейса (access/trunk): ')])

interface = input('Введите тип и номер интерфейса: ')
result_interface = f'interface {interface}'

vlan = input('Введите номер влан(ов): ')
switchport_mode = switchport_mode.format(vlan)

result = '''
{0}
{1}
'''
print(result.format(
    result_interface,
    switchport_mode
    ))