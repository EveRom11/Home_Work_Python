# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12


def a(list):
    sum=0   
    for i in range(1,len(list),2):
        for j in range(i+2, len(list),2):
            sum+=list[i]+list[j]
            print(f'i={i}, j={j}\nlist[i]={list[i]}, list[j]={list[j]}')
            print(sum)
            sum=0
            break


ar=[2,9,8,7,6,4,6,3,1,4,7]
a(ar)