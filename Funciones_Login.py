#Funciones Registro y LogIn

def listas(): #Crea una lista
    usuario = []
    return usuario

def verificar_repetido(usuario, Lista_usuario, existente): #Verifica que el usuario creado no exista
    for i in range(len(Lista_usuario)): #recorre los usuarios(sub[0])
        existente = False
        if usuario == Lista_usuario[i][0]:
            existente = True
            break
    return existente

verificar_edad = lambda años: años >= 18 #Valida que el usuario sea mayor de 18 años
    

def registro_usuarios(Lista_usuario): #Registra todos los datos del usuario en la lista
    
    repetido = True
    mayor = False
    contador_edad = 0 
    turno = 0 #Acá hacer tupla o cola
    
    while repetido == True: #Ingresa usuario y llama a funcion para verificar que no se repita
        usuario = str(input("Ingrese un nombre de usuario para registrarse o 'Volver' para regresar al menu: "))
        '''if usuario == "Volver":
        Agregar retorno a menu'''
        repetido = verificar_repetido(usuario, Lista_usuario, repetido)
     
    contraseña = str(input("Ingrese una contraseña para el usuario creado: "))
    nombre = str(input("Ingrese su nombre y apellido: "))
    dni = int(input("Ingrese su dni: ")) #Validacion de int
    edad = int(input("Ingrese su edad, debe ser mayor para poder validar su registro: "))
    for i in range(3):
        Verificacion = verificar_edad(edad)
        if Verificacion == True:
            i = 3
            Lista_usuario.append([usuario, contraseña, nombre, dni, edad, turno])
        elif i < 2:
            edad = int(input("Ingrese su edad, debe ser mayor para poder validar su registro: "))
    if Verificacion == False:
        print("Usted no puede registrarse debdido a que es menor de edad")
            
def LogIn(Lista_usuarios):
    contraseña = ""
    intentos = 0
    NombreUsuario = str(input("Ingrese su nombre de usuario: "))
    for i in range(len(Lista_usuarios)):
        if NombreUsuario == Lista_usuarios[i][0]:
            usuario = i
    while contraseña != Lista_usuarios[usuario][1]:
        contraseña = str(input("Ingrese su contraseña: "))
        intentos +=1
        if contraseña != Lista_usuarios[usuario][1]:
            print("La contraseña ingresada es incorrecta")
        if intentos > 3:
            print("Ha alcanzado la cantidad maxima de intentos, no podra iniciar sesion")
            break
            return -1
    
    return Lista_usuarios[usuario]
    
            



'''usuarios = listas()
registro_usuarios(usuarios)
print(usuarios)'''
    