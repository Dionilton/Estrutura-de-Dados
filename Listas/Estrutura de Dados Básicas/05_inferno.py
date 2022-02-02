class Deque:
    def __init__(self):
        self.items = []
    def isEmpty():
        return self.items == []
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.item.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)

nomes = input().split()
n = int(input())
d = Deque()

for i in nomes:
    d.addFront(i)
    
for i in range(n):
    temp = d.removeRear()
    d.addFront(temp)
    
print(f'Pessoa da frente: {d.items[0]}')
print(f'Pessoa do fim: {d.items[d.size() - 1]}')