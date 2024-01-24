# 2) Crie duas listas encadeadas. Insira números
#       aleatórios na primeira. A cada número inserido
#      na primeira, insira o dobro do valor na segunda.

class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextData = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printLista(self):
        printdata = self.head
        while printdata is not None:
            print(printdata.data)
            printdata = printdata.nextData

    def inserir(self, data):
        NewNode = Node(data)
        NewNode.nextData = self.head
        self.head = NewNode

    def inserirDobro(self, data):
        NewNode = Node(data * 2)
        NewNode.nextData = self.head
        self.head = NewNode

# Criando as duas listas
lista1 = LinkedList()
lista2 = LinkedList()

# Inserindo números aleatórios na primeira lista
numerosAleatorio = [3, 7, 2, 9, 5]
for numero in numerosAleatorio:
    lista1.inserir(numero)
    lista2.inserirDobro(numero)

# Imprimindo as duas listas
print("Primeira Lista:")
lista1.printLista()
print("\nSegunda Lista (dobro dos valores da primeira):")
lista2.printLista()
