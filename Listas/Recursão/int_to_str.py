def toStr(n, base):
    convStr = '0123456789ABCDEF'
    if n < base:
        return convStr[n]
    else:
        return toStr(n // base, base) + convStr[n%base]

print(toStr(10, 2))