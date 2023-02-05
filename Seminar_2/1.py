# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

def scalpel(num):
    num=str(num)
    sum=0
    for i in num:
        if i=='.':
            continue
        sum+=int(i)
    print(sum)


scalpel(1111.111111)