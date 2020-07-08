'''
@author:    Victor Pedroso Curtarelli
@linkedin:  linkedin.com/in/victorcurtarelli/
@github:    github.com/curtarelli
@created:   July, 2020.
'''
def interseccao(x1, y1, x2, y2, x3, y3, x4, y4):            # Função para teste se 2 retas se interceptam;
    s123 = (y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)
    s124 = (y2 - y1) * (x4 - x1) - (x2 - x1) * (y4 - y1)

    if (s123 == 0.0) and (s124 == 0.0):

        if x1 == x2:
            result = (min(y1, y2) <= max(y3, y4)) and (min(y3, y4) <= max(y1, y2))
        else:
            result = (min(x1, x2) <= max(x3, x4)) and (min(x3, x4) <= max(x1, x2))

    else:

        s341 = (y4 - y3) * (x1 - x3) - (x4 - x3) * (y1 - y3)
        s342 = (y4 - y3) * (x2 - x3) - (x4 - x3) * (y2 - y3)

        result = ((s123 * s124) <= 0.0) and ((s341 * s342) <= 0.0)

    if result:
        print('Os segmentos R1 e R2 se interceptam!''\n')
    else:
        print('Os segmentos R1 e R2 não se interceptam!''\n')

# Coordenadas dos pontos das retas para exemplo;
x1 = 0
y1 = 0

x2 = 2
y2 = 21

x3 = 1
y3 = 0

x4 = 21
y4 = 2

# Retorna as coordenadas de exemplo para as retas R1 e R2;
print('Exemplo para retas:')
print('R1: [(', x1, ';', y1, ') , (', x2, ';', y2,')]')
print('R2: [(', x3, ';', y3, ') , (', x4, ';', y4,')]')

# Aplica a função para as retas deexemplo;
print(interseccao(x1, y1, x2, y2, x3, y3, x4, y4))

#Pergunta ao usuário as coordendas escolhidas para R1 e R2;
x1 = float(input("R1 x1: "))
y1 = float(input("R1 y1: "))

x2 = float(input("R1 x2: "))
y2 = float(input("R1 y2: "))

x3 = float(input("R2 x1: "))
y3 = float(input("R2 y1: "))

x4 = float(input("R2 x2: "))
y4 = float(input("R2 y2: "))

# Retorna valores escolhidos de forma organizada;
print('Retas:')
print('R1: [(', x1, ';', y1, ') , (', x2, ';', y2,')]')
print('R2: [(', x3, ';', y3, ') , (', x4, ';', y4,')]')

# Aplica função intersecção para os valores escolhidos e retorna o resultado;
print(interseccao(x1, y1, x2, y2, x3, y3, x4, y4))