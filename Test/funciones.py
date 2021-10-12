from functools import reduce


def funcionSuma():
    """ Esta funcion toma datos de tipo int para luego sumarlos. """
    #Bandera
    bandera = True
    #Ciclo while
    while bandera:
        #Ingreso de numero para confirmacion
        x = input("precione la letra a para continuar: ")
        #ciclo if con while para poder sumar varios numeros
        if x == 'a' :
            una_lista = []
            continuar = True
            print("precione el numero 0 para sumar")
            while continuar :
                valor = int(input("agregar numero: "))
                una_lista.append(valor)
                if valor == 0:
                    operacion = reduce(lambda x, y: x + y, una_lista)
                    print(f"el resultado es: ",operacion)
                    break
                bandera = False
        else:
            print("ingrese el numero correcto...")


def funcionResta():
    """ Esta funcion toma datos de tipo int para luego sumarlos. """
    #Bandera
    bandera = True
    #Ciclo while
    while bandera:
        #Ingreso de numero para confirmacion
        x = input("precione la letra a para continuar: ")
        #ciclo if con while para poder sumar varios numeros
        if x == 'a' :
            una_lista = []
            continuar = True
            print("precione el numero 0 para restar")
            while continuar :
                valor = int(input("agregar numero: "))
                una_lista.append(valor)
                if valor == 0:
                    operacion = reduce(lambda x, y: x - y, una_lista)
                    print(f"el resultado es: ",operacion)
                    break
                bandera = False
    

def funcionDivision():
    dividendo = int(input("ingrese el numero que quiere dividir: "))
    divisor = int(input("ingrese el numero por el cual quiere dividir: "))
    resultado = dividendo/divisor
    print(resultado)
def funcionMultiplicar():
    numero_a_multiplicar = int(input("ingrese el numero que quiere multiplicar: "))
    por_cuanto_multiplicar = int(input("ingrese el numero por el cual lo quiere multiplicar: "))
    resultado = numero_a_multiplicar*por_cuanto_multiplicar
    print(resultado)