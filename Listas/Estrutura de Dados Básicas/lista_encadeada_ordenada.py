class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNexr(self):
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
    
    
    
