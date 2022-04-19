class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        
    def addNeighbor(self, nbr, weigth = 0):
        self.connectedTo[nbr] = wigth
        
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    
    def getConnections(self):
        return self.connectionTo.keys()
    
    def getId(self):
        return self.id
    
    def getWeigth(self, nbr):
        return self.connectedTo[nbr]