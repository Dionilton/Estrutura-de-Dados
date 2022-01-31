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
    
def isPalindromo(string):
    d = Deque()
    
    for c in string:
        d.addRear(c)
    
    stillEqual = True
    
    while d.size() > 1 and stillEqual:
        first = d.removeFront()
        last = d.removeRear()
        if first != last:
            stillEqual = False
            
    return stillEqual

print(isPalindromo("lsdkjfskf"))
print(isPalindromo("radar"))