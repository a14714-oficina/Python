print("Bem-vindo à Floresta Encantada!") 
nome = input("Qual é o teu nome? ")  # Perguntar o nome do jogador
print(f"{nome}, queres jogar?")  # Pergunta se o jogador quer jogar
escolha = input("Sim (S) ou Não (N): ").lower()  # O jogador responde
if escolha == "s":
    print("OK, vamos a isso!")  # Confirma que o jogador quer jogar
elif escolha == "n":
    print("OK, obrigado!")  # Agradece e encerra o jogo
    exit()
print("Tu estás na Floresta Tropical!")  # Descrição do cenário inicial
direcao1 = input(f"{nome}, queres ir pela esquerda, pela direita ou pela frente? ")  # Perguntar a direção
if direcao1 == "esquerda":  # Se o jogador escolher a esquerda
    print("Tu andaste e encontraste um rio com animais selvagens. FIM DE JOGO!")  # O jogador perdeu!
    exit()
if direcao1 == "frente":  # Se o jogador escolher a frente
    print("Tu foste a andar por um caminho de terra.")  # Descrição da ação
else:
    if direcao1 == "direita":  # Se o jogador escolher a direita
        print("Tu encontraste uma gruta escura.")  # Nova descrição para a direita
        print("Queres entrar na gruta?")  # Pergunta se o jogador quer entrar
        escolha5 = input("Sim (S) ou Não (N): ").lower()  # Captura a resposta
        if escolha5 == "s":  # Se o jogador decide entrar na gruta
            print("Dentro da gruta, encontras um tesouro! Mas há um guardião.")
            print("Queres tentar pegar o tesouro?")  # Pergunta sobre pegar o tesouro
            escolha6 = input("Sim (S) ou Não (N): ").lower()  # O jogador responde
            if escolha6 == "s":  # Se o jogador tenta pegar o tesouro
                print("O guardião acordou e atacou-te! FIM DE JOGO!")  # Resultado negativo
                exit()
            else:
                print("Decidiste não pegar o tesouro e saíste da gruta.")  # Saída da gruta
                exit()
        else:
            print("Decidiste não entrar na gruta. Fim do jogo.")  # Se o jogador não entrar
            exit()
    else:
        print("Não encontraste nada de interessante. Fim do jogo.")  # Se o jogador não escolher uma direção válida
        exit()
print("Queres continuar a explorar o caminho?")  # Perguntar se o jogador quer continuar
escolha2 = input("Sim (S) ou Não (N): ").lower()  # Captura a resposta
if escolha2 == "s":
    print("Continuaste a andar e encontraste uma espada. Desejas pegá-la?")  
    escolha3 = input("Sim (S) ou Não (N): ").lower()  # Perguntar se o jogador quer pegar a espada
    if escolha3 == "s":  # Se o jogador pegar a espada
        print("Prepara-te, encontraste um Goblin Gigante!")  # Nova ameaça
        print("Queres atacar o Goblin gigante?")  # Pergunta sobre a ação
        escolha4 = input("Sim (S) ou Não (N): ").lower()  # Captura a resposta
        if escolha4 == "s":  # Se o jogador decide atacar
            print("MUITO BEM! Tu conseguiste matar o gigante. GANHASTE!")  # Vitória
            exit()
        elif escolha4 == "n":  # Se o jogador decide não atacar
            print("O Goblin gigante atacou-te e tu morreste! FIM DE JOGO!")  # Resultado negativo
            exit()
else:
    print("Decidiste não continuar. Fim do jogo.")  # Se o jogador não quiser continuar
