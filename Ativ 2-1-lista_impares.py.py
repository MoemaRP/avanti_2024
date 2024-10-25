def lista_so_impares(lista_de_numeros):
 
    numeros_impares = []
    for numero in lista_de_numeros:
        if numero % 2 != 0:
            numeros_impares.append(numero)
    return numeros_impares