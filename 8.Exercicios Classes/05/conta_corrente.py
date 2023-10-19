class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0.0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        else:
            return False

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return True
        else:
            return False

    def informacoes(self):
        return f"Número da Conta: {self.numero_conta}, Correntista: {self.nome_correntista}, Saldo: R${self.saldo:.2f}"
