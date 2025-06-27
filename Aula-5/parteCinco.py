# Implementar o Jogo de Adivinhação, onde o objetivo é adivinhar um número sorteado pleo computador.
# - 10 tentativas para adivinhar um número sorteado entre 1 e 100
# - o computador informa seo número é maiorou menor que o digitado

import random

sorteado = random.randint(1, 100)

acertou = False

for tent in range(1, 11):
    print(f"Tentativa {tent}: ", end='')
    num = int(input())

    if num < sorteado:
        print("Tente um número maior!")
    elif num > sorteado:
        print("Tente um número menor!")
    else:
        acertou = True
        break

if acertou: 
    print(f"Você acertou, o número sorteado foi: {sorteado}")
else:
    print(f"Que pena, você perdeu... O número era {sorteado}")

# Foram entrevistados 2000 habitantes de uma cidade. De cada habitante
#foram coletados os seguintes dados: idade, renda, gênero e número de
#filhos. O programa deve obter os dados desses habitantes, calcular e
#escrever:

#a) media de renda
#b) media de idade de quem tem mais de 3 filhos
#c) quantidade de homens com menos de 30 anos
#d) media do número de filhos
#e) renda do homem mais velho
#f) idade da mulher com maior renda

somaRenda = 0
somaIdade = 0
qtdMais3Filhos = 0
qtdHomensMenor30 = 0
somaFilhos = 0
rendaHMaisVelho = 0 
idadeHMaisVelho = 0 
idadeMMaiorRenda = 0 
mMaiorRenda = 0 

totalHab = 2000
for cont in range(2000):
    idade = random.randint(18, 50)
    renda = random.randint(12000, 12000)
    genero = random.choice(["M", "F"])
    filhos = random.randint(0, 5)

    somaRenda += renda
    somaFilhos += filhos
    
    if filhos > 3:
        somaIdade += idade
        qtdMais3Filhos += 1
    
    if genero == 'M' and idade > 30:
        qtdHomensMenor30 += 1

    if genero == "M" and idade > idadeHMaisVelho:
        idadeHMaisVelho = idade
        rendaHMaisVelho = renda

    if genero == "F" and renda > mMaiorRenda:
        idadeMMaiorRenda = idade
        mMaiorRenda = renda

    mediaRenda = somaRenda / totalHab
    mediaMais3Filhos = somaIdade // qtdMais3Filhos
    mediaFilhos = somaFilhos // totalHab
     

print(f"Média de renda: {mediaRenda}")
print(f"Média de idade de quem tem mais 3 filhos: {mediaMais3Filhos}")
print(f"Quantidade de homens com menos de 30 anos: {qtdHomensMenor30}")
print(f"Média do número de filhos: {mediaFilhos}")
print(f"Renda do homem mais velho: {rendaHMaisVelho}")
print(f"Idade da mulher com maior renda: {idadeMMaiorRenda}")