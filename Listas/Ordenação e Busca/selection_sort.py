def selection_sort(lista):
    for i in range(len(lista)):
        menor = lista[i]
        swap = False
        for j in range(i, len(lista)):
            if lista[j] < menor:
                swap = True
                ind = j
                menor = lista[j]
        if swap:
            lista[i], lista[j] = menor, lista[i]
        
            

lista = [54,26,93,17,77,31,44,55,20]
selection_sort(lista)
print(lista)

#terminar implementação do selection sort e corrigir bugs de lógica