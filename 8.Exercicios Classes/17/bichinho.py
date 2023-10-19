import random

class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = random.randint(0, 10)
        self.tedio = random.randint(0, 10)

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira

    def passarTempo(self, horas):
        self.fome += 0.5 * horas
        self.tedio += 1 * horas

    def humor(self):
        if self.fome >= 10 or self.tedio >= 10:
            return "Triste"
        else:
            return "Feliz"

    def __str__(self):
        return f"Bichinho {self.nome} - Fome: {self.fome}, Tédio: {self.tedio}"

