# 5) Implemente o algoritmo de ordenação Merge Sort com 20 elementos;

def mergeSort(list, left, right):
    if(left < right):
        middle = int((left + right) / 2)
        mergeSort(list, left, middle)
        mergeSort(list, middle + 1, right)
        merge(list, left, middle, right)

def merge(list, left, middle, right):
    #cria vetor vazio com tamanho do subvetor
    vector = [None] * (right - left + 1)
    i = left
    j = middle + 1
    k = 0

    while(i <= middle and j <= right):
        if(list[i] < list[j]):
            vector[k] = list[i]
            i = i + 1
        else:
            vector[k] = list[j]
            j = j + 1
        k = k + 1

    while(i <= middle):
        vector[k] = list[i]
        i = i + 1
        k = k + 1

    while(j <= right):
        vector[k] = list[j]
        j = j + 1
        k = k + 1
    
    for l in range(0, k):
        list[left + l] = vector[l]

list = [5, 10, 3, 69, 24, 143, 9, 40, 98, 1, 23, 11, 12, 54, 123, 42435, 65, 77, 2, 4]
mergeSort(list, 0, len(list) - 1)
print(list)