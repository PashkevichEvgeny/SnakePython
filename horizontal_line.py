from point import Point


class HorizontalLine:
    def __init__(self, canvas):
        self.canvas = canvas
        self.p_list = list()
        p1 = Point(canvas, 4, 4,  '*')
        p2 = Point(canvas, 5, 4, '*')
        p3 = Point(canvas, 6, 4, '*')
        self.p_list.append(p1)
        self.p_list.append(p2)
        self.p_list.append(p3)

    def draw(self):
        for point in self.p_list:
            point.draw()
