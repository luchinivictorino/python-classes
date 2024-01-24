# # 4) Implemente o algoritmo de ordenação Quick Sort com 20 elementos;

def quickSort(list, left, right):
    if(left < right):
        splitpoint = partition(list, left, right)
        quickSort(list, left, splitpoint - 1)
        quickSort(list, splitpoint + 1, right)

def partition(list, left, right):
    pivot = list[right]
    i = left

    for j in range(left, right):
        if(list[j] <= pivot):
            list[i], list[j] = list[j], list[i]
            i = i + 1

    list[i], list[right] = list[right], list[i]
    return i

list = [5, 10, 3, 69, 24, 143, 9, 40, 98, 1, 23, 11, 12, 54, 123, 42435, 65, 77, 2, 4]
quickSort(list, 0, len(list)-1)
print("Quicksort: ", list)