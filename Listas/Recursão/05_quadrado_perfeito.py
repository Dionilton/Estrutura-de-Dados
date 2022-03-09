def sum(lista):
    if len(lista) == 2:
        print(f'{lista[0]} + soma({lista[1:]})')
        return lista[0] + sum(lista[1:])
    elif len(lista) == 1:
        print(lista[0])
        return lista[0]
    else:
        print(f'{lista[0]} + soma({lista[1:]})')
        return lista[0] + sum(lista[1:])
    
n = int(input())
lista = []
for i in range(n):
    lista.append((2*(i+1)) - 1)
    
sum_l = sum(lista)

print('-' * 15)
print(f'{n} ** 2 == {sum_l}')