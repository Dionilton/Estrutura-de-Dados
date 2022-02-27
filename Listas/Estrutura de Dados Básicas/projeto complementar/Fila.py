class Fila:
    
    def __init__(self):
        self.itens = []
    
    def vazia(self):
        return self.itens == []
    
    def enfileirar(self, item):
        self.itens.insert(0, item)
    
    def desenfileirar(self):
        return self.itens.pop()
    
    def tamanho(self):
        return len(self.itens)
    
    