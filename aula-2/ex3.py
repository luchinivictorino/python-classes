# 3) Crie uma lista de produtos com os seguintes requisitos:
# – Inicializará com 10 produtos, preços e quantidades;
# – Faça um Foreach para calcular o valor total de cada produto;
# – Ao final, mostre todos os produtos, preços, quantidade, total por produto e o total geral.

produtos = []
for i in range(3):
    print("Insira o nome do produto:")
    nome = input()
    print("Insira o preço do produto:")
    preco = float(input())
    print("Insira a quantidade do produto:")
    quantidade = int(input())
    produtos.append([nome, preco, quantidade, (preco * quantidade)])

print(produtos)