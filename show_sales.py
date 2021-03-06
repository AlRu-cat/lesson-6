# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
#
#     просто запуск скрипта — выводить все записи;
#     запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
#     запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу,
# по номер, равный второму числу, включительно.


import sys


args = sys.argv[1:]

def show_sales(start=0, stop=0):
    for position, line in enumerate(f):
        if position + 1 >= start:
            if position + 1 == stop:
                print(line.rstrip('\n'))
                break
            print(line.rstrip('\n'))

with open('bakery.csv', 'r', encoding='utf-8') as f:
    if not args:
        show_sales()
    elif len(args) == 1:
        show_sales(int(args[0]))
    else:
        show_sales(int(args[0]), int(args[1]))
