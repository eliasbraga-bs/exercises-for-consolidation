#  Jogo simples de adivinhação
import random

numero_secreto = random.randint(1, 10)
tentativas = 0
adivinhou = False

print("Bem-vindo ao jogo de adivinhação!")
print("Estou pensado em um número entre 1 e 10.")

while not adivinhou:
    tantativa = int(input("Digite o seu palpite: "))
    tentativas += 1

    if tentativas == numero_secreto:
        print(f"Parabéns! Você acertou o número em {tantativa} tentativas.")
        adivinhou = True
    elif tantativa < numero_secreto:  
        print("Muito baixo! Tente novamente.")
    else:
        print("Muito alto! Tente novamente.")



        