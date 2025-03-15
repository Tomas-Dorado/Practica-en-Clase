from Proyecto import Proyecto

class Participante:
    """
    Clase que representa a un participante en un proyecto.
    """

    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia
        self.proyectos = []

    def asignar_proyecto(self, proyecto:Proyecto):
        self.proyectos.append(proyecto)
        proyecto.agregar_participante(self)


    def __str__(self):
        return f"Participante: {self.nombre}\nRol: {self.rol}\nExperiencia: {self.experiencia} años"

    def lista_proyectos(self):
        return f"Proyectos: {', '.join([proyecto.nombre for proyecto in self.proyectos])}"