def soma(lista_numeros):
    if len(lista_numeros) == 1:
        return lista_numeros[0]
    else:
        return lista_numeros[0] + soma(lista_numeros[1:])
    
print(soma([1,3,5,7,9]))