from macaco import Macaco

if __name__ == "__main__":
    macaco1 = Macaco("Macaco A")
    macaco2 = Macaco("Macaco B")

    for i in range(3):
        comida = input(f"Digite a comida para Macaco A na refeição {i + 1}: ")
        macaco1.comer(comida)

        comida = input(f"Digite a comida para Macaco B na refeição {i + 1}: ")
        macaco2.comer(comida)

        print(f"Conteúdo do estômago de {macaco1.nome}: {macaco1.verBucho()}")
        print(f"Conteúdo do estômago de {macaco2.nome}: {macaco2.verBucho()}")
        macaco1.digerir()
        macaco2.digerir()
        print(f"Após digestão, conteúdo do estômago de {macaco1.nome}: {macaco1.verBucho()}")
        print(f"Após digestão, conteúdo do estômago de {macaco2.nome}: {macaco2.verBucho()}")
