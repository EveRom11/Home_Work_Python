# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

# 10 -> 1 2 4 8

def stepen(num,mn=0):
    res=2**mn
    if res>num: return
    else:
        print(res, end=' ')
        stepen(num, mn+1)
    
stepen(1000000)

