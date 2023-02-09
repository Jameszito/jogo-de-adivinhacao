print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 43

chute_str = input("Digite o seu número: ")

print("Você digitou", chute_str )

chute = int(chute_str)

acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if (acertou):
    print("Você acertou!")
else:
    if (chute_maior):
        print("Seu chute foi maior que número o secreto")
    elif (chute_menor):
        print("Seu chute foi menor que o número secreto")

print("Fim do jogo!")
