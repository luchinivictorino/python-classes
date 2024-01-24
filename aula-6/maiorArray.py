# 1) Implemente o algoritmo de busca do maior valor de um array. Complexidade: O(n)

def arrayMax(A, n):
    currMax = A[0]  

    for i in range(1, n):  
        if currMax < A[i]: 
            currMax = A[i]
    return currMax  

list = [3, 7, 1, 9, 4, 6]
valorMax = arrayMax(list, len(list))
print("O maior valor no array é: ", valorMax)
