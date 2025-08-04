# 1. Chico tem 1,50 metro e cresce 2 centímetros por ano,enquanto Zé tem 1,10 metro e cresce 3 centímetros por ano.Construa um programa que calcule e exiba quantos anos serão necessários para que Zé seja maior que Chico. 

chico_altura = 150
ze_altura = 110
anos = 0

while ze_altura <= chico_altura:
    chico_altura += 2
    ze_altura += 3
    anos += 1   

print(f"Serão necessários {anos} anos para que Zé seja maior que Chico.")

# 2. Implemente um programa que leia a idade, altura e gênero de 10 estudantes. O programa deve calcular e escrever:

# a) Media de idade dos estudantes
# b) Media de altura das meninas
# c) Percentual de estudantes com mais de 20 anos.
# d) Altura do estudante mais velho

# Valide/Critique os dados de entrada

cont = 0
soma = 0
meninas = 0
altura_meninas = 0
maior_20 = 0
maior_idade = 0
maior_altura = 0

while True: 
    idade = int(input("Digite a idade do estudante (ou -1 para sair): "))

    if idade == -1:
        print("Saindo do programa...")
        break

    while idade <= 0 or idade > 120:
        print("> Idade inválida. Deve ser um número entre 1 e 120.")
        idade = int(input("Digite a idade do estudante: "))

    altura = float(input("Digite a altura do estudante: "))

    while altura <= 0 or altura > 3.0:
        print("> Altura inválida. Deve ser um número positivo e menor que 3 metros.")
        altura = float(input("Digite a altura do estudante: "))

    genero = int(input("Digite o gênero do estudante(1-F 2-M): "))

    while genero!=1 and genero!=2:
        print("> Gênero inválido. Digite 1 para feminino ou 2 para masculino.")
        genero = int(input("Digite o gênero do estudante(1-F 2-M): "))

    # Processamento dos dados

    soma += idade
    cont += 1

    if genero == 1:
        meninas += 1
        altura_meninas += altura   

    if idade > 20:
        maior_20 = (cont / 10) * 100 

    if idade > maior_idade:
        maior_idade = idade
        maior_altura = altura


if cont == 0:
    print("Nenhum estudante foi cadastrado.")
else:
    print(f"Média de idade dos estudantes: {soma / cont:.2f}")

    if meninas == 0:
        print("Não há meninas na turma.")
    else:
        print(f"Média de altura das meninas: {altura_meninas / meninas:.2f}")

    print(f"Percentual de estudantes com mais de 20 anos: {maior_20:.2f}%")
    print(f"Altura do estudante mais velho: {maior_altura:.2f} metros")