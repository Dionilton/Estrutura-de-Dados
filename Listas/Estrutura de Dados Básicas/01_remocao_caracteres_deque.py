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
    
string = input()

deque = Deque()
saida = ''
alphabeta = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ <>:?,.;/°\|!@#$%¨&()-/'
numeros = '0123456789'


for i in string:
    if i in alphabeta:
        deque.addFront(i)
    elif i in numeros:
        deque.addRear(i)
    if not deque.isEmpty():
        if i == '*':
            saida += deque.removeFront()
        elif i == '+':
            saida += deque.removeRear()
        
print(saida)