import sys
sys.setrecursionlimit(10000)

def mdc(q1, q2, maior):
    if q1 % maior == 0 and q2 % maior == 0:
        return maior
    else:
        return mdc(q1, q2, maior - 1)
    
q1, q2 = map(int, input().split())
print(mdc(q1, q2, max(q1, q2)))