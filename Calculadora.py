class Calculadora:
    def __init__(self, valorA, valorB, operacao):
        self.__valorA = valorA
        self.__valorB = valorB
        self.__operacao = operacao

    @property
    def valorA(self):
        return self.__valorA

    @valorA.setter
    def valorA(self, valorA):
        self.__valorA = valorA

    @property
    def valorB(self):
        return self.__valorB

    @valorB.setter
    def valorB(self, valorB):
        self.__valorB = valorB

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao):
        self.__operacao = operacao

    def validarOperacao(self):
        operacoes_validas = ['+', '-', '*', '/']
        return self.__operacao in operacoes_validas

    def calcular(self):
        if not self.validarOperacao():
            print("Operação inválida!")
            exit()

        if self.__operacao == '+':
            resultado = self.__valorA + self.__valorB
        elif self.__operacao == '-':
            resultado = self.__valorA - self.__valorB
        elif self.__operacao == '*':
            resultado = self.__valorA * self.__valorB
        elif self.__operacao == '/':
            if self.__valorB == 0:
                print("Divisão por zero!")
                exit()
            resultado = self.__valorA / self.__valorB
        return resultado

    def mostrarResultado(self):
        print(str(self.valorA) + ' ' + self.operacao + ' ' + str(self.valorB) + ' = ' + str(self.calcular()))