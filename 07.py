maior = 0
for cont in range(1, 6):
    num = int(input(f"Informe o {cont}º numero: "))
    if num > maior:
        maior = num

print(f"O maior número digitado é: {maior}")
