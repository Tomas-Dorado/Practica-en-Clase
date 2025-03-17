from Circulo import Circulo
from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Elipse import Elipse

def main():
    figuras = [
        Circulo(radio=5),
        Rectangulo(ancho=3, alto=4).color("blue"),
        Cuadrado(lado=4).color("green"),
        Elipse(eje_mayor=7, eje_menor=4).color("yellow")
    ]
    
    for figura in figuras:
        print()
        print(figura)

if __name__ == "__main__":
    main()

    import matplotlib.pyplot as plt
    import matplotlib.patches as patches

    def dibujar_figuras(figuras):
        fig, ax = plt.subplots()
        for figura in figuras:
            if isinstance(figura, Circulo):
                circle = patches.Circle((0.5, 0.5), figura.radio, color=figura.color)
                ax.add_patch(circle)
            elif isinstance(figura, Cuadrado):
                square = patches.Rectangle((0.25, 0.25), figura.lado, figura.lado, color=figura.color)
                ax.add_patch(square)
            elif isinstance(figura, Rectangulo):
                rectangle = patches.Rectangle((0.25, 0.25), figura.ancho, figura.alto, color=figura.color)
                ax.add_patch(rectangle)
            elif isinstance(figura, Elipse):
                ellipse = patches.Ellipse((0.5, 0.5), figura.eje_mayor, figura.eje_menor, color=figura.color)
                ax.add_patch(ellipse)
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.show()

    dibujar_figuras(figuras)