class Cuadrado:
    def __init__(self, lado, color):
        self.color = color
        self.lado = lado

    def area(self):
        return self.lado * self.lado

    def perimetro(self):
        return self.lado * 4