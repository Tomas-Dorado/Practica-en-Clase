class Persona:
    def __init__(self, nombre, apellido, apellido_de_soltera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_de_soltera = apellido_de_soltera
        self.conyuge = None
        self.hijos = []

    def casarse(self, pareja):
        self.conyuge = pareja
        pareja.conyuge = self

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def nombre_completo(self):
        if self.apellido_de_soltera is None:
            return f'{self.nombre} {self.apellido}'
        else:
            return f'{self.nombre} {self.apellido} de soltera {self.apellido_de_soltera}'