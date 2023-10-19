class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obterNome(self):
        return self.nome

    def obterSalario(self):
        return self.salario

    def aumentarSalario(self, porcentagem_de_aumento):
        aumento = self.salario * (porcentagem_de_aumento / 100)
        self.salario += aumento

