# 1. Implemente um programa que escreve os divisores dos 100 primeiros valores inteiro.

for num in range(1, 101):
    print(f">> Divisores de {num}:")
    d = 1
    while d <= num:
        if num % d == 0:
            print(f"{num} é divisível por {d}")
        d += 1

# 2. Implemente um programa que escreve os n primeiros números primos.

qtd = int(input("Quantos números primos você deseja ver? "))
while qtd <= 0:
    qtd = int(input(">> Por favor, insira um número positivo: "))
    
num = 2
cont = 0

while cont < qtd:
    divisores = 0
    d = 1

    while d <= num:
        if num % d == 0:
            divisores += 1
        d += 1
    if divisores == 2:
        print(f"{num} é primo")
        cont += 1
    num += 1

# 3. A conjectura de goldbach diz que “todo número par maior ou igual a 4 é a soma de dois primos.” Faça um programa que leia um valor n, inteiro e positivo, e escreva os n primeiros pares acima de 4 juntamente com os primos em que cada par pode ser decomposto.

# Exemplo:
# 4 pode ser decomposto em 2 e 2
# 6 pode ser decomposto em 3 e 3
# 8 pode ser decomposto em 3 e 5
# 10 pode ser decomposto em 5 e 5 (ou 3 e 7 ) 

qtd = int(input("Quantos números pares você deseja ver? "))

while qtd <= 0:
    qtd = int(input(">> Por favor, insira um número positivo: "))

num = 4
pares = 1

while pares <= qtd:
    print(f">> Par {pares}:")
    p1 = num  // 2
    p2 = p1

    while p2 <= p1:
        cont_p1 = 0
        d = 1

        while d <= p1:
            if p1 % d == 0:
                cont_p1 += 1
            d += 1
        if cont_p1 == 2:
            d = 1
            cont_p2 = 0 

            while d <= p2:
                if p2 % d == 0:
                    cont_p2 += 1
                d += 1
            if cont_p2 == 2:
                print(f"{num} pode ser decomposto em {p1} e {p2}")
                pares += 1
                break
        p1 += 1
        p2 -= 1
    num += 2