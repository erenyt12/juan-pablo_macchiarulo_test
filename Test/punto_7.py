# Inicio del programa 
def getOne(una_lista):
    for elemento in una_lista:
        return elemento


def getElements(una_lista):
    for elemento in una_lista:
        yield elemento



if __name__ == "__main__":

    numeros = [1,2,3,4,5]

    devolución = getOne(numeros)

    print(devolución)


    resultado = list(getElements(numeros))

    print(resultado)

    # Fin del programa