class Deque():
    def __init__(self):
        self.items = []
    def addRear(self, item):
        self.items.insert(0, item)
    def addFront(self, item):
        self.items.append(item)
    def removeRear(self):
        return self.items.pop(0)
    def removeFront(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    
n, p = map(int, input().split())
dados = input().split()
d = Deque()

for i in range(len(dados)):
    dados[i] = int(dados[i])

soma = 0
for i in range(len(dados)):
    if i < p:
        d.addFront(dados[i])
        soma += dados[i]
        if i == p-1:
            print(int(soma/p))
    else:
        soma -= d.removeRear()
        soma += dados[i]
        d.addFront(dados[i])
        print(int(soma/p))
