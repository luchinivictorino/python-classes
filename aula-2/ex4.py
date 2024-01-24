# 4) Crie um programa que calcule o dobro dos valores da diagonal principal de uma matriz 3X3.

def calcular_dobro_diagonal_principal(matriz):

    diagonal_principal = [matriz[i][i] * 2 for i in range(3)]
    return diagonal_principal

#trocar os valores da matriz para outro resultado
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

dobro_diagonal_principal = calcular_dobro_diagonal_principal(matriz)
print("Dobro da diagonal principal:", dobro_diagonal_principal)