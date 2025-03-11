class Circulo(color):
    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    def area(self):
        return 3.1416 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.1416 * self.radio