# 1) Implemente o algoritmo de ordenação Bubble Sort com 20 elementos;

def bubbleSort(array):
    n = len(array)
    swapped = False
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
                return
            

list = [5, 10, 3, 69, 24, 143, 9, 40, 98, 1, 23, 11, 12, 54, 123, 42435, 65, 77, 2, 4]
bubbleSort(list)
print("Bubblesort: ", list)