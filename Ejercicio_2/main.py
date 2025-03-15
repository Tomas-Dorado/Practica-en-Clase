from Familia import Familia
from Persona import Persona

def main():
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
    carlos.casarse(diana)

    # Mostrar información de las familias
    print("Familia Windsor:")
    familia_windsor.mostrar_miembros()

    print("\nFamilia Gales:")
    familia_gales.mostrar_miembros()

    # Mostrar relaciones
    print("\nRelaciones:")
    print(f"{guillermo.nombre_completo()} está casado con {guillermo.conyuge.nombre_completo()}")
    print(f"{carlos.nombre_completo()} está casado con {diana.nombre_completo()}")
    print(f"{carlos.nombre_completo()} es padre de {guillermo.nombre_completo()}")
    print(f"{diana.nombre_completo()} es madre de {guillermo.nombre_completo()}")

if __name__ == "__main__":
    main()