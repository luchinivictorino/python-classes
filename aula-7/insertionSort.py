# 3) Implemente o algoritmo de ordenação Insertion Sort;

def insertionSort(array):
    for i in range(1, len(array)):
        j = i - 1
        key = array[i]
        while array[j] > key and j >= 0:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

list = [5, 10, 3, 69, 24, 143, 9, 40, 98, 1, 23, 11, 12, 54, 123, 42435, 65, 77, 2, 4]
insertionSort(list)
print("Insertionsort: ", list)