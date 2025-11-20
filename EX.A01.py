import random
nome = input("Insira o seu nome: ")
numero_aleatorio = random.randint(1, 20)
tentativas = 6
print(f"{nome}, adivinha o número entre 1 e 20")
while tentativas > 0:
    numero = int(input("Insira o valor: "))
    if numero == numero_aleatorio:
        print(f"Parabéns,tu acertaste,{nome}!")
        exit()
    elif numero > numero_aleatorio:
        print(f"Número incorreto, é inferior.")
        print(f"ainda lhe restam {tentativas} tentativas!")
    elif numero < numero_aleatorio:
        print("Número incorreto, é superior.")
tentativas -= 1
print(f"ainda lhe restam {tentativas} tentativas!")
print(f"Acabaram as tuas tentativas o numero correto era o {numero}!")
print("queres jogar novamente?")
escolha = input("Sim (S) ou Não (N): ").lower()
if escolha == "s":
    print("ok vamos la!")
numero_aleatorio = random.randint(1, 20)
tentativas = 6
print(f"{nome}, adivinha o número entre 1 e 20")
while tentativas > 0:
    numero = int(input("Insira o valor: "))
    if numero == numero_aleatorio:
        print(f"Parabéns,tu acertaste,{nome}!")
    elif numero > numero_aleatorio:
        print(f"Número incorreto, é inferior.")
        print(f"ainda lhe restam {tentativas} tentativas!")
    elif numero < numero_aleatorio:
        print("Número incorreto, é superior.")
tentativas -= 1
print(f"ainda lhe restam {tentativas} tentativas!")
print(f"Acabaram as tuas tentativas o numero correto era o {numero}!")
if escolha == "n":
    print("ok até a próxima")
exit()
