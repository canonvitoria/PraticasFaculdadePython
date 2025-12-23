# Defina uma lista com a idade de 20 pessoas. 
# Seu programa deve calcular e escrever: 
# • média de idade
# • maior idade
# •menor idade

import random

lista = []

for i in range(1,21):
    lista.append(random.randint(1,100))
print("Lista de idades:", lista)

media = sum(lista) / len(lista) 
print("Média das idades:", media)

print("A maior idade é:", max(lista))
print("A menor idade é:", min(lista))
