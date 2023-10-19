from fazendaBichinhos import FazendaDeBichinhos

def main():
    fazenda = FazendaDeBichinhos()

    num_bichinhos = int(input("Digite o número de bichinhos na fazenda: "))
    for i in range(1, num_bichinhos + 1):
        nome = input(f"Digite o nome do bichinho {i}: ")
        fazenda.adicionarBichinho(nome)

    while True:
        print("\nEscolha uma ação para todos os bichinhos na fazenda:")
        print("1. Alimentar todos os bichinhos")
        print("2. Brincar com todos os bichinhos")
        print("3. Ouvir todos os bichinhos")
        print("4. Sair")

        acao = input("Ação (1/2/3/4): ")

        if acao == "1":
            quantidade_comida = float(input("Quantidade de comida para todos os bichinhos (porção): "))
            fazenda.alimentarTodos(quantidade_comida)
            print("Você alimentou todos os bichinhos na fazenda.")

        elif acao == "2":
            tempo_brincadeira = float(input("Tempo de brincadeira para todos os bichinhos (horas): "))
            fazenda.brincarTodos(tempo_brincadeira)
            print("Você brincou com todos os bichinhos na fazenda.")

        elif acao == "3":
            fazenda.ouvirTodos()

        elif acao == "4":
            print("Encerrando o programa.")
            break

        else:
            print("Ação inválida. Escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
