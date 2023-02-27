# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# сначала создает файл .txt, а потом будет в него дописывать данные
def spravochnik_add(surname, name, number):
    data=surname + ' ' + name + ' : ' + number
    file_p= open('Home_Work_Python\Seminar_8/telefon_book.txt', 'a', encoding='utf-8')
    file_p.writelines(data+'\n')
    file_p.close()
    print(data)
    return data

# читает из файла
def reader(info,file_p):
    if info is None:info=' '
    count=0
    for line in file_p:
        if info in line:
            print(line, end='')
            count+=1
    if count==0:print('Такого контакта нет в справочнике')

# открывает файл, выгружает из  него инфу в список и позволяет удалить запись
def del_row(info,file_p):
    list_file=file_p.readlines()
    for i in range(len(list_file)):
        if info in list_file[i]:
            print(i+1, '.', list_file[i], end='')
    print(' ')
    command=int(input('Введите номер строки, которую нужно удалить: '))
    list_file.pop(command-1)
    print(list_file)
    file_p=open('Home_Work_Python\Seminar_8/telefon_book.txt','w',encoding='utf-8')
    file_p.writelines(list_file)
    file_p.close()
    return command-1

def replace_row(info,file_p):
    list_file=file_p.readlines()
    for i in range(len(list_file)):
        if info in list_file[i]:
            print(i+1, '.', list_file[i], end='')
    print(' ')
    command=int(input('Введите номер строки, которую нужно изменить: '))
    list_file.pop(command-1)
    print(list_file)
    list_file.insert(command-1,spravochnik_add(str(input('Введите фамилию: ')).capitalize(),str(input('Введите имя: ')).capitalize(), str(input('Введите номер телефона: ')))+'\n' )
    print(list_file)
    file_p=open('Home_Work_Python\Seminar_8/telefon_book.txt','w',encoding='utf-8')
    file_p.writelines(list_file)
    file_p.close()


def telephone_directory(command):
    file_p=open('Home_Work_Python\Seminar_8/telefon_book.txt','r',encoding='utf-8')

    if command==1:spravochnik_add(str(input('Введите фамилию: ')).capitalize(),str(input('Введите имя: ')).capitalize(), str(input('Введите номер телефона: ')))
    elif command==2:reader(input("Введите фамилию или имя, чтобы найти контакт.\nНе вводите ничего, чтобы увидеть весь весь справочик: ").capitalize(),file_p)
    elif command==3:del_row(input("Введите фамилию или имя, чтобы удалить контакт: ").capitalize(),file_p)
    elif command==4:replace_row(input("Введите фамилию или имя, чтобы изменить контакт: ").capitalize(),file_p)
    else:print('Вы не выбрали команду')
    file_p.close()
    
telephone_directory(int(input('Введите команду:\n1- Добавить контакт \n2- Найти контакт\n3- Удалить контакт\n4- Изменить контакт\n----> ')))
# 