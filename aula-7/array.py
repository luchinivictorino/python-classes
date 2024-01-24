# Crie um algoritmo em Python para ordenar o array:

numeros = [ 10, 4, 2, 8, 6, 1, 7, 9, 5 ]

#array.sort()
#print(array)

###################################################

# print("Números originais: ", numeros)
# for i in range(len(numeros)):
#     index_min = i
#     for j in range(i + 1, len(numeros)):
#         if (numeros[index_min] > numeros[j]):
#             index_min = j
    
#     numeros[i], numeros[index_min] = numeros[index_min], numeros[i]

# print("Números ordenados: ", numeros)

###################################################

# def insertionSort(array):
#     for i in range(1, len(array)):
#         j = i - 1
#         key = array[i]
#         while array[j] > key and j >= 0:
#             array[j + 1] = array[j]
#             j = j - 1
#         array[j + 1] = key

# list = [6, 5, 3, 1, 8, 7, 2, 4]
# insertionSort(list)
# print(list)

