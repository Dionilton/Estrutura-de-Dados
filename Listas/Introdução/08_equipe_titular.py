n = int(input())
s = input().split()
vec = []
sum_atq = 0
sum_def = 0

for i in range(len(s)):
    vec.append(int(s[i]))

for i in range(len(vec) - 1):
    for j in range((len(vec) - i) - 1):
        if vec[j+1] > vec[j]:
            vec[j+1], vec[j] = vec[j], vec[j+1]

for i in range(len(vec)):
    if i <= 10:
        sum_atq += vec[i]
    else:
        sum_def += vec[i]
    if i == 21:
        break
        
print(sum_atq - sum_def)