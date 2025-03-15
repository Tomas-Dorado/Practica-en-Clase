from Proyecto import Proyecto
from Miembros import Participante
from Tecnologia import Tecnologia

# Ejemplo de uso
if __name__ == "__main__":
    tecnologias = [Tecnologia("Python", "Lenguaje de Programación"), Tecnologia("Django", "Framework")]
    proyecto = Proyecto("Sistema de Gestión", "Un sistema para gestionar recursos", 12, [tec.nombre for tec in tecnologias])
    participante1 = Participante("Juan Pérez", "Desarrollador", 5)
    participante1.asignar_proyecto(proyecto)
    participante2 = Participante("María López", "Diseñadora", 3)
    participante2.asignar_proyecto(proyecto)

    print(proyecto.lista_participantes())