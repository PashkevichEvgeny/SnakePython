from figure import Figure
from point import Point


class HorizontalLine(Figure):
    def __init__(self, canvas, x_left, x_right, y, sym):

        super().__init__()

        for x in range(x_left, x_right + 1):
            self.p_list.append(Point(canvas, x, y, sym))
