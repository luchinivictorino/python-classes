# 2) Crie 2 listas encadeadas, na primeira insira 20 números distintos entre
# si, do início para o fim. A medida que inserir o valor na primeira, adicione
# de trás para frente o valor na segunda lista.

import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

class ListaDeNumeros:

    def __init__(self):
        self.lista1 = LinkedList()
        self.gerarNumAleatorio(20)

    def gerarNumAleatorio(self, n):
        numAleatorio = set()
        while len(numAleatorio) < n:
            numAleatorio.add(random.randint(1,50))
        for num in numAleatorio:
            self.lista1.append(num)

    def listaReversa(self):
        dobroReverso = []
        current = self.lista1.head
        while current:
            dobroReverso.insert(0, current.data * 2)
            current = current.next
        return dobroReverso
    
if __name__ == "__main__":
    listaNormal = ListaDeNumeros()
    listaDobroReverso = listaNormal.listaReversa()

    print("Lista Normal: ")
    current = listaNormal.gerarNumAleatorio.head
    while current:
        print(current.data)
        current = current.next

    print("\nLista dobro inverso: ")
    for num in  listaDobroReverso:
        print(num)







    # if __name__ == "__main__":
    #     numAleatorio = gerarNumAleatorio(20)
    # listaEnc = LinkedList()
    # for numero in numAleatorio:
    #     listaEnc.append(numero)

    # current = listaEnc.head
    # while current:
    #     print(current.data)
    #     current = current.next
