# Construa um programa que gera uma lista com as avaliações de 25 pessoas. 
# Cada pessoa avaliou a gestão do prefeito de uma cidade com notas de 5 a 1, onde 5 corresponde a Excelente, 4 a Bom, 3 a Regular, 2 a Ruim e 1 a Péssimo. 
# Seu programa deve calcular e escrever:
# • A quantidade de votos em cada conceito.

import random

lista = []

for i in range(1,26):
    lista.append(random.randint(1,5))
print("Lista de avaliações:", lista)

excelente = lista.count(5)
bom = lista.count(4)
regular = lista.count(3)
ruim = lista.count(2)
pessimo = lista.count(1)
print("Quantidade de votos Excelente (5):", excelente)
print("Quantidade de votos Bom (4):", bom)
print("Quantidade de votos Regular (3):", regular)
print("Quantidade de votos Ruim (2):", ruim)
print("Quantidade de votos Péssimo (1):", pessimo)