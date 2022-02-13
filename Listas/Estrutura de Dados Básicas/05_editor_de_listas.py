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



while True:
    n = input().split()
    
    if n[0] == 'X':
        break
    
    elif n[0] == 'I':
        L.add(int(n[1]))
        
    elif n[0] == 'F':
        L.append(int(n[1]))
        
    elif n[0] == 'P':
        print(L.pop())
        
    elif n[0] == 'D':
        print(L.popInd(0))
        
    elif n[0] == 'V':
        count = 0
        while L.search(int(n[1])):
            L.remove(int(n[1]))
            count += 1
        print(count)
        
    elif n[0] == 'E':
        print(L.popInd(int(n[1]) - 1))
        
    elif n[0] == 'T':
        current = L.head
        while True:
            if current.getData() == int(n[1]):
                current.setData(int(n[2]))
                break
            else:
                current = current.getNext()
                
    elif n[0] == 'C':
        current = L.head
        count = 0
        while current != None:
            if current.getData() == int(n[1]):
                count += 1
            current = current.getNext()
        print(count)
    
    #print(f'A lista atual é: {L}')
        
    
print()

current = L.head

while current != None:
    print(current.getData())
    current = current.getNext()