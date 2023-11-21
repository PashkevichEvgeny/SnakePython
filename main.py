import curses
# Для работы с консолью надо установить библиотеку windows-curses, она будет отрисовывать символы
# pip install windows-curses
# В случае ошибки "Redirection is not supported."
# установите галочку в Run -> EditConfigurations -> Emulate terminal in output console

# Импортируем класс Point из файла point.py
from point import Point


def canvas():
    """
     Функция создает и возвращает полотно, на котором будут отрисовываться символы
    """
    # Инициализация полотна
    new_canvas = curses.initscr()
    # Выключить отображение курсора
    curses.curs_set(False)
    return new_canvas


if __name__ == '__main__':
    canvas = canvas()

    # Создаем точку и передаем ей значения в контруктор
    p1 = Point(canvas, 1, 3, '*')
    p1.draw()

    # Создаем еще одну точку
    p2 = Point(canvas, 4, 5, '#')
    p2.draw()

    # Устанавлиаем задержку 3000 мс., чтобы просмотреть результат отрисовки
    curses.napms(3000)

    # Создаем список и добавляем в него три числа
    num_list = list()
    num_list.append(0)
    num_list.append(1)
    num_list.append(2)

    # Создаем три переменных и присваиваем им значения из списка чисел
    x = num_list[0]
    y = num_list[1]
    z = num_list[2]

    # Цикл for для перебора значений из списка
    for i in num_list:
        print(i)

    # Извлекаем из списка элемент под индексом 0
    num_list.pop(0)

    # Создаем список с точками p1 и p2
    p_list = list()
    p_list.append(p1)
    p_list.append(p2)

    print()
