def encontrar_segundo_maior(lista):
    if len(lista) < 2:
        return None
    lista_unica = list(set(lista))
    lista_ordenada = sorted(lista_unica, reverse=True)
    if len(lista_ordenada) < 2:
        return None
    return lista_ordenada[1]

