class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0

    def andar(self, distancia_km):
        combustivel_necessario = distancia_km / self.consumo_km_por_litro
        if combustivel_necessario <= self.nivel_combustivel:
            self.nivel_combustivel -= combustivel_necessario
            return f"O carro percorreu {distancia_km} km."
        else:
            return "Combustível insuficiente para percorrer essa distância."

    def obterGasolina(self):
        return f"Nível de combustível atual: {self.nivel_combustivel} litros."

    def adicionarGasolina(self, litros):
        self.nivel_combustivel += litros
