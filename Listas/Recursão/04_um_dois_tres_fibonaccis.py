count = 0
def fib(n):
    global count
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input())
fib_n = fib(n)
print(f'Fib({n}) = {fib_n} ({count} chamadas)')