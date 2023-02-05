# Задача 2: Найдите сумму цифр трехзначного числа. 

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

def scalpel(num):
    num=str(num)
    sum=0
    for i in num:
        sum+=int(i)
    print(sum)


scalpel(1111111111)