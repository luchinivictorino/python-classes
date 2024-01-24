class Stack :
    def __init__(self):
        self.itens = []

    def append(self, value):
        if value not in self.itens:
            self.itens.append(value)
        else:
            print("Valor ", value, "já está na lista!")

    def pop(self):
        if len(self.itens) > 0:
            self.itens.pop()
        else:
            print("Lista vazia")

    def print(self):
        for item in self.itens:
            print("Item", item)

    def size(self):
        return len(self.itens)

stack = Stack()
stack.append(5)
stack.append(6)
stack.append(10)
stack.append(11)
stack.append(15)
stack.print()
print(stack.size())