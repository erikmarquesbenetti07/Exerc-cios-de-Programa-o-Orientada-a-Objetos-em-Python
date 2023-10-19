from BichinhoVirtual import BichinhoVirtual

if __name__ == "__main__":
    nome = input("Digite o nome do seu Tamagushi: ")
    fome = float(input("Digite o nível de fome (de 0 a 100): "))
    saude = float(input("Digite o nível de saúde (de 0 a 100): "))
    idade = int(input("Digite a idade do seu Tamagushi: "))

    meu_bichinho = BichinhoVirtual(nome, fome, saude, idade)

    while True:
        print("Estado do Tamagushi:", meu_bichinho.informacoes())
        print("Opções:")
        print("1. Alterar Nome")
        print("2. Alterar Fome")
        print("3. Alterar Saúde")
        print("4. Alterar Idade")
        print("5. Sair")

        opcao = input("Escolha uma opção (1/2/3/4/5): ")

        if opcao == "1":
            novo_nome = input("Digite o novo nome do Tamagushi: ")
            meu_bichinho.alterarNome(novo_nome)
        elif opcao == "2":
            nova_fome = float(input("Digite o novo nível de fome (de 0 a 100): "))
            meu_bichinho.alterarFome(nova_fome)
        elif opcao == "3":
            nova_saude = float(input("Digite o novo nível de saúde (de 0 a 100): "))
            meu_bichinho.alterarSaude(nova_saude)
        elif opcao == "4":
            nova_idade = int(input("Digite a nova idade do Tamagushi: "))
            meu_bichinho.alterarIdade(nova_idade)
        elif opcao == "5":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3, 4 ou 5.")
