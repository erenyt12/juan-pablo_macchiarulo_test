""" a- Crear un programa en el cual el usuario tenga un menu que pueda realizar 
   las operaciones matematicas basicas (suma, resta, division, multiplicacion). 

    Ejemplo: 

            Menu
        1- suma
        2- resta
        3- division
        4- multiplicacion

   b- Extender el ejercio anterior, modularizando en funciones cada bloque de codigo 
      asociado a cada una de las opciones, definir dichas funciones en un archivo 
      a parte e importalas para hacer uso de ellas. 

   c- Extienda ahora el ejercicio agregando dos opciones al menu: 
         Menu
        1- suma
        2- resta
        3- division
        4- multiplicacion
        5- pares e impares 
        6- acumulador

      Descripcion: 
        - pares e impares: debe ingresar 10 numeros por consola e imprimir dos colecciones
          la coleccion de pares y la coleccion de impares.
        
        - acumulador: ingrese 6 numeros por consola los cuales debe validar que sean mayor a 0, 
          en el caso de que ingresara 0 o un numero negativo debera imprimir el siguiente mensaje:

              "El numero ingresado es menor a 0 vuelva a intentarlo"

    d- Extienda el ejercicio para que ahora la funcion division lance una excepcion en el caso que 
       el divisor sea 0, luego maneje la excepcion donde este llamando dicha funcion.
 """


from funciones import funcionSuma, funcionResta, funcionDivision, funcionMultiplicar, paresImpares, acumulador


continuar = True

print("""               Menu
         Menu
        1- suma
        2- resta
        3- division
        4- multiplicacion
        5- pares e impares 
        6- acumulador
        7- salir del sistema """)
while continuar:

    opcion = int(input("ingrese una opcion: "))
    if opcion == 1:
        funcionSuma()
    elif opcion == 2:
        funcionResta()
    elif opcion == 3:
        funcionDivision()
    elif opcion == 4:
        funcionMultiplicar()
    elif opcion == 5:
        paresImpares()
    elif opcion == 6:
        acumulador()
    elif opcion == 7:
        print("saliendo del programa...")
        continuar = False
    else:
        print("no se encuentra la opcion: ",opcion,",intentelo de nuevo")
        