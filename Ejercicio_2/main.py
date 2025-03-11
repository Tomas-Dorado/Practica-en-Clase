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

class Familia:
    def __init__(self, apellido):
        self.apellido = apellido
        self.miembros = []

    def agregar_miembro(self, persona):
        self.miembros.append(persona)

# Crear personas
kate = Persona("Kate", "Windsor", "Middleton")
guillermo = Persona("Guillermo", "Windsor")
carlos = Persona("Carlos", "Windsor")
diana = Persona("Diana", "Gales", "Spencer")

# Crear familias
familia_windsor = Familia("Windsor")
familia_gales = Familia("Gales")

# Agregar miembros a las familias
familia_windsor.agregar_miembro(kate)
familia_windsor.agregar_miembro(guillermo)
familia_windsor.agregar_miembro(carlos)
familia_gales.agregar_miembro(diana)

# Establecer relaciones
guillermo.casarse(kate)
carlos.agregar_hijo(guillermo)
diana.agregar_hijo(guillermo)