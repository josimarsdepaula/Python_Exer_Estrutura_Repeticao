nome = input("Informe seu nome: ")
while len(nome) <= 3:
    print("Nome Inválido. Insira novamente acima de 3 caracteres.")
    nome = input("Informe seu nome: ")

idade = int(input("Informe sua Idade: "))
while not idade > 0 and idade >= 150:
    print("Idade inválida. Insira novamente entre 0 e 150 anos.") 
    idade = input("Informe sua Idade: ")

salario = float(input("Informe seu sálario: "))
while salario < 0:
    print("salário inválido. Insira novamente.")
    salario = float(input("Informe seu salário: "))

sexo = input("Informe qual o seu sexo (F) - Feminino ou (M) - Masculino: ")
while len(sexo) > 1 and sexo not in ("m", "f"):
    print("Sexo inválido. Insira novamente.")
    sexo = input("Informe qual o seu sexo (F) - Feminino ou (M) - Masculino: ")

lista_estado_civil = [
    "(C) - Casado(a)",
    "(S) - Solteiro(a)",
    "(V) - Viúvo(a)",
    "(D) - Divorciado(a)"
]

for estado in lista_estado_civil:
    print(estado)

estado_civil = input(f"Informe a letra conforme seu estado civil: ").strip().upper()
while estado_civil not in ("S", "C", "V", "D"):
    print("Estado Civil inválido. Insira novamente.")
    estado_civil = input(f"Informe a letra conforme seu estado civil: ").strip().upper()






