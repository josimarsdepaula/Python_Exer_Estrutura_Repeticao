while True:
    populacao_a = int(input("Informe a quantidade de habitantes A: "))
    while populacao_a < 0:
        print("Valor inválido, Favor informar um número maior de Zero.")
        populacao_a = int(input("Informe a quantidade de habitantes A: "))

    populacao_b = int(input("Informe a quantidade de habitantes B: "))
    while populacao_b < 0:
        print("Valor inválido, Favor informar um número maior de Zero.")
        populacao_b = int(input("Informe a quantidade de habitantes B: "))

    taxa_crescimento_a = float(input("Informe a taxa de crescimento para população A: "))
    while taxa_crescimento_a < 0:
        print("Valor inválido, Favor informar uma taxa maior ou igual a Zero.")
        taxa_crescimento_a = float(input("Informe a quantidade de habitantes A: "))

    taxa_crescimento_b = float(input("Informe a taxa de crescimento para população B: "))
    while taxa_crescimento_b < 0:
        print("Valor inválido, Favor informar uma taxa maior ou igual a Zero.")
        taxa_crescimento_b = float(input("Informe a quantidade de habitantes B: "))

    anos = 0

    while populacao_a < populacao_b:
        populacao_a += populacao_a * taxa_crescimento_a
        populacao_b += populacao_b * taxa_crescimento_b
        anos += 1
    print(f"A Quantidade de anos necessários para a população (A) ultrapassar ou igualar população B é de: {anos} anos")

    repetir = input("Deseja repetir essa operação? (S - Sim, N - Não):").strip().upper()

    while repetir not in ("S", "N"):
        print("Valor Inválido")
        repetir = input("Deseja repetir essa operação? (S - Sim, N - Não):").strip().upper()

    if repetir == "N":
        break
