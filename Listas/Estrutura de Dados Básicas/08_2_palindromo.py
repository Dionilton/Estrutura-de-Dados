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
    

def isPalindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False

palavras = input().split()

for i in palavras:
    if not isPalindromo(i):
        p_01 = False
        p_02 = False
        n = 3
        l = []
        while len(i) - n > 0:
            d = Deque()
            for j in range(n):
                d.addFront(i[j])
                l.append(i[j])
            if isPalindromo(l):
                p_01 = True
            ind = n
            for j in range(len(i) - n):
                d.removeRear()
                d.addFront(i[ind])
                l = []
                for k in range(d.size()):
                    l.append(d.items[k])
                if isPalindromo(l) and p_01 == True:
                    p_02 = True
                    break
                elif isPalindromo(l) and not p_01:
                    p_01 = True
                ind += 1
            n += 1
            if p_01 and p_02:
                print(i)
                break
        else:
            continue