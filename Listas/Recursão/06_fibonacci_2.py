def fibonacci(n):
    lista = []
    for i in range(n):
        lista.append(fib(i))
    
    return lista
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
print(fibonacci(19))