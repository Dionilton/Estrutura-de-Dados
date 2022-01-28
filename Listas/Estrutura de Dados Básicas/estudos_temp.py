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
    
x = input()
x = list(x)
ope = "+-*/"
let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"
saida = ""
par_stack = Stack()
ope_stack = Stack()

ind = 0
for i in x:
    if i in let:
        saida += i
    elif i == "(":
        par_stack.push(i)
    elif i in ope:
        ope_stack.push(i)
    elif i == ")":
        par_stack.pop()
        saida += ope_stack.pop()
        
print(saida)
        
