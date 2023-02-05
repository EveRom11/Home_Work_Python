# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

from random import randint
#Создает список
def spisok(num):
    list=[randint(-num,num) for i in range(num)]
    print(list)
    return list

# Создает файл .txt, где в каждой новой строке хранятся индексы для перемножения
def make_file(list:list,path):
    ar=[]
    size_ar=0
    list_ind=open(path,'w')
    while size_ar!=len(list):
        num=randint(0,len(list)-1)
        if ar.count(num):
            continue
        ar.append(num)
        list_ind.writelines(f"{num}\n")
        size_ar+=1

# Парами берет позиции из файла и применяет их к списку из N элементов.
def fisher(list:list,path):
    ar_res=[]
    data= open(path, 'r')
    for j in data:
        j=int(j)
        for i in data:
            i=int(i)
            result=list[j]*list[i]
            ar_res.append(result)
            print(f"j- {j}, i- {i}, list[j]- {list[j]}, list[i]- {list[i]}, result- {result}")
            break
    if len(list)%2==1:
        alone=list[j]**2
        print(f'Без пары. Квадрат самого себя list[{j}]**2= {alone}')
        ar_res.append(alone)
    print(ar_res)
    data.close()

arr=spisok(11)
path_file='Home_Work_Python/Seminar_2/list_index.txt'
make_file(arr,path_file)
fisher(arr,path_file)