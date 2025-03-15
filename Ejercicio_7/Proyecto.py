class Proyecto:
    """
    Clase que representa un proyecto en el que participo habitualmente.
    """

    def __init__(self, nombre, descripcion, duracion, tecnologias):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion = duracion
        self.tecnologias = tecnologias
        self.participantes = []

    def agregar_participante(self, participante):
        self.participantes.append(participante)

    def __str__(self):
        return f"Proyecto: {self.nombre}\nDescripción: {self.descripcion}\nDuración: {self.duracion} meses\nTecnologías: {', '.join(self.tecnologias)}"

    def lista_participantes(self):
        return f"Participantes: {", ".join(participante.nombre for participante in self.participantes)}"