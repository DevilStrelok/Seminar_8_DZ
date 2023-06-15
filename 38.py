# Задача 38:
# Создать телефонный справочник с возможностью добавления записей и чтения.
# Пользователь также может ввести фамилию, тогда программа должна вывести на экран все записи с этой фамилией.
# Также пользователь может добавлять новых людей в справочник в режиме экспорт.


def show_data():
    with open('phone.txt', 'r', encoding='utf-8') as file:
        book = file.read()
    return book


def new_data():
    with open('phone.txt', 'a', encoding='utf-8') as file:
        file.write(input('Введите новую строку: ') + '\n')


def find_data():
    with open('phone.txt', 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        temp = input('Кого ищем?: ')
        for i in book:
            if temp in i:
                print(i)


while True:
    mode = input('Выберите режим работы справочника' + '\n'
                 + '1-чтение, 2-добавление, 3-поиск, 0-выход: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        find_data()
    elif mode == '0':
        break
    else:
        print('Такого режима работы нет')
