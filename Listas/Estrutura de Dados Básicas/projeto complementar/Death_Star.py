import random

class Death_Star:
    
    def __init__(self):
        self.defesa = 1000
        self.ataque = int(random.uniform(0, 100))
        self.precisao = round(random.uniform(0, 1), 2)
        self.canhoes = int(random.uniform(1, 6))
        
    def get_defesa(self):
        return self.defesa
    
    def get_ataque(self):
        return self.ataque
    
    def get_precisao(self):
        return self.precisao
    
    def __str__(self):
        return f'death_star d: {self.defesa}, a: {self.ataque}, p: {self.precisao}, c: {self.canhoes}'
    
    def disparar(self):
        r = []
        
        for i in range(self.canhoes):
            if random.uninform(0,1) <= self.precisao:
                r.append(seld.ataque)
            else:
                r.append(0)
        
        return r
    
    def sobreviveu_danos(self, disparos):
        self.defesa -= disparo
        
        return self.defesa > 0