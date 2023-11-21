import curses
# Для работы с консолью надо установить библиотеку windows-curses, она будет отрисовывать символы
# pip install windows-curses
# В случае ошибки "Redirection is not supported."
# установите галочку в Run -> EditConfigurations -> Emulate terminal in output console


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

    x1 = 1
    y1 = 3
    sym1 = '*'

    x2 = 4
    y2 = 5
    sym2 = '#'

    # Рисуем символ в заданных координатах
    canvas.addstr(y1, x1, sym1)
    # Рисуем еще один символ
    canvas.addstr(y2, x2, sym2)

    # Обновляем полотно
    canvas.refresh()

    # Устанавлиаем задержку 3000 мс., чтобы просмотреть результат отрисовки
    curses.napms(3000)



