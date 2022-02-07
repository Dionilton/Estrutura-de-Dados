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
    def __inti__(self):
        self.head = None
        
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

