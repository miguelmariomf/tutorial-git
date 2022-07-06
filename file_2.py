#!/usr/bin/python

from file_1 import hola_mundo

def saludar(nombre):
    
    lista=hola_mundo()
    cad=""
    for d in lista:
        cad=cad+" "+d
    return f'{cad} {nombre}'

print(saludar("Lucas"))