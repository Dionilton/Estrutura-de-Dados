import datetime
string = input().split()
di, tempo_i = int(string[0]), string[1]

string = input().split()
df, tempo_f = int(string[0]), string[1]


hi, mi, si = map(int, tempo_i.split(':'))
hf, mf, sf = map(int, tempo_f.split(':'))

t_hora = 0
t_dia = 0
t_minuto = 0
t_segundo = 0

data_i = datetime.timedelta(di,si,0,0,mi,hi,0)
data_f = datetime.timedelta(df,sf,0,0,mf,hf,0)
duracao = data_f - data_i

if duracao.days < 0 or duracao.days == 0 and duracao.seconds == 0:
    print("Data inválida!")
    
else:
    if duracao.days == 0:
        tempo = str(duracao)
        tempo = tempo.split(':')
        print(f'{duracao.days} dia(s)\n{int(tempo[0])} hora(s)\n{int(tempo[1])} minuto(s)\n{int(tempo[2])} segundo(s)')
        
    else:
        tempo = str(duracao)
        tempo = tempo.split()
        tempo = tempo[2]
        tempo = tempo.split(':')
        print(f'{duracao.days} dia(s)\n{int(tempo[0])} hora(s)\n{int(tempo[1])} minuto(s)\n{int(tempo[2])} segundo(s)')