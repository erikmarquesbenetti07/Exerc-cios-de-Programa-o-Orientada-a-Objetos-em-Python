from quadrado import Quadrado

if __name__ == "__main__":
    # Solicitar entrada do usuário para o tamanho do lado
    lado = float(input("Digite o tamanho do lado do quadrado: "))

    # Cria uma instância da classe Quadrado com o valor fornecido pelo usuário
    meu_quadrado = Quadrado(lado)

    # Exibe o tamanho do lado e a área do quadrado
    print("Tamanho do lado:", meu_quadrado.retornarLado())
    print("Área do quadrado:", meu_quadrado.calcularArea())

    # Solicitar ao usuário para mudar o tamanho do lado do quadrado
    novo_lado = float(input("Digite o novo tamanho do lado do quadrado: "))
    meu_quadrado.mudarLado(novo_lado)

    # Exibe o novo tamanho do lado e a nova área do quadrado
    print("Novo tamanho do lado:", meu_quadrado.retornarLado())
    print("Nova área do quadrado:", meu_quadrado.calcularArea())
