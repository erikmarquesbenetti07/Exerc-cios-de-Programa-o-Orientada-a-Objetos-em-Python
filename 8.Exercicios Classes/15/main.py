from BichinhoVirtual import BichinhoVirtual

def main():
    nome = input("Digite o nome do seu bichinho virtual: ")
    bichinho = BichinhoVirtual(nome)

    print(f"\nSeu bichinho virtual {bichinho.nome} foi criado!")

    while True:
        print("\nEscolha uma ação para o seu bichinho:")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Passar o tempo")
        print("4. Ver humor do bichinho")
        print("5. Sair")

        acao = input("Ação (1/2/3/4/5): ")

        if acao == "1":
            quantidade_comida = float(input("Quantidade de comida para alimentar (porção): "))
            bichinho.alimentar(quantidade_comida)
            print(f"Você alimentou o seu bichinho {bichinho.nome}.")

        elif acao == "2":
            tempo_brincadeira = float(input("Tempo de brincadeira (horas): "))
            bichinho.brincar(tempo_brincadeira)
            print(f"Você brincou com o seu bichinho {bichinho.nome}.")

        elif acao == "3":
            horas = float(input("Horas que passaram: "))
            bichinho.passarTempo(horas)
            print(f"O tempo passou para o seu bichinho {bichinho.nome}.")

        elif acao == "4":
            print(f"O humor do seu bichinho {bichinho.nome} está: {bichinho.humor()}")

        elif acao == "5":
            print("Encerrando o programa.")
            break

        else:
            print("Ação inválida. Escolha 1, 2, 3, 4 ou 5.")

if __name__ == "__main__":
    main()
