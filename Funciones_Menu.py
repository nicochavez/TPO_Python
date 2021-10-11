#Funciones Menu paciente
import Funciones_Login
Usuarios = [["hola", "chau"],["holasda", "chau"],["hadfgola", "chau"]]
    
def Menu():
    print("Bienvenido",Nombre[0],"al menu del Doctor Ricardo Thompson")
    print()
    opcion = 0
    while opcion != 4:
        print("1. Sacar turno")
        print("2. Cambiar turno")
        print("3. Cancelar turno")
        print("4. Salir del programa")
        print()
        opcion = int(input("Ingrese la opcion que quiera realizar: "))
        #if opcion == 1:



Nombre = Funciones_Login.LogIn(Usuarios)
Menu()


