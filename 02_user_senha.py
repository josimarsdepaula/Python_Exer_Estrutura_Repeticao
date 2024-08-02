nome = input("Informe nome de usuário:")
senha = input("Informe uma senha:")

while nome == senha:
    print("Senha Inválida! Senha não pode ser igual ao usuário.")
    senha = input("Informe uma senha:")
print("Senha cadastrada com sucesso!")