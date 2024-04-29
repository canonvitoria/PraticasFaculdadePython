# Aula prática

# Exercício - 1
# Faça um programa que converte de Fahrenheit para graus Celsius. O programa deve ler uum valor em Fahrenheit, converter e escrever o valor correspondete em Celsius. Para realizar a conversão use a fórmula c = 5/9(f-32)

fahrenheit = float(input('Insira a temperatura em Fahrenheit: '))
celsius = 5/9 * (fahrenheit - 32) #celsius = 5/9 (fahrenheit - 32)
print('A temperatura em graus Celsius é de: ', celsius, '°')