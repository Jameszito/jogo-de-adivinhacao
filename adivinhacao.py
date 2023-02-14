import random

def jogar():

    print("********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?", numero_secreto)
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input ("Defina um nível: "))
    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))

        chute_str = input("Digite o seu número entre 1 e 100: ")
        print("Você digitou", chute_str )
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número maior entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        chute_maior =  chute > numero_secreto
        chute_menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos !".format(pontos))
            break
        else:
            if (chute_maior):
                print("Seu chute foi maior que número o secreto")
                if(rodada == total_de_tentativas):
                    print("O número secreto era {}. Você fez {}".format(numero_secreto, pontos))
            elif (chute_menor):
                print("Seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()
