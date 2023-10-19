from ponto import Ponto
from retangulo import Retangulo

def main():
    ponto_inicial = Ponto(0, 0)
    retangulo = Retangulo(ponto_inicial, 4, 3)

    while True:
        print("\nEscolha uma opção:")
        print("1. Imprimir Retângulo")
        print("2. Encontrar e Imprimir Centro do Retângulo")
        print("3. Alterar Valores do Retângulo")
        print("4. Sair")

        opcao = input("Opção (1/2/3/4): ")

        if opcao == "1":
            print(f"Retângulo: Ponto Inicial ({ponto_inicial.x}, {ponto_inicial.y}), Largura {retangulo.largura}, Altura {retangulo.altura}")

        elif opcao == "2":
            centro = retangulo.encontrarCentro()
            print(retangulo.imprimirCentro())

        elif opcao == "3":
            x = float(input("Novo valor de X para o ponto inicial: "))
            y = float(input("Novo valor de Y para o ponto inicial: "))
            largura = float(input("Nova largura do retângulo: "))
            altura = float(input("Nova altura do retângulo: "))

            ponto_inicial = Ponto(x, y)
            retangulo = Retangulo(ponto_inicial, largura, altura)

        elif opcao == "4":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
