from ponto import Ponto

class Retangulo:
    def __init__(self, ponto_inicial, largura, altura):
        self.ponto_inicial = ponto_inicial
        self.largura = largura
        self.altura = altura

    def encontrarCentro(self):
        x_centro = self.ponto_inicial.x + self.largura / 2
        y_centro = self.ponto_inicial.y + self.altura / 2
        return Ponto(x_centro, y_centro)

    def imprimirCentro(self):
        centro = self.encontrarCentro()
        return f"Centro do Retângulo: {centro.imprimir()}"
