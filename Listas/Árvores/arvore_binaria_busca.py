def arvoreBusca(lista):
    arvore = Node(lista[0])
    current = arvore
    for i in range(1, len(lista)):
        while current.getRigth() != None or current.getLeft() != None:
            if lista[i] > current.getData():
                current = current.getRigth()
            else:
                
            
    
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.rigth = None
        self.left = None
        
    def getData(self):
        return self.data
    def getRigth(self):
        return self.next_rigth
    def getLeft(self):
        return self.next_left
    
    def setData(self, newdata):
        self.data = newdata
    def setRigth(self, newrigth):
        self.rigth = newrigth
    def setLeft(self, newleft):
        self.left = newleft