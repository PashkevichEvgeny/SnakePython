class Figure:
    def __init__(self):
        self.p_list = list()

    def draw(self):
        for point in self.p_list:
            point.draw()
