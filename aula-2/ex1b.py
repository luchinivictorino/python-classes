#lista de números pares:

numeros = []
for i in range(4):
    print("Digite um número inteiro e par:")
    numero = int(input())
    if numero % 2 == 0:
        numeros.append(numero)
    else:
        print("O número digitado não é par.")

print(numeros)