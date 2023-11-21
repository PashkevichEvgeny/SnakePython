# Создаем класс Point
class Point:
    # Удаляем свойста из класса, объявление и установка по умолчанию будет происходить в констркторе

    # Конструктор в Python - это метод. И он только один в классе в отличии от C# и Java
    # Для возможности вызова класса без параметров надо установить значения по умолчанию
    def __init__(self, canvas=None, x=0, y=0, sym=' '):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.sym = sym

    # Передаем в метод параметр self для обращения к свойствам экземпляра
    def draw(self):
        """
        Функция принимает полотно, координаты точки и символ, который потом отрисовывает
        """
        # Рисуем символ в заданных координатах
        self.canvas.addstr(self.y, self.x, self.sym)

        # Обновляем полотно
        self.canvas.refresh()
