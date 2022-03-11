def fat(n):
    if n == 1:
        return n
    else:
        return n * fat(n - 1)
    
def fat2(n):
    x = 1
    for i in range(n):
        x *= i+1
    return x
    
print(fat2(3000))