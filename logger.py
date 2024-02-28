from data_create import name_data, surname_data, phone_data, adress_data
import pandas as pd


def input_data():            # Добавление данных в телефонные справочники
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()
    var = int(input(f"В каком формате записать данные? \n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{adress}\n\n"
    f"2 Вариант: \n"
    f"{name};{surname};{phone};{adress}\n"
    f"Выберете вариант: "))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите число '))

    if var == 1:
        with open('data_first_variant.csv', 'a', encoding='utf-8') as f:
            f.writelines(f"\n\n{name}\n{surname}\n{phone}\n{adress}")
    elif var == 2:
        with open('data_second_variant.csv', 'a', encoding='utf-8') as f:
            f.writelines(f"{name};{surname};{phone};{adress}\n")



def print_data():          # Отображение всех справочников
    print('Вывожу данные из 1 файла: \n', end='-------- \n')
    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        data_first = f.read()  # Читаем весь файл в одну строку
        data_first_people = data_first.split('\n\n') # Разделяем строку на отдельные значения по двойному пробелу
        for i in data_first_people:
            print(i)
            print('--------')

    print('Вывожу данные из 2 файла: \n')
    data_second = pd.read_csv('data_second_variant.csv', encoding='utf-8')
    print(data_second)


def del_data():           # Удаление данных из телефонных справочников
    var = int(input("Введите, из какого файла надо удалить запись: \n"))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите корректный номер файла '))

    num = int(input("Введите номер записи, которую необходимо удалить: \n"))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            data_del = data_first[:num-1] + data_first[num+4:]   # Удаляем от начала записи по человеку до конца, включая последний пробел
            with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                f.writelines(data_del)
            print('Запись удалена')
           
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            data_del = data_second[:num] + data_second[num+1:]
            with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                f.writelines(data_del)
            print('Запись удалена')


def chenge_data():       # Изменение данных в телефонных справочниках
    print('Введите новые данные для абонента')
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    adress = adress_data()

    var = int(input("Введите номер файла, в который надо внести изменения: \n"))

    while var != 1 and var != 2:
        print('Неправильный ввод')
        var = int(input('Введите корректный номер файла '))

    num = int(input("Введите номер записи, которую необходимо изменить: \n"))

    if var == 1:
        with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
            data_first = f.readlines()
            if 1 <= num <= len(data_first):
                data_first[num-1:num+3] = f"{name}\n{surname}\n{phone}\n{adress}\n"
                with open('data_first_variant.csv', 'w', encoding='utf-8') as f:
                    f.writelines(data_first)
                print('Запись изменена')
            else:
                print('Некорректный номер записи')
           
    elif var == 2:
        with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            data_second = f.readlines()
            if 1 <= num <= len(data_second):
               data_second[num-1] = f"{name};{surname};{phone};{adress}\n"
               with open('data_second_variant.csv', 'w', encoding='utf-8') as f:
                    f.writelines(data_second)
            print('Запись изменена')


def search_data():    # Поиск в стправочнике
    temp = input("Введите параметры для поиска: \n")

    with open('data_first_variant.csv', 'r', encoding='utf-8') as f:
        # Ищем все слова с заданным параметром в строке
        data_first = f.read()  # Читаем весь файл в одну строку
        data_first_people = data_first.split('\n\n') # Разделяем строку на отдельные значения по двойному пробелу
        Flag1 = False
        for i in data_first_people:
            if temp in i:
                if Flag1 == False:
                    print('В первом справочнике найдены следующие записи: \n', end='-------- \n')
                print(i)
                print('--------')
                Flag1 = True

    with open('data_second_variant.csv', 'r', encoding='utf-8') as f:
            Flag2 = False
            for i in f:
                if temp in i:
                    if Flag2 == False:
                        print('Во втором справочнике найдены следующие записи:')
                    print(i, end='') 
                    Flag2 = True

    if Flag1 == False and Flag2 == False:
        print('По данному параметру значения не найдены') 


def txt_data():
    pass