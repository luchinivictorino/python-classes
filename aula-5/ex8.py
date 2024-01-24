# 8) Crie uma fila de carros para serem lavados no posto do bairro.

class PostoDoBairro:
    def __init__(self):
        self.filaCarros = []

    def proximoCarro(self, carro):
        self.filaCarros.append(carro)
        print(f"Um {carro} entrou na fila.")

    def lavarProx(self):
        if not self.filaCarros:
            print("A fila esvaziou")
        else:
            carro = self.filaCarros.pop(0)
            print(f"O {carro} entrou para a lavação.")

    def printarFila(self):
        if not self.filaCarros:
            print("Não há carros na fila")
        else:
            print("Fila de lavação:")
            for carro in self.filaCarros:
                print(carro)

printar = PostoDoBairro()

printar.proximoCarro("Fuscão Preto")
printar.proximoCarro("Fuscão Azul")
printar.proximoCarro("Fuscão Vermelho")
print("\n")
printar.printarFila()
print("\n")
printar.lavarProx()
printar.lavarProx()
print("\n")
printar.printarFila()