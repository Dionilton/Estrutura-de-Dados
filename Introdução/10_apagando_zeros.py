n = int(input())
for i in range(n):
    s = input()
    s = list(s)
    zeros = 0
    
    ind = len(s) - 1
    for i in s[::-1]:
        if s[ind] == '1':
            break
        else:
            s[ind] = '*'
        ind -= 1
    for i in range(len(s)):
        if s[i] == '1':
            break
        else:
            s[i] = '*'
    for i in s:
        if i == '0':
            zeros += 1
    print(zeros)