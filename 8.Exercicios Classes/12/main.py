from ContaInvestimento import ContaInvestimento

def main():
    saldo_inicial = float(input("Digite o saldo inicial da conta de investimento: R$"))
    taxa_juros = float(input("Digite a taxa de juros (em porcentagem): "))

    conta = ContaInvestimento(saldo_inicial, taxa_juros)

    for _ in range(5):
        conta.adicioneJuros()

    saldo_final = conta.saldo

    print(f"Saldo final após 5 aplicações de juros: R${saldo_final:.2f}")

if __name__ == "__main__":
    main()
