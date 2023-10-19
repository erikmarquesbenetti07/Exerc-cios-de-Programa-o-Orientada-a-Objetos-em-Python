from carro import Carro

def main():
    consumo = float(input("Digite o consumo de combustível do carro (km por litro): "))
    meu_carro = Carro(consumo)

    while True:
        print("\nEscolha uma opção:")
        print("1. Abastecer o carro")
        print("2. Dirigir o carro")
        print("3. Verificar nível de combustível")
        print("4. Sair")

        opcao = input("Opção (1/2/3/4): ")

        if opcao == "1":
            litros = float(input("Quantos litros deseja abastecer? "))
            meu_carro.adicionarGasolina(litros)
            print(f"Carro abastecido com {litros} litros de combustível.")

        elif opcao == "2":
            distancia = float(input("Quantos quilômetros deseja percorrer? "))
            resultado = meu_carro.andar(distancia)
            print(resultado)

        elif opcao == "3":
            print(meu_carro.obterGasolina())

        elif opcao == "4":
            print("Encerrando o programa.")
            break

        else:
            print("Opção inválida. Escolha 1, 2, 3 ou 4.")

if __name__ == "__main__":
    main()
