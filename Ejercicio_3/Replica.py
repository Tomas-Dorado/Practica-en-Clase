from ObraDeArte import ObraDeArte


class Replica(ObraDeArte):
    def __init__(self, titulo, autor, adscripcion_cronologica, tecnica, sub_tecnica, material_soporte, descripcion, original):
        super().__init__(titulo, autor, adscripcion_cronologica, tecnica, sub_tecnica, material_soporte, descripcion)
        self.original = original