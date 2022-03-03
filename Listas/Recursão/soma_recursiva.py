def soma(lista_numeros):
    if len(lista_numeros) == 1:
        print(lista_numeros)
        return lista_numeros[0]
    else:
        print(lista_numeros)
        return lista_numeros[0] + soma(lista_numeros[1:])
    
print(soma([1,3,5,7,9,11,13,15,17,19]))