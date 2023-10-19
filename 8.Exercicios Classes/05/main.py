from conta_corrente import ContaCorrente

if __name__ == "__main__":
    numero_conta = input("Digite o número da conta: ")
    nome_correntista = input("Digite o nome do correntista: ")
    saldo_inicial = float(input("Digite o saldo inicial (opcional, pressione Enter para saldo zero): ") or 0.0)

    conta = ContaCorrente(numero_conta, nome_correntista, saldo_inicial)

    print("Informações da conta corrente:")
    print(conta.informacoes())

    novo_nome = input("Digite o novo nome do correntista (ou pressione Enter para manter o nome atual): ")
    if novo_nome:
        conta.alterarNome(novo_nome)

    print("Informações da conta corrente atualizadas:")
    print(conta.informacoes())

    valor_deposito = float(input("Digite o valor do depósito (ou pressione Enter para nenhum depósito): ") or 0.0)
    if valor_deposito:
        conta.deposito(valor_deposito)

    print("Informações da conta corrente após o depósito:")
    print(conta.informacoes())

    valor_saque = float(input("Digite o valor do saque (ou pressione Enter para nenhum saque): ") or 0.0)
    if valor_saque:
        if conta.saque(valor_saque):
            print("Saque realizado com sucesso.")
        else:
            print("Saque não pode ser realizado devido a saldo insuficiente.")

    print("Informações da conta corrente após o saque:")
    print(conta.informacoes())
