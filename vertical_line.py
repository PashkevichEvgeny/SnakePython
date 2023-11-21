from figure import Figure
from point import Point


class VerticalLine(Figure):
    def __init__(self, canvas, y_up, y_down, x, sym):

        super().__init__()

        for y in range(y_up, y_down + 1):
            self.p_list.append(Point(canvas, x, y, sym))
