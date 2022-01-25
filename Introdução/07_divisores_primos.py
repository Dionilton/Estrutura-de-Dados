def eh_primo(n):
    primo = True
    for i in range(n):
        if n % (i+1) == 0 and i+1 != 1 and i+1 != n:
            primo = False
    if primo:
        return True
    else:
        return False

def primos_gemeos(n):
    lista = []
    num = 5
    
    for i in range(n):
        while True:
            if eh_primo(num) and eh_primo(num-2):
                lista.append((num-2, num))
                num += 1
                break
            else:
                num += 1
        
    return lista