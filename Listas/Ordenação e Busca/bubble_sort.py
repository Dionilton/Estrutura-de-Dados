def bubbleSort(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if lista[j] > lista[j +1]:
                lista[j], lista[j +1] = lista[j + 1], lista[j]

lista = [54,26,93,17,77,31,44,55,20]
bubbleSort(lista)
print(lista)