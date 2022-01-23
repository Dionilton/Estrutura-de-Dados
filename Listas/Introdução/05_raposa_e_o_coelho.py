import math
escapar = False
n = int(input())
coelho_x, coelho_y = map(float, input().split())
raposa_x, raposa_y = map(float, input().split())

for i in range(n):
    buraco_x, buraco_y = map(float, input().split())
    dis_coelho = math.sqrt(((coelho_x - buraco_x) ** 2) + ((coelho_y - buraco_y) ** 2))
    dis_raposa = math.sqrt(((raposa_x - buraco_x) ** 2) + ((raposa_y - buraco_y) ** 2))
    if not escapar:
        if dis_raposa > dis_coelho * 2:
            escapar = True
            x, y = buraco_x, buraco_y
if escapar:
    print(f'O coelho pode escapar pelo buraco ({x:.3f}, {y:.3f}).')
else:
    print('O coelho nao pode escapar.')
