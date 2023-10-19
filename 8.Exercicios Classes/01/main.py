from bola import Bola

if __name__ == "__main__":
    # Solicitar entrada do usuário para os atributos da bola
    cor = input("Digite a cor da bola: ")
    circunferencia = float(input("Digite a circunferência da bola: "))
    material = input("Digite o material da bola: ")

    # Cria uma instância da classe Bola com os valores fornecidos pelo usuário
    minha_bola = Bola(cor, circunferencia, material)

    # Exibe os atributos da bola
    print("Atributos da bola:")
    print("Cor:", minha_bola.mostraCor())
    print("Circunferência:", minha_bola.circunferencia)
    print("Material:", minha_bola.material)

    # Solicitar ao usuário para trocar a cor da bola
    nova_cor = input("Digite a nova cor da bola: ")
    minha_bola.trocaCor(nova_cor)

    # Exibe a nova cor da bola
    print("Nova cor da bola:", minha_bola.mostraCor())
