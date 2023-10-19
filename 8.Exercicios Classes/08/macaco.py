class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []

    def __str__(self):
        return f"Nome: {self.nome}, Bucho: {self.bucho}"

