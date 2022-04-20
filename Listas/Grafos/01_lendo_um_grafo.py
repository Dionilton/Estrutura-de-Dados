class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self, nbr, weigth=0):
        self.connectedTo[nbr] = weight
        
    def removeNeighbor(self, nbr):
        if nbr in self.connectedTo:
            del self.connectedTo[nbr]
        
    def __str__(self):
        return str(self.id) + ' connectedTo ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeigth(self, nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __inti__(self):
        self.vertexList = {}
        self.numVertex = 0
        
    def addVertex(self, key):
        self.numVertex += 1
        nv = Vertex(key)
        self.vertexList[key] = nv
        return nv
    
    def getVertex(self, key):
        if key in self.vertexList:
            return self.vertexList[key]
        else:
            return None
        
    def __contains__(self, n):
        return n in self.vertixList
    
    def addEdge(self, f, t, w):
        if __contains__(f) and __contains__(t):
            self.vertexList[f].addNeigthbor(self.vertexList[t], w)
            
    def removeVertex(self, key):
        del self.vertexList[key]
        
    def removeEdge(self, f, t):
        self.vertexList[f].removeNeigthbor(t)
    
        