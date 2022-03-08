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
            lstr += ' ' + str(tmp.data)
            tmp = tmp.getNext()
        lstr = lstr[1:]
        
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
            if lista[j][0] > lista[j + 1][0]:
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
    
    ret = ''
    current = lista.head
    for i in range(lista.size()):
        ret += str(current.getData())
        current = current.getNext()
            
    return ret

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
        
    lista_i = []
        
    for j in range(int(len(i) / 2)):
        pair = [i[j+j], i[j+j+1]]
        lista_i.append(pair)
    
    sort(lista_i)
    
    lista_d = UnorderedList()
    
    for j in range(len(lista_i)):
        lista_d.append(lista_i[j])
        
    current = lista_d.head.getNext()
    previous = lista_d.head
    
    change = False
    
    while current != None:
        if current.getData()[1] <= previous.getData()[1]:
            previous.setNext(current.getNext())
            current = previous.getNext()
            
        elif current.getData()[0] <= previous.getData()[1]:
            controle = False
            temp = [previous.getData()[0], current.getData()[1]]
            if current.getNext() == None:
                controle = True
            lista_d.remove(previous.getData())
            lista_d.remove(current.getData())
            if controle:
                lista_d.append(temp)
            else:
                lista_d.add(temp)
            previous = lista_d.head
            currunt = previous.getNext()
            
        else:
            previous = current
            current = current.getNext()
        
        
    return lista_d
    
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
        