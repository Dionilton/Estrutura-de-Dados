count = 0
def fib(n):
    count += 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


n = int(input())
print(fib(n))
print(count)