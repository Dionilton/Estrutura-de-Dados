def selection_sort(lista):
    for i in range(len(lista)):
        menor = lista[i]
        for j in range(i, len(lista)):
            if lista[j] < menor:
                ind = j
                menor = lista[j]
                lista[i], lista[j] = menor, lista[i]
        
            

lista = [54,26,93,17,77,31,44,55,20]
selection_sort(lista)
print(lista)

