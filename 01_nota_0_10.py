nota = float(input("Informe uma nota entre 0 e 10: "))
while nota > 10 or nota < 0:
    print("Valor Inválido! Favor informe uma nota entre 0 e 10.")
    nota = float(input("Informe uma nota entre 0 e 10: "))

print(f"Valor Válido! Nota informada: {nota}")