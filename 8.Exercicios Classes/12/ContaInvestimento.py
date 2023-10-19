class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  # Convertendo a taxa de porcentagem para decimal

    def adicioneJuros(self):
        self.saldo += self.saldo * self.taxa_juros
