import random

class Fighter:
    
    def __init__(self, id):
        self.id = id
        self.defesa = 100
        self.ataque = int(random.uniform(0, 100))
        self.precisao = round(random.uniform(0, 1), 2)
        self.jedi = bool(round(random.uniform(0, 1), 2) <= 1.25e-10)
        
    def get_id(self):
        return self.id
    
    def get_defesa(self):
        return self.defesa
    
    def get_ataque(self):
        return self.ataque
    
    def get_precisao(self):
        return self.precisao
    
    def get_jedi(self):
        return self.jedi
    
    def __str__(self):
        return f'fighter_id: {self.id}, d: {self.defesa}, a: {self.ataque}, p: {self.precisao}, j: {self.jedi}'
    
    def disparar(self):
        
        if random.uniform(0, 1) <= self.precisao:
            return self.ataque
        
        return 0
    
    def sobreviveu_danos(self, disparos):
        
        for i in disparos:
            self.defesa -= i
            
        return self.defesa > 0
        
