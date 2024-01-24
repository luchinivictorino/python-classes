# 9) Crie uma pilha de tarefas a serem executadas.

class pilhaTarefas:
    def __init__(self):
        self.tarefas = []

    def addTarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def exeTarefa(self):
        if self.tarefas:
            tarefa = self.tarefas.pop()
            tarefa()

    def tamanhoPilha(self):
        return len(self.tarefas)

def tarefa1():
    print("Comprar um fusca")

def tarefa2():
    print("Pintar o fusca")

def tarefa3():
    print("Passear com o fusca")

printar = pilhaTarefas()

printar.addTarefa(tarefa1)
printar.addTarefa(tarefa2)
printar.addTarefa(tarefa3)