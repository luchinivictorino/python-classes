def heapify(array, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and array[i] < array[left]:
        largest = left

    if right < n and array[largest] < array[right]:
        largest = right
    
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)

def heapSort(array):
    n = len(array)

    for i in range(n // 2, -1, -1):
        heapify(array, n, i)

    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)


lista = [2,5,7,8,10,4,3,6,9,1]

print("Lista antes: ", lista)

heapSort(lista)

print("Lista depois: ", lista)