
#Variables que registran los numeros que el usuario quiere restar 
variable_1 = int(input("ingrese un numero: "))
variable_2 = int(input("ingrese otro numero: "))

#Funcion
def resta(dato_1: int, dato_2: int):
    """ Esta funcion toma dos datos numericos para restarlos y retornar el resultado. """
    return dato_1 - dato_2
    

resultado = resta(variable_1, variable_2)
print(f"El resultado de la resta es: ",resultado)
