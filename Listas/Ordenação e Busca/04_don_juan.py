n = int(input())
lista = []
for i in range(n):
    lista.append(input())
    
for i in range(1, n):
    current = lista[i]
    position = i
    while position > 0 and len(lista[position - 1]) > len(current):
        lista[position] = lista[position - 1]
        position -= 1
        
    lista[position] = current
    
print(lista)

#fazer um while para fazer pop dos 2 últimos itens da lista caso o len(item) forem iguais