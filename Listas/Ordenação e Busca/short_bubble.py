def shortBubble(lista):
    swap = True
    passnum = len(lista) - 1
    while passnum > 0 and swap:
        swap = False
        for i in range(passnum):
            if lista[i] > lista[i+1]:
                swap = True
                lista[i], lista[i+1] = lista[i+1], lista[i]
        passnum -= 1
    
lista = [20,30,40,90,50,60,70,80,100,110]
shortBubble(lista)
print(lista)