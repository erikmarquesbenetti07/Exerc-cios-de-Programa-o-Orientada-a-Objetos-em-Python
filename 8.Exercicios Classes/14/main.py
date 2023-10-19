from funcionario import Funcionario

def main():
    nome = input("Digite o nome do funcionário: ")
    salario = float(input("Digite o salário do funcionário: R$"))

    funcionario = Funcionario(nome, salario)

    print("\nInformações do funcionário:")
    print(f"Nome: {funcionario.obterNome()}")
    print(f"Salário: R${funcionario.obterSalario():.2f}")

    porcentagem_de_aumento = float(input("\nDigite a porcentagem de aumento de salário: "))
    funcionario.aumentarSalario(porcentagem_de_aumento)

    print("\nInformações do funcionário após o aumento de salário:")
    print(f"Nome: {funcionario.obterNome()}")
    print(f"Salário: R${funcionario.obterSalario():.2f}")

if __name__ == "__main__":
    main()
