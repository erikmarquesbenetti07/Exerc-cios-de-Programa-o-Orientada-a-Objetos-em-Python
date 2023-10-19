class TV:
    def __init__(self):
        self.canal = 1
        self.volume = 10

    def definirCanal(self, numero_canal):
        if 1 <= numero_canal <= 100:
            self.canal = numero_canal
        else:
            print("Canal inválido. Os canais válidos estão na faixa de 1 a 100.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume máximo atingido.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume mínimo atingido.")

    def informacoes(self):
        return f"Canal: {self.canal}, Volume: {self.volume}"

