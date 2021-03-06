# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""


input_net = input('input subnet (ex:10.1.1.0/24): ').split('/')
net = input_net[0].split('.')
net[0] = int(net[0])
net[1] = int(net[1])
net[2] = int(net[2])
net[3] = int(net[3])

mask = int(input_net[1])
mask_bit = '1' * mask + '0' * (32 - mask)
mask_bit = ([
    int(mask_bit[0:8], 2),
    int(mask_bit[8:16], 2),
    int(mask_bit[16:24], 2),
    int(mask_bit[24:], 2),
])
#{0:<10b}
# 0  = номер аргумента в .format
# <  = выравнивание по левому краю
# 10 = выделяем кол-во символов для данных
# b  = перевод в bin(2)
result = '''
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}

Mask:
/{4:}
{5:<10}{6:<10}{7:<10}{8:<10}
{5:8b}  {6:08b}  {7:08b}  {8:08b}
'''

print(result.format(
  net[0], 
  net[1], 
  net[2], 
  net[3],
  mask,
  mask_bit[0], 
  mask_bit[1], 
  mask_bit[2], 
  mask_bit[3],
))