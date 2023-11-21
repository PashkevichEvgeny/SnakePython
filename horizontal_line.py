from figure import Figure
from point import Point


# Наследуем класс HorizontalLine от класса Figure
class HorizontalLine(Figure):
    def __init__(self, canvas, x_left, x_right, y, sym):
        # Вызываем конструктор из базового класса
        super().__init__()

        for x in range(x_left, x_right + 1):
            self.p_list.append(Point(canvas, x, y, sym))
