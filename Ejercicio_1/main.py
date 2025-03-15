from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Elipse import Elipse

def main():
    figuras = [
        Circulo(radio=5).color("Rojo"),
        Cuadrado(lado=4),
        Elipse(eje_mayor=7, eje_menor=4)
    ]
    
    for figura in figuras:
        print()
        print(figura)

if __name__ == "__main__":
    main()