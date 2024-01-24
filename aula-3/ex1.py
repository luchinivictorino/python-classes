# 1) Crie uma lista Encadeada
#       a) Crie o método para inicialização (slide);
#       b) Crie o método inserir um elemento no início da
#      Lista (slide);
#       c) Crie o método para inserir um elemento no final
#      da lista.

class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextData = None

class LinkedList:
    def __init__(self):
        self.head = None

    def listprint(self):
            printdata = self.head
            while printdata is not None:
                print(printdata.data)
                printdata = printdata.nextData

    def AtBegining(self, data):
            NewNode = Node(data)
            NewNode.nextData = self.head
            self.head = NewNode

    def AtEnd(self, data):
        NewNode = Node(data)
        if self.head is None:
            self.head = NewNode
            return
        lastNode = self.head
        while lastNode.nextData:
            lastNode = lastNode.nextData
        lastNode.nextData = NewNode

list = LinkedList()
list.head = Node("Quarta")
list.AtBegining("Terça")
list.AtBegining("Segunda")
list.AtEnd("Quinta")
print(list.listprint())