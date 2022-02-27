import random
from Fila import Fila
from Fighter import Fighter
from Death_Star import Death_Star

class Simulacao_Batalha:
    
    def __init__(self, turnos, confianca):
        self.f_fighters = Fila()
        self.turnos = turnos
        self.confianca = confianca
        self.id_geral = 0
        self.death_star = Death_Star()
        
    def novo_fighter(self):
        numero = round(random.uniform(0, 1), 2)
        return numero <= self.confianca
    
    def get_novo_id(self):
        self.id_geral += 1
        return self.id_geral
    
    def executar_simulacao(self):
        
        for t in range(self.turnos):
            
            print('---------------------------------')
            print(f'Turno {t}')
            print('---------------------------------')
            
            if self.novo_fighter():
                fighter = Fighter(self.get_novo_id())
                
                self.f_fighters.enfileirar(fighter)
                print(f'- fighter_id: {fighter.get_id()} entrou em formação.')
                
            print(f'- {self.f_fighters.tamanho()} fighters para atacar.')
            
            if self.f_fighters.tamanho() == 0:
                continue
            
            fighter = self.f_fighters.desenfileirar()
            print(f'- <LIDER> {fighter}')
            
            if fighter.get_jedi():
                print('<<<<<<< TEMOS UM JEDI >>>>>>>')
                
            #turno Death Star
            print('\nTurno - Death Star')
            print(f'- {self.death_star}')
            
            disparos = self.death_star.disparar()
            print(f'- disparos: {disparos}')
            
            if fighter.sobreviveu_danos(disparos):
                print(f'- {fighter} sobreviveu!')
            else:
                print(f'- MAN DOWN! - fighter_id: {fighter.get_id()}')
                continue
            
            #turno fighter
            print('\nTurno - Fighter')
            disparo = fighter.disparar()
            print(f'- disparo: {disparo}')
            
            if fighter.get_jedi():
                print('- Bonus JEDI +10.000')
                disparo += 10000
            
            if self.death_star.sobreviveu_danos(disparo):
                print(f'- {self.death_star} sobreviveu!')
            else:
                print('\n\n DEATH STAR DESTROYES!! ')
                print(f'{self.death_star}')
                exit()
                    
                    
            self.f_fighters.enfileirar(fighter)
                
            