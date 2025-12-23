# Defina uma lista com as notas de 15 alunos. O programa deve contar e escrever quantos alunos estão:
# • acima da média.
# • na média.
# • abaixo da média.
# Escrever também a maior e menor nota.

import random

lista = []

for i in range(1,15):
    lista.append(random.randint(1,100)/10) # Adiciona valores aleatorios entre 0.1 e 10.0 na lista
print("Lista de notas:", lista)

media = sum(lista) / len(lista)  #soma e depois divide pelo tamanho da lista
print("Média das notas:", round(media,2))

acima_media = 0
abaixo_media = 0

for nota in lista:
    if nota > media:
        acima_media += 1
    elif nota < media:
        abaixo_media += 1   

print("Quantidade de alunos acima da média:", acima_media)
print("Quantidade de alunos abaixo da média:", abaixo_media)
print("Quantidade de alunos na média:", lista.count(media))
print("A maior nota é:", max(lista))
print("A menor nota é:", min(lista))
