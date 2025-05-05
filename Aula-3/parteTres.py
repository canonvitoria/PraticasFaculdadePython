#Faça um programa que leia o horário de inicio de um jogo, em horas e minutos, e o horario de fim desse jogo, também em horas e minutos. Sabendo que a duração máxima do jogo é de 24 horas, determine o tempo de duração do jogo em horas e minutos.

tempoMax = 1440

horasIni = int(input("Digite a hora que iniciou a partida: "))
minutosIni = int(input("Digite os minutos que iniciou a partida: "))

inicio = (horasIni * 60) + minutosIni

horasFim = int(input("Digite a hora que terminou a partida: "))
minutosFim = int(input("Digite os minutos que terminou a partida: "))

fim = (horasFim * 60) + minutosFim
diferença = ((inicio - fim) / 60 )

if (inicio > tempoMax) :
    print("Tempo excedido!")
else :
    print ('O tempo de jogo foi de: ', diferença)

#Resolução - faltou fazer -> começa em um dia e termina no outro

if inicio < fim: 
    duracao = fim - inicio
    print('O tempo de jogo foi de: ', duracao)
else:
    duracao = 24 * 60 - inicio + fim

print('Horas: ', duracao//60)
print('Minutos: ', duracao%60)

#Elabore um programa que leia um número inteiro de 4 digitos (garanta isso). A seguir o programa deve determinar se o número lido é capicua. Um número é capicua quando lido da esquerda para a direita ou da direita para a esquerda representa sempre o mesmo valor, como por exemplo 6446.

num = int(input('Informe um valor inteiro de 4 digitos: '))

if  num < 1111 or num > 9999:
    print('Valor invalido')
else:
    milhar = num // 1000
    resto = num % 1000
    centena = resto // 100
    resto = resto % 100
    dezena = resto // 10 
    unidade = resto % 10 
    invertido = unidade * 1000 + dezena * 100 + centena * 10 + milhar
    print('Número invertido: ', invertido)
    if num == invertido:
        print("Capicua!")
    else:
        print("Não é Capicua!!")