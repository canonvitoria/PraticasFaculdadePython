#Implemente um programa que leia um valor inteiro entre 1 e 7, correspondente ao dia da semana. O programa deve escrever o dia da semana por extenso correspondente ao valor lido. Por exemplo, se o usuário escrever 1, o programa deve exibir Domingo.

diaSemana = int(input("Informe um número entre 1 e 7: "))

if diaSemana <1 or diaSemana >7:
    print("Valor inválido!! Informe um valor entre 1 e 7.")
else: 
    if diaSemana == 1: print("Domingo")
    if diaSemana == 2: print("Segunda-feira")
    if diaSemana == 3: print("Terça-feira")
    if diaSemana == 4: print("Quarta-feira")
    if diaSemana == 5: print("Quinta-feira")
    if diaSemana == 6: print("Sexta-feira")
    if diaSemana == 7: print("Sábado")

#Elabore um programa que leia 3 notas, calcule e escreva a media ponderada delas considerando os pesos 5, 2.5 e 2.5. A maior nota deve ter peso 5.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))


if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2> 10 or nota3 < 0 or nota3 > 10:
    print("Notas invalidas! Devem estar no intervalo [0;10].")
else: 
    maior = nota1
    if nota2 > maior: maior = nota2
    if nota3 > maior:  maior = nota3
    media = 0.5 * maior + 0.25 * (nota1 + nota2 + nota3 - maior)
    print("Média Ponderada: ", media)

# Implemente um programa que leia os valores a,b e c de uma formula de Bhaskara, calcule e escreva as suas raízes reais.

import math

a = int(input("Informe o valor de A: "))
b = int(input("Informe o valor de B: "))
c = int(input("Informe o valor de C: "))

delta = math.pow(b,2) - 4 * a * c

if delta < 0 or a == 0: 
    print("Valores inválidos! Delta negativo ou divisão por zero.")
else: 
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("X1: ", x1)
    print("X2: ", x2)

# Implemente um programa que leia o saldo médio de uma conta corrente, calcule e escreve o seu limite conforme a tabela abaixo.
# Saldo Médio                  Limite
# menor que R$ 500,00          não há limite
# de R$ 500,00 a R$ 1.000,00   8% do saldo médio
# maior ou igual a R$ 1.000,00 15% do saldo médio

saldoMedio = float(input("Informe o saldo médio de sua conta: "))

if saldoMedio < 500:
    print("Não há limite disponivel.")
else: 
    if saldoMedio > 500 and saldoMedio < 1000:
        print('Limite de: R$', saldoMedio * 0.08)
    if saldoMedio > 1000: 
        print("Limite de: R$", saldoMedio * 0.15)