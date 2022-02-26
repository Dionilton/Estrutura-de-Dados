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
        

class OrderedList:
    def __init__(self):
        self.head = None
        
    def __str__(self):
        temp = self.head
        lstr = ''
        while temp != None:
            lstr += str(temp.data) + ' '
            temp = temp.getNext()
            
        return lstr
    
    def isEmpty(self):
        return self.head == None
    
    def search(self, item):
        current = self.head
        found = False
        stop = False
        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext()
        
        return found
    
    def add(self, item):
        current = self.head
        previous = None
        stop = False
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext()
                
        temp = Node(item)
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else:
            temp.setNext(current)
            previous.setNext(temp)
            
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
            
        return count
    
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
        
        
L = OrderedList()
L.add(5)
L.add(8)
L.add(2)
L.add(6)
print(L)
L.remove(6)
print(L)
print(L.size())
print(L.search(8))
print(L.search(2))
print(L.search(18))
print(L.isEmpty())
L.remove(8)
L.remove(2)
print(L)
L.remove(5)
print(L.isEmpty())

    
