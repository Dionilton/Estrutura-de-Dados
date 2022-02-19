class Deque:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def addFront(self, item):
        self.items.append(item)
        
    def addRear(self, item):
        self.items.insert(0, item)
        
    def removeFront(self):
        return self.items.pop()
    
    def removeRear(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)
    

def isPalindromo(palavra: Deque()):
    iguais = True
    
    while palavra.size() > 1 and iguais:
        primeiro = palavra.removeFront()
        ultimo = palavra.removeRear()
        if primeiro != ultimo:
            iguais = False
    return iguais

palavras = input().split()

for i in palavras:
    n = 3
    palin_01 = False
    palin_02 = False
    while len(i) - n > 0 or not palin_01 and not palin_02:
        d = Deque()
        for j in range(n):
            d.addFront(i[j])
        if isPalindromo(d):
            palin_01 = True
        ind = n
        for j in range(len(i) - n):
            d.removeRear()
            d.addFront(i[ind])
            if isPalindromo(d) and palin_01:
                palin_02 = True
                palin = True
                break
            elif isPalindromo(d) and not palin_01:
                palin_01 = True
            ind += 1
        n += 1
        if palin:
            print(i)
            break
    
    


"""
Dar um split na entrada
depois faz um for interando a lista do split
analisa item por item
se a palavrar for 2-palíndromo (parte mais "difícil", validar se a palavra é 2-palíndromo)
retorna/print a palavra

"""