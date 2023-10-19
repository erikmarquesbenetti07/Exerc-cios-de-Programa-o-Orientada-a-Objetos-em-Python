from retangulo import Retangulo

if __name__ == "__main__":
    # Solicitar entrada do usuário para as medidas do local
    lado_a = float(input("Digite o comprimento do local: "))
    lado_b = float(input("Digite a largura do local: "))

    # Cria uma instância da classe Retangulo com as medidas fornecidas pelo usuário
    local = Retangulo(lado_a, lado_b)

    # Exibe as medidas do local, a área e o perímetro
    print("Medidas do local (Comprimento x Largura):", local.retornarLados())
    print("Área do local:", local.calcularArea())
    print("Perímetro do local:", local.calcularPerimetro())

    # Cálculo da quantidade de pisos e rodapés necessários
    tamanho_piso = float(input("Digite o tamanho do piso em metros quadrados: "))
    tamanho_rodape = float(input("Digite o tamanho do rodapé em metros: "))

    area_local = local.calcularArea()
    quantidade_pisos = area_local / tamanho_piso
    quantidade_rodapes = local.calcularPerimetro() * tamanho_rodape

    print("Quantidade de pisos necessários:", quantidade_pisos)
    print("Quantidade de rodapés necessários:", quantidade_rodapes)
