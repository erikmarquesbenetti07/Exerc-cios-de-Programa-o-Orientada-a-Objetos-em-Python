from pessoa import Pessoa

if __name__ == "__main__":
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    peso = float(input("Digite o peso da pessoa (em kg): "))
    altura = float(input("Digite a altura da pessoa (em metros): "))

    pessoa = Pessoa(nome, idade, peso, altura)

    print("Informações iniciais da pessoa:")
    print(pessoa.info())

    anos = int(input("Digite quantos anos a pessoa envelhecerá: "))
    pessoa.envelhecer(anos)

    peso_ganho = float(input("Digite quantos quilos a pessoa ganhará: "))
    pessoa.engordar(peso_ganho)

    peso_perdido = float(input("Digite quantos quilos a pessoa perderá: "))
    pessoa.emagrecer(peso_perdido)

    altura_ganha = float(input("Digite quantos metros a pessoa crescerá: "))
    pessoa.crescer(altura_ganha)

    print("Informações atualizadas da pessoa:")
    print(pessoa.info())
