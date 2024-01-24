import time
import random

timeStart = time.time()

# n = 10000
# for i in range(n):
#     j = i
#     for j in range(n):
#         print(j)
#     print(i)

# def func(numero):
#     print(numero)
#     if numero >= 0:
#         return func(numero - 1)
#     else:
#         return 0

# func(n)

# def arrayMax(array):
#     currMax = array[0]
#     for i in range(1, len(array)):
#         if currMax < array[i]:
#             currMax = array[i]
#     return currMax

def arrayMax(array, currentMax):
    if len(array) >= 0 and i <= len(array):
        # print('i', i)
        if currentMax < array[i]:
            currentMax = array[i]
            arrayMax(array, currentMax)
        return currentMax

n = 1000
numeros = []
for i in range(n):
    numeros.append(random.randint(1, 100))

# numeros = [1, 2, 3, 6, 4, 7, 8, 10, 14, 20, 22, 27]

print(arrayMax(numeros, -1))

timeEnd = time.time()
print('seconds', timeEnd - timeStart)