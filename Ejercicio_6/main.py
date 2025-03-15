from Persona import Persona

def main():
    persona = Persona("Juan", "Pérez", "Velazquez", "01/01/1990","Masculino", "12345678A")
    print(persona)
    print(persona.nombre_completo())
    print(persona.edad(2021))

if __name__ == "__main__":
    main()