import os

def main():
    while True:
        print("Seleccione el ejercicio que desea realizar:")
        print("1. Ejercicio 1")
        print("2. Ejercicio 2")
        print("3. Salir")
        
        opcion = input("Ingrese el número de la opción: ")
        
        if opcion == "1":
            os.system('python /workspaces/Pr-ctica-en-Clase/Ejercicio_1/main.py')
        elif opcion == "2":
            os.system('python /workspaces/Pr-ctica-en-Clase/Ejercicio_2/main.py')
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")
        if opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()