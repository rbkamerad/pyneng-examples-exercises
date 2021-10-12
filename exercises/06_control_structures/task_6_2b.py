# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_per_byte = []
ip_input_is_correct = False

while ip_input_is_correct == False:
    ip_input = input('Введите ip-адрес формата 10.0.1.1: ')
    try:
        ip_per_byte = ip_input.split('.')
        if len(ip_per_byte) != 4:
            raise IndexError('Должно быть 4 октета')
        ip_per_byte[0] = int(ip_per_byte[0])
        ip_per_byte[1] = int(ip_per_byte[1])
        ip_per_byte[2] = int(ip_per_byte[2])
        ip_per_byte[3] = int(ip_per_byte[3])
        for byte in ip_per_byte:
            if not 0 <= byte <= 255:
                raise ValueError('Принимаются числа в октете 0-255')
    except (ValueError, IndexError):
        print('Неправильный IP-адрес\n')
        continue
    ip_input_is_correct = True
        

if ip_input == '0.0.0.0':
    print('unassigned')
elif ip_input == '255.255.255.255':
    print('local broadcast')
elif 0 < ip_per_byte[0] <= 223:
    print('unicast')
elif 224 <= ip_per_byte[0] <= 239:
    print('multicast')
else:
    print('unused')