from bombaCombustivel import BombaCombustivel

def main():
    tipo_combustivel = input("Digite o tipo de combustível da bomba: ")
    valor_litro = float(input("Digite o valor por litro: "))
    quantidade_combustivel = float(input("Digite a quantidade de combustível na bomba (litros): "))

    bomba = BombaCombustivel(tipo_combustivel, valor_litro, quantidade_combustivel)

    while True:
        print("\nEscolha uma opção:")
        print("1. Abastecer por Valor")
        print("2. Abastecer por Litro")
        print("3. Alterar Valor do Litro")
        print("4. Alterar Tipo de Combustível")
        print("5. Alterar Quantidade de Combustível na Bomba")
        print("6. Informações da Bomba")
        print("7. Sair")

        opcao = input("Opção (1/2/3/4/5/6/7): ")

        if opcao == "1":
            valor = float(input("Digite o valor a ser abastecido: "))
            resultado = bomba.abastecerPorValor(valor)
            print(resultado)

        elif opcao == "2":
            litros = float(input("Digite a quantidade de litros a ser abastecida: "))
            resultado = bomba.abastecerPorLitro(litros)
            print(resultado)

        elif opcao == "3":
            novo_valor_litro = float(input("Digite o novo valor por litro: "))
            bomba.alterarValor(novo_valor_litro)

        elif opcao == "4":
            novo_tipo_combustivel = input("Digite o novo tipo de combustível: ")
            bomba.alterarCombustivel(novo_tipo_combustivel)

        elif opcao == "5":
            nova_quantidade = float(input("Digite a nova quantidade de combustível na bomba (litros): "))
            resultado = bomba.alterarQuantidadeCombustivel(nova_quantidade)
            if resultado:
                print(resultado)
            else:
                print("Quantidade de combustível atualizada com sucesso.")

        elif opcao == "6":
            print(bomba.informacoes())

        elif opcao == "7":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Escolha 1, 2, 3, 4, 5, 6 ou 7.")

if __name__ == "__main__":
    main()
