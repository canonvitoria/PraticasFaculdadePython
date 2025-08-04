# 1. Implemente um programa que calcula a soma do n primeiros termos da serie a seguir:
# 1 + 1/2 + 1/3 + 1/4 + 1/5 + ...

nTermos = int(input("Informe a quantodade de termos: "))

if nTermos <= 0:
    print("A quantidade de termos deve ser maior que zero.")
else:
    soma = 0
    cont = 1
    while cont <= nTermos:
        soma = soma + 1 / cont
        cont += 1
    print("A soma dos", nTermos, "termos é:", soma)

# 2. Implemente um programa que calcula a soma do n primeiros termos da serie a seguir:
# 2 + 4/3 + 6/5 + 8/7 + 10/9 + ....

nTermos = int(input("Informe a quantodade de termos: "))

if nTermos <= 0:
    print("A quantidade de termos deve ser maior que zero.")
else:
    soma = 0
    cont = 1
    numerador = 2
    denomidador = 1
    while cont <= nTermos:
        soma =+ soma + numerador / denomidador
        cont += 1
        numerador += 2
        denomidador += 2
    print("A soma dos", nTermos, "termos é:", soma)

# 3. Implemente um programa que leia dois valores a e b. O programa deve escrever e somar os valores impares existentes entre a e b.
# Exemplo: a = 10 e b = 16
# 11, 13, 15
# Soma = 39

a = int(input("Informe o valor de a: "))
b = int(input("Informe o valor de b: "))

if a < 0 and b < 0:
    print("Os valores devem ser maiores ou iguais a zero.")
elif a == b:
    print("Os valores devem ser diferentes.")
else:
    a > b
    aux = a
    a = b
    b = aux

    if a % 2 == 0:
        a += 1
        soma = 0
    print("Os valores impares entre", a, "e", b, "são:")
    while a <= b:
        print(a, end=", ")
        soma += a
        a += 2
    print("A soma dos impares do intervalo é:", soma)

# 4. Implemente um programa que leia um valor e verifique se é perfeito. Para ser perfeito, ele deve corresponde ‘a soma dos seus divisores próprios.
# Exemplo: 6, pois 1 +2 + 3 e’ 6.

num = int(input("Informe um número: "))

while num <= 0:
    print("O número deve ser maior que zero.")
    num = int(input("Informe um número: "))

soma = 0
d = 1

while d < num/2:
    if num / d == 0:
        soma += d
    d += 1
if soma == num:
    print(num, "é um número perfeito.")
else:
    print(num, "não é um número perfeito.")