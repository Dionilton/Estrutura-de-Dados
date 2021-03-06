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
        

#Videos/estudos: Travessias

"""
***Videos***
Pré-Ordem: https://youtu.be/ahQ2KpC3ba4
Em-Ordem: https://youtu.be/Yy0oyWx55yw
Pós-Ordem: https://youtu.be/ELguSB4T2JY
Alg. Remoção de Nós: https://youtu.be/M2Hb3O9KJBM
Balanceamento/Desbalanceamento, Algoritmos de Rotação de Árvore AVL: https://youtu.be/W16tC-xMx-M
Algoritmo DSW: https://youtu.be/k3yt7VUn0eY
***Videos***
Arvore parentes: https://dcm.ffclrp.usp.br/~augusto/teaching/aedi/AED-I-Arvores.pdf
(A(B(D()(G()()))())(C(E(H()())(I()()))(F()(J)))) -> Representar em grafo
in-ordenm: D G B A H E I C F J  ???
"""
