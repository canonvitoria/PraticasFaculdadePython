# Elabore um programa que gera uma lista com 30 valores inteiros, cria e escreve uma outra lista com os 10 maiores.

import random

valores = []

for i in range(30):
    valores.append(random.randint(1, 100))
print("Lista de valores:", valores)

maiores_valores = sorted(valores, reverse=True)[:10] #sorted retorna uma nova lista ordenada, reverse=True ordena do maior para o menor, e [:10] pega os 10 primeiros elementos dessa lista ordenada
print("Os 10 maiores valores são:", maiores_valores)