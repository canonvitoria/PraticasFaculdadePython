import math

# Aula prática

# Exercício - 1
# Faça um programa que converte de Fahrenheit para graus Celsius. O programa deve ler uum valor em Fahrenheit, converter e escrever o valor correspondete em Celsius. Para realizar a conversão use a fórmula c = 5/9(f-32)

fahrenheit = float(input('Insira a temperatura em Fahrenheit: '))
celsius = 5/9 * (fahrenheit - 32) #celsius = 5/9 (fahrenheit - 32)
print('A temperatura em graus Celsius é de: ', celsius, '°')

#Exercício - 2
#Construa um problema que leia dois valores inteiros e escreva na tela:
# a) a soma
# b) a diferença
# c) a média
# d) a distância (valor absoluto da diferença)
# e) o maior dos dois (use maior = a+b+|a-b|/2).
# f) o menor dos dois (use menor = a+b-b|a-b|/
 
valor1 = int(input('Informe o primeiro valor: '))
valor2 = int(input('Informe  o segundo valor: '))
soma = valor1 + valor2
diferença = valor1 - valor2
média = (valor1 + valor2)/2
distância = math.fabs(diferença) 
maior = (valor1 + valor2 + math.fabs(valor1 - valor2))/2 #Erro: maior = valor1 + valor2 + math.fabs(valor1 - valor2)/2 
menor = (valor1 + valor2 - math.fabs(valor1 -  valor2))/2 #Erro: menor = valor1 + valor2 - valor2 * math.fabs(valor1 -  valor2)/2

print('A soma dos números informados é de:', soma)
print('A diferença dos núemros informados é de:', diferença)
print('A média dos números informados é de:', média)
print('A distância entre os números informados é de:', distância)
print('O maior dos dois é de:', maior)
print('O menor dos dois é de:', menor)

# Exercício - 3
# Construa um programa que lê o tempo de um evento em segundos e o escreve decomposto em horas, minutos e segundos.

tempo = int(input('Informe o tempo d0 evento em segundos: '))
horas = tempo//3600 # entrada de segundos (trabalhar nessa unidade)
resto = tempo%3600
minutos = resto//60 
segundos = resto%60

print('Horas:', horas)
print('Minutos:', minutos)
print('Segundos:', segundos)

