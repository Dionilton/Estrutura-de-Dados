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

par_stack = Stack()
ope_stack = Stack()

ind = 0
for i in x:
    if i == "(":
        par_stack.push(i)
    if i in ope:
        ope_stack.push(i)
    if i == ")":
        ope_stack.pop()
        par_stack.pop()
        x[ind] = ope_stack.pop()
    ind += 1

print(x)