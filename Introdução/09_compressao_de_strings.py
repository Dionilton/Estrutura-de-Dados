n = int(input())
numeros = '0123456789'
for i in range(n):
    char = ''
    n_vezes_str = ''
    controle = False
    saida = ''
    string = input()
    string += '\n'
    char = string[0]
    for j in string:
        if j not in numeros and controle:
            n_vezes_int = int(n_vezes_str)
            saida += char * n_vezes_int
            char = j
            n_vezes_str = ''
        else:
            if controle:
                n_vezes_str += j
            controle = True
            
    print(saida)