# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def trans(num):
    osn=2
    resalt=''
    while num>=osn:
        ost=num%osn
        num//=osn 
        resalt=str(ost)+resalt
    resalt=str(num)+resalt
    print(resalt)

trans(455)

