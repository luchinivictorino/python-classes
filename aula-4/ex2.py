# 2) Crie uma fila para controlar as pessoas que estão
# esperando para serem atendidas em um consultório médico.

class Consultorio:
    def __init__(self):
        self.filaEspera = []

    def pacienteNovo(self, nome):
        self.filaEspera.append(nome)
        print(f"{nome} entrou na fila de espera.")

    def atenderPaciente(self):
        if self.filaEspera:
            proxima_pessoa = self.filaEspera.pop(0)
            print(f"{proxima_pessoa} está sendo atendido.")
        else:
            print("Todos já foram atendidos.")

printar = Consultorio()

print("\n")
printar.pacienteNovo("Paciente 1")
printar.pacienteNovo("Paciente 2")
printar.pacienteNovo("Paciente 3")

print("\n")

printar.atenderPaciente()
printar.atenderPaciente()
printar.atenderPaciente()
printar.atenderPaciente()
