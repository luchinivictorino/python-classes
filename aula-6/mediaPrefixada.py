# 2) Implemente o algoritmo que calcule a média pré-fixada em um array, conforme o algoritmo abaixo. Complexidade O(n2).

def mediaPrefixada(X):
    n = len(X)
    A = [0] * n

    for i in range(n):
        a = 0
        for j in range(i + 1):
            a += X[j]
        A[i] = a / (i + 1)

    return A

list = [1, 2, 3, 4, 5]
mediaPref = mediaPrefixada(list)
print("Média pré-fixada:", mediaPref)