def busca_binaria(lista, item):
    if not lista:
        return False
    
    meio = len(lista) // 2
    if lista[meio] == item:
        return True
    elif lista[meio] < item:
        return bisca_binaria(lista[meio + 1:], item)
    else:
        return busca_binaria(lista[:meio], item)

print(busca_binaria([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))