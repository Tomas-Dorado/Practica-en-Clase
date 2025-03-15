class Tecnologia:
    """
    Clase que representa una tecnología utilizada en los proyectos.
    """

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo

    def __str__(self):
        return f"Tecnología: {self.nombre} (Tipo: {self.tipo})"