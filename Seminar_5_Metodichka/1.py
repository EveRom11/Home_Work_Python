# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

# def st(a,b,step=1):
#     res=a**step
#     print(res)
#     if step==b: return res
#     st(a,b,step+1) 
# st(2,3)

# либо

# def st(a,b):
#     res=a**b
#     if b==0: return res
#     st(a,b-1)
#     print(res)
# st(2,3)

# либо

def st(a,b,step=1):
    res=a**b
    if step==b: return res
    return st(a,b,step+1)
print(st(3,5))