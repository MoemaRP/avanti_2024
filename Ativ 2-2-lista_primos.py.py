def lista_so_primos(lista_de_numeros):
    def so_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    numeros_primos = []
    for numero in lista_de_numeros:
        if so_primo(numero):
            numeros_primos.append(numero)
    return numeros_primos


##lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
##resultado = lista_so_primos(lista_original)
##print(resultado)  # Saída: [2, 3, 5, 7, 11]
