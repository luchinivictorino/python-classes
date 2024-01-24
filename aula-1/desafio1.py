nome = input('Insira o nome: ')
salarioBruto = float(input('Insira o salário (em reais): '))
desconto = float(input('Insira o percentual de desconto: '))

salarioLiq = (salarioBruto * (desconto / 100))

print('Seu salário liquido é: ', salarioBruto - salarioLiq)