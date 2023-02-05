# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

# 385916 -> yes
# 123456 -> no

# Решение №1. Если отталкиваться от того, что нам нужно считать именно автобусный билет и решение может быть не масштабируемым.
from random import randint
def scalpel_2_0(num):
    num=str(num)
    result=0
    for i in num:
        result+=int(i)
    if result>9:return scalpel_2_0(result)
    else:return result

def happy_ticket():
    ticket=[randint(0,9) for i in range(6)]
    sum_l=scalpel_2_0(int(ticket[0])+int(ticket[1])+int(ticket[2]))
    sum_r=scalpel_2_0(int(ticket[3])+int(ticket[4])+int(ticket[5]))
    print(f'Ваш билет {ticket}\nСумма левого сектора =  {sum_l}\nСумма правого сектора =  {sum_r}\n--->', end=' ')
    print('счастливый)' if sum_l==sum_r else 'не счастливый(')

happy_ticket()

# Решение №2. Если нам все же понадобится масштабировать для задачки побольше, но при условии, что аргумент num- четное число.
# def happy_ticket_2_0(num):
#     ticket=[randint(0,9) for i in range(num)]
#     print(ticket)
#     res_l=0
#     res_r=0
#     for i in range(num//2):
#             res_l+=ticket[i]
#     for j in range(-1,-num//2-1,-1):
#         res_r+=ticket[j]
#     print(f'res_l= {(res_l)}, res_r= {(res_r)}')
#     print(f'Сумма левого сектора = {scalpel_2_0(res_l)}\nСумма правого сектора = {scalpel_2_0(res_r)}')

# happy_ticket_2_0(6)
