import curses
# Для работы с консолью надо установить библиотеку windows-curses, она будет отрисовывать символы
# pip install windows-curses
# В случае ошибки "Redirection is not supported."
# установите галочку в Run -> EditConfigurations -> Emulate terminal in output console

# Импортируем класс Point из файла point.py
from horizontal_line import HorizontalLine
from human_employee import Employee
from point import Point
from vertical_line import VerticalLine


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
    # Размеры полотна
    height, width = canvas.getmaxyx()
    # Настройка размеров полотна
    height, width = height - 2, width - 1

    # Отрисовка рамочки
    up_line = HorizontalLine(canvas, 1, width, 1, '+')
    down_line = HorizontalLine(canvas, 1, width, height, '+')
    left_line = VerticalLine(canvas, 1, height, 1, '+')
    right_line = VerticalLine(canvas, 1, height, width, '+')
    up_line.draw()
    down_line.draw()
    left_line.draw()
    right_line.draw()

    # Отрисовка точки
    p = Point(canvas, 4, 5, '#')
    p.draw()

    # Устанавлиаем задержку 3000 мс., чтобы просмотреть результат отрисовки
    curses.napms(3000)

    # Создаем работника
    employee = Employee()
    # У него есть свойство возраст из класса Human
    employee.age = 42
    # И свойство зарплата из класса Employee
    employee.pay = 30_000
