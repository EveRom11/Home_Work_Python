# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

# 3 2 4 -> yes
# 3 2 1 -> no

def choko_part(pow, column, part):
    if part==1: dol='дольку'
    elif 1<part<5: dol='дольки' 
    else: dol='долек'
    print(f'Можно ли отломить {part} {dol} за раз?', end=' ---> ')
    print('Да!' if part!=1 and part<pow*column and part%pow==0 or part%column==0 else 'Нет!')

choko_part(3,2,4)