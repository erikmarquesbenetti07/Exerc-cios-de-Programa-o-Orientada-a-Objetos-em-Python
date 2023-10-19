class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor):
        if valor <= 0:
            return "Valor inválido"
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            return "Quantidade de combustível insuficiente na bomba"
        self.quantidade_combustivel -= litros_abastecidos
        return f"Abastecidos {litros_abastecidos:.2f} litros. Valor a pagar: R${valor:.2f}"

    def abastecerPorLitro(self, litros):
        if litros <= 0:
            return "Quantidade de litros inválida"
        valor_pagar = litros * self.valor_litro
        if valor_pagar > self.quantidade_combustivel * self.valor_litro:
            return "Quantidade de combustível insuficiente na bomba"
        self.quantidade_combustivel -= litros
        return f"Abastecidos {litros:.2f} litros. Valor a pagar: R${valor_pagar:.2f}"

    def alterarValor(self, novo_valor_litro):
        self.valor_litro = novo_valor_litro

    def alterarCombustivel(self, novo_tipo_combustivel):
        self.tipo_combustivel = novo_tipo_combustivel

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        if nova_quantidade < 0:
            return "Quantidade de combustível inválida"
        self.quantidade_combustivel = nova_quantidade

    def informacoes(self):
        return f"Tipo de Combustível: {self.tipo_combustivel}, Valor por Litro: R${self.valor_litro:.2f}, Quantidade de Combustível: {self.quantidade_combustivel:.2f} litros"
