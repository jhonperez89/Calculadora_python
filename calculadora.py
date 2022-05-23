
import funciones as fc
usuario = 1
resultado=0
print(' ')

print('Hola, soy la calculada de Nuevas tecnologias, escriba que funcion quiere realizar')

while usuario != 0:
    print(' ')

    usuario= int((input('1.sumar, 2.restar, 3.multiplicar, 4.dividir, 5.seno, 6.coseno, 7.tangente, 8.NumerosPares, 0.salir: ')))

    print('-----------------------------------------------------------------------------------------')

    if usuario== 'sumar' or usuario == 1 :
        try:
            a=float(input('Escriba el primer numero que desea sumar:'))
            b=float(input('Escriba el segundo numero que desea sumar:'))
            resultado= fc.sumar(a,b)
            fc.registro('suma',resultado)
        except:
            print('por favor valida la informacion')
            

    elif usuario=='restar' or usuario == 2 :
        try:
            a=float(input('Escriba el primer numero que desea restar:'))
            b=float(input('Escriba el segundo numero que desea restar:'))
            resultado = fc.restar(a,b)
            fc.registro('resta',resultado)
        except:
            print('por favor valida la informacion')


    elif usuario=='multiplicar' or usuario == 3:
        try:
            a=float(input('Escriba el numero que desea multiplicar:'))
            b=float(input('Escriba el numero multiplicador:'))
            resultado = fc.multiplicar(a,b)
            fc.registro('multiplicacion',resultado)
        except:
            print('por favor valida la informacion')

            
    elif usuario=='dividir' or usuario == 4:
        try:
            a=float(input('Escriba el numero divisor:'))
            b=float(input('Escriba el numero dividendo:'))
            resultado= round(fc.dividir(a,b),2)
            fc.registro('Division',resultado)
        except:
            print('por favor valida la informacion')

    elif usuario=='seno' or usuario == 5:
        try:
            a=float(input('Escriba el numero de seno:'))
            resultado= fc.seno(a)
            fc.registro('Seno',resultado)
        
        except:
            print('por favor valida la informacion')

    elif usuario=='coseno' or usuario == 6:
        try:
            a=float(input('Escriba el numero del coseno:'))
            resultado= fc.coseno(a)
            fc.registro('Coseno',resultado)
        
        except:
            print('por favor valida la informacion')

    elif usuario=='tangente' or usuario == 7:
        try:
            a=float(input('Escriba el numero de la tangente:'))
            resultado= fc.tangente(a)
            fc.registro('Tangente',resultado)
        
        except:
            print('por favor valida la informacion')

    elif usuario=='NumerosPares' or usuario == 8:
        
         a=int(input('Escriba la cantidad que desea imprimir:'))
         fc.numerosPares(a)
        
            
    else:
        if resultado==0:
            print('')
        else:
            print("No recibimos un dato valido, favor valida la información")
            
            

    print('-----------------------------------------------------------------------------------------')
    if resultado==0:
        print('')
    else:
        print(f'El resultado es de la operacion {usuario} es: {resultado}')
    

    print(' ')
print('****************Gracias por utilizar nuestra calculadora***********************************')
print(' ')
       
        
        



