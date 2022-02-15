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
    
n = int(input())
d = Deque()
janela = input().split()
k = int(input())
saida = []


for i in range(n):
    janela[i] = int(janela[i])
  
max = 0
for i in range(len(janela)):
    if i < k:
        d.addFront(janela[i])
        if janela[i] > max
        max = janela[i]
        if i == k - 1:
            saida.append(max)
    else:
        d.removeRear()
        
