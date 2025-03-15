class Persona:
    def __init__(self, nombre:str, primer_apellido:str, segundo_apellido:str, f_naci, sexo, dni):
        self.nombre = nombre
        self.apellido = primer_apellido
        self.segundo_apellido = segundo_apellido
        self.fecha_nacimiento = f_naci
        self.sexo = sexo
        self.dni = dni

    def nombre_completo(self):
        return f'{self.nombre} {self.apellido} {self.segundo_apellido}'
    

    def edad(self, current_year):
        birth_year = int(self.fecha_nacimiento.split('/')[2])
        return current_year - birth_year

    def __str__(self):
        return f'Nombre: {self.nombre_completo()}, Fecha de Nacimiento: {self.fecha_nacimiento}, Sexo: {self.sexo}, DNI: {self.dni}'
