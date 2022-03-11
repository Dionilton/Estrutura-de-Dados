def fat(n):
    x = 1
    for i in range(n):
        x *= i+1
    return x

n = int(input())
for i in range(n):
    lista = []
    f = int(input())
    for j in range(f + 1):
        if j < 7:
            lista.append(fat(j))
        else:
            lista.append(fat(j) % 2357)
    
    saida = ''
    
    for i in range(len(lista) - 1):
        saida += f'{lista[i]} '
    
    saida += f'{lista[len(lista) - 1]}'
    
    print(saida)