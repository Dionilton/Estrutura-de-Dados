n = int(input())
lista = []
for i in range(n):
    nome = input()
    t1, t2, t3 = map(float, input().split())
    tt = t1 + t2 + t3
    lista.append((nome, tt))
    
    
for i in range(1, len(lista)):
    current = lista[i]
    position = i
    while position > 0 and lista[position - 1][1] > current[1]:
        lista[position] = lista[position - 1]
        position -= 1
        
    lista[position] = current
    
for i in range(len(lista)):
    m = int(lista[i][1] // 60)
    s = lista[i][1] % 60
    mm = lista[i][1] % 1
    mm = float(f'{mm:.3f}')
    mm = int(mm * 1000)
    s = int(s)
    
    print(f'{i + 1}. {lista[i][0]} ({m}:{s:02}.{mm:03})')