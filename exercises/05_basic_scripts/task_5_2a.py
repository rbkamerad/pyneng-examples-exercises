# -*- coding: utf-8 -*-
"""
Задание 5.2a

Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску,
как в задании 5.2.

Пример адреса сети (все биты хостовой части равны нулю):
* 10.0.1.0/24
* 190.1.0.0/16

Пример адреса хоста:
* 10.0.1.1/24 - хост из сети 10.0.1.0/24
* 10.0.5.195/28 - хост из сети 10.0.5.192/28

Если пользователь ввел адрес 10.0.1.1/24, вывод должен быть таким:

Network:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000


Проверить работу скрипта на разных комбинациях хост/маска, например:
    10.0.5.195/28, 10.0.1.1/24

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)


Подсказка:
Есть адрес хоста в двоичном формате и маска сети 28. Адрес сети это первые 28 бит
адреса хоста + 4 ноля.
То есть, например, адрес хоста 10.1.1.195/28 в двоичном формате будет
bin_ip = "00001010000000010000000111000011"

А адрес сети будет первых 28 символов из bin_ip + 0000 (4 потому что всего
в адресе может быть 32 бита, а 32 - 28 = 4)
00001010000000010000000111000000

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""


input_net = input('input subnet (ex:10.1.1.0/24): ').split('/')

mask = int(input_net[1])
mask_bit_str = '1' * mask + '0' * (32 - mask)
mask_bit_list = ([
    int(mask_bit_str[0:8], 2),
    int(mask_bit_str[8:16], 2),
    int(mask_bit_str[16:24], 2),
    int(mask_bit_str[24:], 2),
])
result_mask = '''
Mask:
/{0:}
{1:<10}{2:<10}{3:<10}{4:<10}
{1:08b}  {2:08b}  {3:08b}  {4:08b}
'''

ip = input_net[0].split('.')
ip[0] = int(ip[0])
ip[1] = int(ip[1])
ip[2] = int(ip[2])
ip[3] = int(ip[3])
ip_bit_str=f'{ip[0]:08b}{ip[1]:08b}{ip[2]:08b}{ip[3]:08b}'
net_bit_str = ip_bit_str[0:mask] + '0' * (32 - mask)
result_net = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}
'''
print(result_net.format(
          int(net_bit_str[0:8], 2),
          int(net_bit_str[8:16], 2),
          int(net_bit_str[16:24], 2),
          int(net_bit_str[24:], 2)) +
      result_mask.format(
          mask,
          mask_bit_list[0], 
          mask_bit_list[1], 
          mask_bit_list[2], 
          mask_bit_list[3]
          ))