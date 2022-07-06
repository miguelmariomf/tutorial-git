#!/usr/bin/python


from file_1 import hola_mundo
import datetime

def saludar(nombre):
    
    lista=hola_mundo()
    resultado=" ".join(lista)+" "+nombre
    return resultado

print(saludar("Lucas"))

def calcular_cumpleaños(fecha):
    hoy=datetime.datetime.now().strftime('%d/%m/%Y')
    hoy=hoy.split("/")
    fecha=fecha.split("/")
    resultado=f'Para tu {abs(int(hoy[2])-int(fecha[2]))} cumpleaños quedan {abs(int(hoy[1])-int(fecha[1]))} meses y {abs(int(hoy[0])-int(fecha[0]))} dias'
    return resultado
    

print(calcular_cumpleaños("02/07/1999"))
