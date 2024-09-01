from Calculadora import Calculadora

# Criando uma instância da calculadora
calculadora = Calculadora(10, 10, "*")

# Mostrando o resultado
calculadora.mostrarResultado()

from Calculadora import Calculadora

def obter_dados_usuario():
    valorA = float(input("Digite o primeiro valor: "))
    valorB = float(input("Digite o segundo valor: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    return valorA, valorB, operacao

valorA, valorB, operacao = obter_dados_usuario()
calculadora = Calculadora(valorA, valorB, operacao)
calculadora.mostrarResultado()