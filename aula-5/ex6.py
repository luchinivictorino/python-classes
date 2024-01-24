# 1) Crie uma pilha para armazenar nomes de documentos. Cada documento terá um nome.

class pilhaDoc:
    def __init__(self):
        self.documentos = []

    def empilhar(self, nome_documento):
        self.documentos.append(nome_documento)

    def printPilha(self):
        for documento in self.documentos:
            print(documento)

    def tamanho(self):
        return len(self.documentos)

    def desempilhar(self):
        if not self.vazia():
            return self.documentos.pop()
        else:
            return None

    def vazia(self):
        return len(self.documentos) == 0
    
pilha = pilhaDoc()

pilha.empilhar("Doc1")
pilha.empilhar("Doc2")
pilha.empilhar("Doc3")

print("\n")

print("Pilha: ")
pilha.printPilha()
print("\n")

print("Tamanho da pilha: ", pilha.tamanho())
print("\n")

#removerDoc = pilha.desempilhar()
#if removerDoc:
#    print("Documento removido: ", removerDoc)
#print("\n")

print("Tamanho da pilha após a remoção: ", pilha.tamanho())