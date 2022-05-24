from ast import operator
from datetime import *
import math

class Calculadora:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b
    
    def restar(self):
        return(self.a - self.b)

    def multiplicar(self):
        return(self.a * self.b)

    def dividir(self):
        return(self.a / self.b)
    
    #####

def seno(a):
    return math.sin(a)
        

def coseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)

#####

def numerosPares(a):
    x = 1
    while x <= a:
        if x %2 == 0:
            print(x)
        x = x + 1
            
    
              
            
def registro (operacion, resultado ):
    fecha = datetime.today()
    archivo = open('resgistroCalculadora.txt', 'a')
    archivo.write(f' {fecha} la operacion realizada es: {operacion} y el resultado es: {resultado}\n')
    archivo.close()   
    return (fecha, archivo)   
    
