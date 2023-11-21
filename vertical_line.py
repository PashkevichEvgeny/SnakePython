from point import Point


class VerticalLine:
    def __init__(self, canvas, y_up, y_down, x, sym):

        self.p_list = list()

        for y in range(y_up, y_down + 1):
            self.p_list.append(Point(canvas, x, y, sym))

    def draw(self):
        for point in self.p_list:
            point.draw()
