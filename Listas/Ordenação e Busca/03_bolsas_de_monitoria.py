n = int(input())
lista = []
for i in range(n):
    lista.append(float(input()))

for i in range(1, n):
    current = lista[i]
    ind = i
    while ind > 0 and lista[ind - 1] < current:
        lista[ind] = lista[ind - 1]
        ind -= 1
    
    lista[ind] = current
    
for i in lista:
    print(f'{i:.2f}')