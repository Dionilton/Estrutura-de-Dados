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
    
#Implementação da classe Node

class Node:
    
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext

#Implementação do tipo abtrato Lista Desordenada
        
class UnorderedList:
    
    def __ini__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head = None
    
    

#Funções

def bubbleSort(alist): #implementar bubblesort
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    
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
    for ind in range(len(i)):
        i[ind] = i[ind].replace('[','')
        i[ind] = i[ind].replace(']','')
        i[ind] = i[ind].replace(',','')
        i[ind] = int(i[ind])
    bubbleSort(i)
    
    saida = f'[{i[0]}, {i[3]}] [{i[4]}, {i[7]}]'
        
    return saida
    
#Programa principal
    
processos = Queue()

while True:
    comando = input().split()
    
    if comando[0] == 'halt':
        n_processos = processos.size()
        n_comandos = 0
        for i in processos.items:
            n_comandos += i.size()
        print(f'{n_processos} processo(s) e {n_comandos} comando(s) órfão(s).')
        break
    
    elif comando[0] == 'add':
        fila = Queue()
        for i in range(int(comando[1])):
            processo = input().split()
            fila.enqueue(processo)
            
        processos.enqueue(fila)
            
    elif comando[0] == 'process':
        fila_processos = processos.dequeue()
        processo = fila_processos.dequeue()
        if fila_processos.size() != 0:
            processos.enqueue(fila_processos)
        
        if processo[0] == 'crypto':
            print(crypto(processo[1]))
            
        elif processo[0] == 'deYodafy':
            print(deYodafy(processo[1: ]))
            
        elif processo[0] == 'merge':
            print(merge(processo[1: ]))
            
