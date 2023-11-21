from point import Point


class HorizontalLine:
    def __init__(self, canvas, x_left, x_right, y, sym):

        self.p_list = list()

        for x in range(x_left, x_right + 1):
            self.p_list.append(Point(canvas, x, y, sym))

    def draw(self):
        for point in self.p_list:
            point.draw()
