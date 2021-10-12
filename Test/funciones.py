from functools import reduce


def funcionSuma():
    """ Esta funcion toma datos de tipo int para luego sumarlos. """
    #Bandera
    bandera = 0
    cantidad_de_numeros = int(input("Cuantos numeros quiere sumar?: "))
    #Ciclo while
    una_lista = []
    while bandera < cantidad_de_numeros:
        numeros = int(input("ingresar numeros: "))
        una_lista.append(numeros)
        bandera = bandera + 1
        if bandera == cantidad_de_numeros:
            operacion = reduce(lambda x, y: x + y, una_lista)
            print(f"el resultado es: ",operacion)
            break

def funcionResta():
    """ Esta funcion toma datos de tipo int para luego restarlos. """
    #Bandera
    bandera = 0
    cantidad_de_numeros = int(input("Cuantos numeros quiere restar?: "))
    #Ciclo while
    una_lista = []
    while bandera < cantidad_de_numeros:
        numeros = int(input("ingresar numeros: "))
        una_lista.append(numeros)
        bandera = bandera + 1
        if bandera == cantidad_de_numeros:
            operacion = reduce(lambda x, y: x - y, una_lista)
            print(f"el resultado es: ",operacion)
            break
               

        




def funcionDivision():
    """ Esta funcion toma dos valores int para luego dividirlos y mostrar el resultado. """
    dividendo = int(input("ingrese el numero que quiere dividir: "))
    divisor = int(input("ingrese el numero por el cual quiere dividir: "))
    try:
        resultado = dividendo/divisor
        print(resultado)
    except ZeroDivisionError:
        print("no se puede dividir por 0, intentelo de nuevo ")

def funcionMultiplicar():
    """Esta funcion toma dos valores int para luego multiplicarlos y mostrar el resultado.   """
    numero_a_multiplicar = int(input("ingrese el numero que quiere multiplicar: "))
    por_cuanto_multiplicar = int(input("ingrese el numero por el cual lo quiere multiplicar: "))
    resultado = numero_a_multiplicar*por_cuanto_multiplicar
    print(resultado)

# def paresImpares():
#     lista = []
#     pares = []
#     impares = []
#     cantidad_de_numeros = int(input("Cuantos numeros tendra la lista: "))
#     cant = 0
#     while cant < cantidad_de_numeros:
#         numeros = int(input("ingrese un numero: "))
#         lista.append(numeros)
#         cant = cant + 1
#     for i in lista:
#         if i %2 == 0:
#             pares.append(i)
#         else:
#             impares.append(i)
#     print(f"Los numeros pares son: ",pares)
#     print(f"Los numeros impares son: ",impares)

def paresImpares():
    """ Esta funcion recibe 10 numeros y los separa en dos listas de pares e impares """
    variable_1 = 0
    lista_pares = []
    lista_impares = []
    numeros_ingresados = []
    while variable_1 < 10 :
        numeros = int(input("ingresar numero: "))
        numeros_ingresados.append(numeros)
        variable_1 = variable_1 + 1
    for ele in numeros_ingresados:
        if ele %2 == 0:
            lista_pares.append(ele)
        else:
            lista_impares.append(ele)

    print(f"Los numeros pares son: ",lista_pares)
    print(f"Los numeros impares son: ",lista_impares)


def acumulador():
    """ Recibe 6 numeros y verifica que no sean menos o igual a 0 """
    variable = 0
    lista_num = []
    while variable < 6:
        num = int(input("ingrese un numero: "))
        variable = variable +1       
    
        if (num <= 0):
            print(f"El valor ingresado {num} es menor o igual , ingrese otro numero.")
        else:
            lista_num.append(num)
    print("sus numeros son: ", lista_num)        



