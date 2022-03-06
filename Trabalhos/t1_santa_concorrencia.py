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
    
    def __init__(self):
        self.head = None
        
    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data)
            tmp = tmp.getNext()
        
        return lstr
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        
        return count
    
    def serach(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
                
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
             
    def append(self, item):
        if self.size() == 0:
            self.add(item)
        else:
            temp = Node(item)
            current = self.head
            previous = None
            found = False
            while not found:
                if current == None:
                    previous.setNext(temp)
                    found = True
                else:
                    previous = current
                    current = current.getNext()
                    
    def index(self, item):
        count = 0
        current = self.head
        while True:
            if current.getData() == item:
                break
            else:
                current = current.getNext()
                count += 1
                
        return count
    
    def pop(self):
        if self.size == 1:
            ret = self.head.getData()
            self.head = None
        else:
            current = self.head
            for i in range(self.size() - 2):
                current = current.getNext()
            ret = current.getNext().getData()
            current.setNext(None)
            

#Funções

def sort(lista):
    for i in range(len(lista) - 1):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
def crypto(s):
    alg = [9,8,7,6,5,4,3,2,1]
    lista = UnorderedList()
    plus = False
    for i in range(len(s)):
        if i == 0:
            if s[i] == '+':
                lista.append(alg.pop())
                lista.append(alg.pop())
                last_plus = lista.head.getNext()
                plus = True
            elif s[i] == '-':
                lista.add(alg.pop())
                lista.add(alg.pop())
        else:
            if s[i] == '+':
                lista.append(alg.pop())
                last_plus = lista.head
                for j in range(lista.size() - 1):
                    last_plus = last_plus.getNext()
                plus = True
            elif s[i] == '-' and plus:
                current = lista.head
                previous = None
                found = False
                while not found:
                    if current.getData() == last_plus.getData():
                        found = True
                    else:
                        previous = current
                        current = current.getNext()
                        
                temp = Node(alg.pop())
                temp.setNext(current)
                previous.setNext(temp)
                last_plus = previous.getNext()
            elif s[i] == '-' and not plus:
                lista.add(alg.pop())
            
    return lista

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
    sort(i)
    
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
        if processos.size() != 0:
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
        else:
            continue
    
# observações e casos de teste a serem resolvidos:

"""
Dos 13 casos de teste o atual código não passou em 3, nos quais a maioria é devido a alguma
falha na implementação da função merge() que retorna valores divergentes do resultaddo esperado

"""

#casos de testes falhos:

# Caso 01:

"""

Entrada:

process
halt

Resultado esperado:

0 processo(s) e 0 comando(s) órfão(s).

Resultado do meu código:

*** Answer Error! ***
Line: 15
IndexError: pop from empty list

"""

# Caso 02:

"""

Entrada:

add 1
merge [-5, 5] [13, 42] [10, 100]
process
add 2
merge [1, 2] [2, 3] [3, 4] [4, 5]
merge [4, 5] [2, 3] [1, 2] [3, 4]
process
halt

Resultado esperado:

[-5, 5] [10, 100]
[1, 5]
1 processo(s) e 1 comando(s) órfão(s).

Resultado do meu código:

*** Answer Error! ***
Line: 242
IndexError: list index out of range

"""

# Caso 03:

"""

Entrada:

add 3
crypto +--+
deYodafy nossa bossa?
merge [1, 2] [2, 2] [2, 3] [3, 4]
process
process
process
halt

Resultado esperado:

14325
bossa nossa?
[1, 4]
0 processo(s) e 0 comando(s) órfão(s).

Resultado do meu código:

14325
bossa nossa?
[1, 2] [2, 4]
0 processo(s) e 0 comando(s) órfão(s).

"""


            
