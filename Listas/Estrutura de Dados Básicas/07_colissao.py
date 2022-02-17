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

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        tmp = self.head
        lstr = ''
        while tmp != None:
            lstr += str(tmp.data) + ' '
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
            count += 1
            current = current.getNext()
            
        return count
    
    def search(self, item):
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
    
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            current = self.head
            previous = None
            for i in range(pos):
                previous = current
                current = current.getNext()
                
            temp_node = Node(item)
            temp = current
            previous.setNext(temp_node)
            previous = previous.getNext()
            previous.setNext(temp)
    
    def popInd(self, pos):
        if pos == 0:
            ret = self.head.getData()
            self.head = self.head.getNext()
        elif pos == self.size():
            return self.pop()
        else:
            current = self.head
            previous = None
            for i in range(pos):
                previous = current
                current = current.getNext()
            ret = current.getData()
            temp = current.getNext()
            previous.setNext(temp)
        
        return ret
          
    def pop(self):
        if self.size() == 1:
            ret = self.head.getData()
            self.head = None
        else:
            current = self.head
            previous = None
            for i in range(self.size() - 2):
                previous = current
                current = current.getNext()
            ret = current.getNext().getData()
            current.setNext(None)
        
        return ret
    
L = UnorderedList()

n_linhas, n_colunas = map(int, input().split())
chaves = input().split()
for i in range(len(chaves)):
    L.append(chaves[i])

matrix = [''] * n_linhas

current = L.head
while current != None:
    if int(current.getData()) < n_linhas:
        matrix[int(current.getData())] += current.getData() + ' '
    else:
        ind = int(current.getData()) % n_linhas
        if len(matrix[ind]) == 0:
            matrix[ind] += current.getData() + ' '
        else:
            matrix[ind] += ' ' + current.getData()
    current = current.getNext()

count = 0
for i in matrix:
    x = i.split()
    if len(i) == 0:
        print(f'{count} - [x]')
    else:
        saida = ''
        for i in range(len(x)):
            if i == 0:
                saida += f'{count} - {x[i]}'
            else:
                saida += f' -> {x[i]}'
        print(saida)
    count += 1

    

'''
current = L.head

for i in range(L.size()):
    ind = current.getData() % n_linhas
    matrix[ind].append(current.getData())
    current = current.getNext()

for i in range(n_linhas):
    if matrix[i] == []:
        print(f'i - [x]')
    else:
        for j in range(len(matrix[i])):
            if i == 0:
                saida = f'{i} - {matrix[i][0]}'
            else:
                saida += f' -> {matrix[i][j]}'
        print(saida)
        
    
'''
    

