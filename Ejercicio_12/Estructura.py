class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales, estructuras_componente=None):
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales
        self.estructuras_componente = estructuras_componente if estructuras_componente else []

    def agregar_estructura_componente(self, estructura):
        self.estructuras_componente.append(estructura)

    def __str__(self):
        componentes = ', '.join([str(estructura.codigo) for estructura in self.estructuras_componente])
        return f"EstructuraArqueologica(codigo={self.codigo}, datacion={self.datacion}, materiales={self.materiales}, estructuras_componente=[{componentes}])"

    class SubEstructura(EstructuraArqueologica):
        def __init__(self, codigo, datacion, materiales, estructuras_componente=None):
            super().__init__(codigo, datacion, materiales, estructuras_componente)