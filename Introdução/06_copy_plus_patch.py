from decimal import Decimal
n = int(input())
sum5 = 0
segundos = 0

print(f'Transmitindo {n} bytes...')
while n != 0:
    num = int(input())
    n -= num
    segundos += 1
    sum5 += num
    if segundos % 5 == 0:
        if sum5 != 0:
            seg_i = 0
            tem = 0
            const = sum5/5
            while True:
                if tem >= n:
                    break
                elif (n - tem) > 0:
                    tem = float(Decimal(str(tem)) + Decimal(str(const)))
                    seg_i += 1
            if n != 0:
                print(f'Tempo restante: {seg_i} segundos.')
            sum5 = 0
            
        else:
            print('Tempo restante: pendente...')
print(f'Tempo total: {segundos} segundos.')