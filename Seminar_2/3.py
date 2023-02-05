# Задайте список из n чисел последовательности {x : (1=1/x) ** x } и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def dict_make(num):
    res=4
    dict_m={}
    for i in range(1,num+1):
        dict_m[i]=res
        res+=3
    print(dict_m)

dict_make(6)