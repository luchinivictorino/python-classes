class Queue:
    def __init__(self):
        self.items = []

#colocando um elemento na fila
    def enqueue(self, value):
        if value not in self.items:
            self.items.append(value)
        else:
            print('O valor ', value, ' já está na fila')

#removendo um elemento na fila
    def dequeue(self):
        if len(self.items) > 0:
            self.items.pop(0) #remove o índice 0
        else:
            print('Fila já está vazia!')

    def size(self):
        return len(self.items)

    def print(self):
        for item in self.items:
            print(item)        


filaPessoas = Queue()
filaPessoas.enqueue("João")
filaPessoas.enqueue("Maria")
filaPessoas.enqueue("Pedro")
filaPessoas.enqueue("José")
print('\nInício da fila:\n')
filaPessoas.print()
print('\nA fila andou:\n')
filaPessoas.dequeue()
filaPessoas.print()
print('\n')