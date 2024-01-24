# 2) Implemente o algoritmo de ordenação Selection Sort com 20 elementos;

def selectionSort(list):
    for index in range(len(list)):
        min_index = index
        for j in range(index + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[index], list[min_index] = list[min_index], list[index]

list = [5, 10, 3, 69, 24, 143, 9, 40, 98, 1, 23, 11, 12, 54, 123, 42435, 65, 77, 2, 4]
selectionSort(list)
print("Selectionsort: ", list)