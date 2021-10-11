import time
import re
import calendar

def sacar_fecha():#Utilizamos la funcion time para saber la fecha actual y "re" para sacar solo los numeros
    tiempo = str(time.localtime())
    lista_tiempo = re.findall(r'\d+', tiempo)
    fecha = lista_tiempo[0:5]
    return fecha
def calendario(fecha):
    año = int(fecha[0])
    mes = int(fecha[1])
    calendario = calendar.TextCalendar(calendar.MONDAY)
    matriz_calendario = calendario.monthdayscalendar(año, mes)
    return matriz_calendario

def mostrarMatriz(matriz): #Muestra la matriz por filas y columnas
    for i in range (len(matriz)):
        print(matriz[i])
def lista_horarios(fecha):
    print("Para el dia", fecha[2], "se encuentran estos horarios disponibles: ")

fecha_actual = sacar_fecha()
calendario_matriz = calendario(fecha_actual)
mostrarMatriz(calendario_matriz)


