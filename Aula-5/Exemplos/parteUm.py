# Exemplos - 4: Adaptando o algoritmo para que seja possível utilizar a repetição por contagem: 
# 1. Comece por um "chute", n
# 2. Repita uma certa quantidade de vezes: 
#   1. O próximo "chute" será a media entre n e x/n
# 3. Exiba o "chute" final

num = int (input("Digite um número: "))
total = int(input("Digite a quantidade de tentativas: "))
aprox = 1 

for cont in range (1, total + 1):
    aprox = (aprox + num / aprox) / 2
    print(f"Tentativa {cont:3}: {aprox:5}")

print(f"A raiz quadrada de {num} é aproximadamente {aprox:.2f}")