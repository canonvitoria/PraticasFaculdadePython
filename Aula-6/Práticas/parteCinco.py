# Exercício 1 – Construa um programa que escreve o fatorial dos 100 primeiros inteiro.

inteiro = 1
fatorial = 1

while inteiro <= 100:
    fatorial *= inteiro
    print(f"O fatorial de {inteiro} é: {fatorial}")
    inteiro += 1

# Exercício 2 – Escreva um programa que leia uma quantidade desconhecida de números. A seguir, o programa deve contar e escrever a quantidade de valores pertencentes aos seguintes intervalos: [0;25], [26;50], [51;75] e [76;100]. A entrada de dados deve terminar quando for lido um número negativo. Ao final o programa deve exibir ainda a quantidade de valores lidos.

cont_0_25 = 0
cont_26_50 = 0
cont_51_75 = 0
cont_76_100 = 0

while True:
    num = int(input("Digite um número inteiro (-1 para sair): "))

    if num < 0:
        print("Número negativo, encerrando o programa.")
        break
    elif num >= 0 and num <=25:
        cont_0_25 += 1
    elif num >= 26 and num <=50:
        cont_26_50 += 1
    elif num >= 51 and num <=75:
        cont_51_75 += 1
    elif num >= 76 and num <=100:
        cont_76_100 += 1
    else:
        print("Número fora do intervalo considerado.")

print(f"Quantidade de valores no intervalo [0;25]: {cont_0_25}")
print(f"Quantidade de valores no intervalo [26;50]: {cont_26_50}")
print(f"Quantidade de valores no intervalo [51;75]: {cont_51_75}")
print(f"Quantidade de valores no intervalo [76;100]: {cont_76_100}")
print(f"Quantidade total de valores lidos: {cont_0_25 + cont_26_50 + cont_51_75 + cont_76_100}")

# Exercício 3 – Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo (1-masculino/2-feminino) e salário. Faça um programa que leia os dados necessário e informe:

#(a) a média de salário do grupo;
#(b) maior e menor idade do grupo;
#(c) quantidade de mulheres com salário até R$3500,00.

#Encerre a entrada de dados quando for digitada uma idade negativa

cont = 0
soma = 0
soma_salario = 0

while True: 
    idade = int(input("Digite a idade (ou -1 para sair): "))

    if idade == -1:
        print("Saindo do programa...")
        break

    while idade <= 0 or idade > 120:
        print("> Idade inválida. Deve ser um número entre 1 e 120.")
        idade = int(input("Digite a idade: "))

    genero = int(input("Digite o gênero(1-F 2-M): "))

    while genero!=1 and genero!=2:
        print("> Gênero inválido. Digite 1 para feminino ou 2 para masculino.")
        genero = int(input("Digite o gênero(1-F 2-M): "))

    salario = float(input("Digite o salário: "))

    # Processamento dos dados

    soma += idade
    cont += 1 
    soma_salario += salario
    if cont == 1:
        maior_idade = menor_idade = idade
    else:
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade

    if genero == 2 and salario <= 3500:
        cont_mulheres_salario_baixo = 1

print(f"Média de idade do grupo: {soma / cont:.2f}")
print(f"Maior idade do grupo: {maior_idade}")  
print(f"Menor idade do grupo: {menor_idade}")
print(f"Quantidade de mulheres com salário até R$3500,00: {cont_mulheres_salario_baixo}") 

