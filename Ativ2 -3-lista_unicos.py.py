def elementos_unicos_listas(lista1, lista2):
    conjunto1 = set(lista1)
    conjunto2 = set(lista2)
    elementos_unicos = conjunto1 ^ conjunto2
    return list(elementos_unicos)