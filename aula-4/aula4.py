numeros = []
print("Números", numeros, len(numeros))

#adicionar elementos no final
numeros.append(10)
numeros.append(12)
numeros.append(10)

#quantos elesmentos tem no array
print("Números", numeros, len(numeros))
#mostrar a quantidade de elementos "10" no array
print("Quantidade" ,numeros.count(10))
#adicionar elementos dentro do array (posição 2)
numeros.insert(2, 12)
print("Números", numeros, len(numeros))
#mostrar onde está o elemento
index = numeros.index(10, 1, len(numeros))
print("Index de 10", index)

numeros.remove(12)
print("Removendo um dos números 12##", numeros)
numeros.pop()
print("Removendo", numeros)