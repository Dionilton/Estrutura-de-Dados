#Implementação do tipo de dado abstrato Fila

class Queue:
    
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

#Implementação do tipo de dado abstrato Pilha

class Stack:
    
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)


#Funções
    
def crypto(s):
    #implementação de crypto (médio)
    return s

def deYodafy(w):
    pilha = Stack()
    saida = ''
    chars = '.?!'
    char = ''
    
    if w[len(w) - 1][len(w[len(w) - 1]) - 1] in chars:
        char += w[len(w) - 1][len(w[len(w) - 1]) - 1]
        w[len(w) - 1] = w[len(w) - 1][:len(w[len(w) - 1]) -1]
    
    for i in w:
        pilha.push(i)
    for i in range(len(w)):
        if i == 0:
            saida += pilha.pop()
        else:
            saida += ' ' + pilha.pop()
            
    if len(char) != 0:
        saida += char
        
    return saida
    
def merge(i):
    #implementação de merge (médio)
    return i
    
#Programa principal
    
processos = Queue()

while True:
    comando = input().split()
    
    if comando[0] == 'halt':
        n = processos.size()
        print(f'{n} processo(s) e {n} comando(s) órfão(s).')
        break
    
    elif comando[0] == 'add':
        for i in range(int(comando[1])):
            processo = input().split()
            processos.enqueue(processo)
            
    elif comando[0] == 'process':
        processo = processos.dequeue()
        
        if processo[0] == 'crypto':
            print(crypto(processo[1]))
            
        elif processo[0] == 'deYodafy':
            print(deYodafy(processo[1: ]))
            
        elif processo[0] == 'merge':
            print(merge(processo[1: ]))
            
