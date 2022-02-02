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
        return self.items[len(self.items) - 1]
    
    def size():
        return len(self.items)
    
s = Stack()

while True:
    n = int(input())
    if n == 0:
        break
    else:
        s.push(n)

retiradas = 0
total_peso = 0

a = int(input())

while True and not s.isEmpty():
    r = int(s.pop())
    retiradas += 1
    total_peso += r
    print(f'Peso retirado: {r}')
    if r == a:
        break
print(f'Anilhas retiradas: {retiradas}')
print(f'Peso total movimentado: {total_peso}')