def selection_sort(lista):
    print(f'Passo 0, {lista}')
    for i in range(len(lista)):
        menor = lista[i]
        for j in range(i, len(lista)):
            if lista[j] < menor:
                ind = j
                menor = lista[j]
                lista[i], lista[j] = menor, lista[i]
        print(f'Passo {i + 1}, {lista}')
        
        
def selection_sort2(lista):
    #implementar a selection_sort2
            

lista = [9, 6, 3, 5, 1, 2, 0, 4, 7, 8]
selection_sort(lista)


#Melhorar implementação afim de se obter os seguinte passos na ordenação:

"""
Passo 0, [9, 6, 3, 5, 1, 2, 0, 4, 7, 8]
Passo 1, [0, 6, 3, 5, 1, 2, 9, 4, 7, 8]
Passo 2, [0, 1, 3, 5, 6, 2, 9, 4, 7, 8]
Passo 3, [0, 1, 2, 5, 6, 3, 9, 4, 7, 8]
Passo 4, [0, 1, 2, 3, 6, 5, 9, 4, 7, 8]
Passo 5, [0, 1, 2, 3, 4, 5, 9, 6, 7, 8]
Passo 6, [0, 1, 2, 3, 4, 5, 9, 6, 7, 8]
Passo 7, [0, 1, 2, 3, 4, 5, 6, 9, 7, 8]
Passo 8, [0, 1, 2, 3, 4, 5, 6, 7, 9, 8]
Passo 9, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Passo 10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

"""

