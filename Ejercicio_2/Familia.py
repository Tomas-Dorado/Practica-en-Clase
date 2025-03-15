class Familia:
    def __init__(self, apellido):
        self.apellido = apellido
        self.miembros = []

    def agregar_miembro(self, persona):
        self.miembros.append(persona)

    def mostrar_miembros(self):
        for miembro in self.miembros:
            print(f'{miembro.nombre} {self.apellido}')