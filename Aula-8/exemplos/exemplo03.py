# Uma empresa de estatística analisou os 5 melhores jogadores deuma liga profissional de basquete e registrou os pontos,assistências e rebotes de cada um. 
# Para isso, crie uma lista de tuplas, onde cada tupla é da forma (nome do jogador, pontos,assistência, rebotes). 
# Ao final, o programa deve percorrer a lista e informar a tupla do jogador que tem as melhores estatísticas
# ((pontos+assistências+rebotes)/3).

jogares = []
estatisticas = []
cont = 1

while cont <= 3:
    print('Jogador: ', cont)
    nome = input ('Informe o nome do jogador: ')
    pontos = float(input('Informe os pontos: '))
    assistencias = int(input('Informe as assistências: '))
    rebotes = int(input('Informe os rebotes: '))
    jogares.append((nome, pontos, assistencias, rebotes))
    cont += 1
print(jogares)

for dados in jogadores:
    soma=0
    for i in range(1,4):
        soma += dados[i]
    media = soma / 3
    estatisticas.append((dados[0], media))
print(estatisticas)

melhor = estatisticas[0]
for jogador in estatisticas:
    if jogador[1] > melhor[1]:
        melhor = jogador
print('O melhor jogador é: ', melhor[0], ' com média de: ', melhor[1])