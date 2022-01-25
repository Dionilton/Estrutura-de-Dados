def frequencia(string):
    let = []
    dic = {}
    for i in string:
        if i in let:
            dic[i] += 1
        else:
            dic[i] = 1
            let.append(i)
            
    maior = -1
    char = ''
    for i in let:
        if dic[i] > maior:
            maior = dic[i]
            char = i
    return char