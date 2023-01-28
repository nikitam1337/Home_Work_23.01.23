
def operating_mode():
    op = int(input('Варианты работы с базой:\n\
1 - Добавление нового студента\n\
2 - Добавление предмета\n\
3 - Добавление оценки ученику по предмету\n\
4 - Показ списка учеников\n\
5 - Показ листа оценок конкретного ученика\n\
6 - Выход из программы\n\
: '))
    return op

def input_student():
    name = input("Введите имя и фамилию: ")
    return name

def input_less():
    less = input('Введите предмет: ')
    return less

def input_mark():
    name = input("Введите имя и фамилию ученика: ")
    less = input("Введите предмет: ")
    mark = input("Введите оценку: ")
    return name, less, mark

def get_name_to_show():
    name = input("Введите имя студента для просмотра оценок: ")
    return name



