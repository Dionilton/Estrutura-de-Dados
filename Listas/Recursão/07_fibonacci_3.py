n = int(input())
lista = [0] * 35

def fibonacci(n):
    global lista
    lista[n] += 1
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(f'fibonacci({n}) = {fibonacci(n)}.')

for i in range(n + 1):
    print(f'{lista[i]} chamada(s) a fibonacci({i}).')