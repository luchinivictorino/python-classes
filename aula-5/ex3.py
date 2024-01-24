# 3) Crie uma lista encadeada com 20 números aleatórios. Após a inserção
# mostre os valores que são maiores que o primeiro valor. E mostre todos
# os valores pares.

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    print("=========================")

def maiorPrimeiro(lista, valor1):
    atual = lista
    print("Valores maiores que o primeiro:")
    while atual:
        if atual.data > valor1:
            print(atual.data, end=' ')
        atual = atual.next
    print()

    print("=========================")

def valorPar(lista):
    atual = lista
    print("Valores pares:")
    while atual:
        if atual.data % 2 == 0:
            print(atual.data, end=' ')
        atual = atual.next
    print()

    print("=========================")

valor1 = random.randint(1, 50)
head = Node(valor1)
current = head

for _ in range(19):
    valorNovo = random.randint(1, 50)
    current.next = Node(valorNovo)
    current = current.next

maiorPrimeiro(head, valor1)

valorPar(head)
