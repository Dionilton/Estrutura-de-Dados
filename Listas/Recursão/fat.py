n = int(input())
total = 0
c = 0
r = 0
s = 0

for i in range(n):
    dados = input().split()
    num = int(dados[0])
    tipo = dados[1]
    if tipo == 'C':
        c += num
    elif tipo == 'R':
        r += num
    elif tipo == 'S':
        s += num
    
    total += num
    
print(f"Total: {total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print(f"Percentual de coelhos: {((100*c)/total):.2f}")
print(f"Percentual de ratos: {((100*r)/total):.2f}")
print(f"Percentual de sapos: {((100*s)/total):.2f}")

#Exercício URI