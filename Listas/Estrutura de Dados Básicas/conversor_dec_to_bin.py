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
        return self.items[len(sel.items) - 1]
    
    def size(self):
        return len(self.items)
    
def decToBin(dec):
    s = Stack()
    
    while dec > 0:
        s.push(dec % 2)
        dec = dec // 2
    
    bin = ''
    
    while not s.isEmpty():
        bin += str(s.pop())
    
    return bin