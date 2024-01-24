# 3) Implemente o algoritmo que realize uma busca de um elemento em um array e retorna o seu index. Complexidade O(n).

def acharIndex(x, A):
    n = len(A)

    for i in range(n):
        if x == A[i]:
            return i

    return -1

list = [1, 2, 3, 4, 5]
elemento = 5
index = acharIndex(elemento, list)
if index != -1:
    print(f"O elemento {elemento} foi encontrado no índice {index}.")
else:
    print(f"O elemento {elemento} não foi encontrado no array.")