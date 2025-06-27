# Exemplo 3 - Somatório de 1 a num

soma = 0
num = int(input("Número: "))
for cont in range(1, num+1):
    soma = soma + cont 
print(f"Somatório: {soma}")

# Exemplo 4 - Algoritmo de Heron para calcular aproximação de raiz quadrada

num = int(input("Valor desejado: "))
total = int(input("Qtd. de repetições: "))

aprox = 1 
for cont in range (1, total + 1):
    aprox = (aprox + num/aprox) / 2 
    print(f"{cont:3} {aprox:.5f}")
print(f"Raiz aproximada: {aprox: .5f}")

