# 4) Crie um algoritmo para calcular o Fatorial de um número. Detalhe, desenvolva um algoritmo recursivo. Complexidade O(n).

def fatorial(n):
    if n <= 0:
        return 1
    else:
        return n * fatorial(n - 1)


numero = 3
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: ", resultado)