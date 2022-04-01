def arvoreBusca(lista):
    arvore = Node(lista[0])
    current = arvore
    for i in range(1, len(lista)):
        temp = Node(lista[i])
        while current.getRigth() != None or current.getLeft() != None:
            if lista[i] > current.getData():
                current = current.getRigth()
            else:
                current = current.getLeft()
        if lista[i] > current.getData():
            current.setRigth(temp)
        elif lista[i] < current.GetData():
            current.setLeft(temp)
    
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
        
        
# 3 Stps
"""
metod.: < ^ >

//most imp
1 - 1 ^ 3 (2m)
2 - 3 ^ 7 (2m)
3 - 7.7 ... (quit all end m) / 3m -> 90% all dbt (3m)
//most imp

plus stps - (nov & dec: 8 ^ 25)
end dec: QUIT ALL

2k23: nw ag

1 - checkpoint ^ 25 (1m)
2 - 25.+4 (2m)

end 1° tri 2k23 +50 in M.Ac. (1. MGL)(2.CH)

HW: fz plani do plan
    fz plani de priridade
    Sistematizar plan, polir e exe.

"""

#Videos/estudos: Travessias

"""

Pré-Ordem: https://youtu.be/ahQ2KpC3ba4
Em-Ordem: https://youtu.be/Yy0oyWx55yw
Pós-Ordem: https://youtu.be/ELguSB4T2JY
Arvore parentes: https://dcm.ffclrp.usp.br/~augusto/teaching/aedi/AED-I-Arvores.pdf
(A(B(D()(G()()))())(C(E(H()())(I()()))(F()(J)))) -> Representar em grafo
in-ordenm: D G B A H E I C F J  ???

"""
