# Crie uma lista com 30 valores inteiros. Gere a lista com valores aleatorios entre 1 e 500. A seguir, implemente um programa que varre a lista, calcula e exibe:
    # a) O maior valor da lista
    # b) A quantidade de pares

import random

lista=[]

for i in range(1,30): # Loop para repetir 30 vezes (para cada iterador de 1 a 30)
    lista.append(random.randint(1,500)) # Adiciona valores aleatorios entre 1 e 500 na lista
print("Lista de valores:", lista)

maior = lista[0] # Inicializa a variável maior com o primeiro valor da lista
pares = 0 
for num in lista: # Loop para percorrer cada número na lista
    if num > maior:
        maior = num
    if num % 2 == 0:
        pares += 1 

print("O maior valor da lista é:", maior)
print("A quantidade de números pares na lista é:", pares) 