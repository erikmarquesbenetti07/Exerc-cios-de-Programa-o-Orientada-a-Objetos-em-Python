from bichinho import BichinhoVirtual

class FazendaDeBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionarBichinho(self, nome):
        bichinho = BichinhoVirtual(nome)
        self.bichinhos.append(bichinho)

    def alimentarTodos(self, quantidade_comida):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade_comida)

    def brincarTodos(self, tempo_brincadeira):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo_brincadeira)

    def ouvirTodos(self):
        for bichinho in self.bichinhos:
            print(bichinho)

