def shellSort(lista):
    n_sublistas = len(lista) // 2
    while n_sublistas > 0:
        for inicial in range(n_sublistas):
            gapInsertionSort(lista, inicial, n_sublistas)
        
        n_sublistas //= 2
        
def gapInsertionSort(lista, inicio, gap):
    for i in range(inicio + gap, len(lista), gap):
        current = lista[i]
        position = i
        
        while position >= gap and lista[position - gap] > current:
            lista[position] = lista[position - gap]
            position -= gap
            
        lista[position] = current
    
    
lista = [64, 75, 6, 57, 99, 27, 0, 96]
shellSort(lista)
print(lista)