import os

def main():
    while True:
        print("Seleccione el ejercicio que desea realizar:")
        for i in range(1, 11):
            print(f"{i}. Ejercicio {i}")
        print("11. Salir")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion in [str(i) for i in range(1, 11)]:
            os.system(f'python /workspaces/Practica-en-Clase/Ejercicio_{opcion}/main.py')
        elif opcion == "11":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
