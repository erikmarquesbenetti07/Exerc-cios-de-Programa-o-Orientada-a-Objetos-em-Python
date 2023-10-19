from tv import TV

if __name__ == "__main__":
    minha_tv = TV()

    while True:
        print("Estado da TV:", minha_tv.informacoes())
        print("Opções:")
        print("1. Definir Canal")
        print("2. Aumentar Volume")
        print("3. Diminuir Volume")
        print("4. Sair")

        opcao = input("Escolha uma opção (1/2/3/4): ")

        if opcao == "1":
            numero_canal = int(input("Digite o número do canal desejado: "))
            minha_tv.definirCanal(numero_canal)
        elif opcao == "2":
            minha_tv.aumentarVolume()
        elif opcao == "3":
            minha_tv.diminuirVolume()
        elif opcao == "4":
            print("Desligando a TV.")
            break
        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")

