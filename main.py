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

    # Создаем экземпляр класса Point
    p1 = Point()

    # Задаем значения переменным
    p1.canvas = canvas
    p1.x = 1
    p1.y = 3
    p1.sym = '*'

    p1.draw()

    # Создаем еще одну точку
    p2 = Point()

    # Задаем значения переменным
    p2.canvas = canvas
    p2.x = 4
    p2.y = 5
    p2.sym = '#'

    p2.draw()

    # Устанавлиаем задержку 3000 мс., чтобы просмотреть результат отрисовки
    curses.napms(3000)
