from figure import Figure
from point import Point


# Наследуем класс VerticalLine от класса Figure
class VerticalLine(Figure):
    def __init__(self, canvas, y_up, y_down, x, sym):
        # Вызываем конструктор из базового класса
        super().__init__()

        for y in range(y_up, y_down + 1):
            self.p_list.append(Point(canvas, x, y, sym))
