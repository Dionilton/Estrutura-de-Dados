def insertionSort(lista):
    for ind in range(1, len(lista)):
        current = lista[ind]
        position = ind
        while position > 0 and lista[position - 1] > current:
            lista[position] = lista[position - 1]
            position -= 1
        
        lista[position] = current
        
        
lista = [54,26,93,17,77,31,44,55,20]
insertionSort(lista)
print(lista)