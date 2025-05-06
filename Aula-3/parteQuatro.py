#Implemente um programa que determina o preço de venda dos produtos de uma loja conforme o preço de custo desses produtos. O programa deve ler o preço de custo e calcular o valor de venda conforme a tabela abaixo. 

# preço unitário de custo preço de venda
# valor abaixo de R$ 10,00 lucro de 70%
# de R$ 10,00 a menos de R$ 30,00 lucro de 50%
# de R$ 30,00 a menos de R$ 50,00 lucro de 40%
# valor acima ou igual a R$ 50,00 lucro de 30%

preco = float(input("Informe o preço de custo do produto: "))

if preco < 10: 
    lucro = (preco * 70) / 100
    venda = lucro + preco 
    print("O lucro sobre o produto é de: ", lucro)
    print("Então a venda será de: R$ ", venda)


if preco >= 10 or preco < 30: 
    lucro = (preco * 50) / 100
    venda = lucro + preco 
    print("O lucro sobre o produto é de: ", lucro)
    print("Então a venda será de: R$ ", venda)



if preco >= 30 or preco < 50: 
    lucro = (preco * 40) / 100
    venda = lucro + preco 
    print("O lucro sobre o produto é de: ", lucro)
    print("Então a venda será de: R$ ", venda)


if preco >= 50: 
    lucro = (preco * 30) / 100
    venda = lucro + preco 
    print("O lucro sobre o produto é de: ", lucro)
    print("Então a venda será de: R$ ", venda)

