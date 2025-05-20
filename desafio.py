import random

def narrativa_inicial():
    print("Sandubinha - Então você é meu primeiro desafio nessa floresta encantada?")
    input("Pressione Enter para continuar...\n")

    print("Monstro - Bem vindo, vejo que você é um dos escolhidos para enfraquecer Glozium,")
    print("meu nome é *Processus Ministerii*, sou o ser mágico que atende as almas feridas,")
    print("envio os informativos disso às cavernas de *Faturamentus*.") 
    input("Pressione Enter para continuar...\n")

    print("Processus - Você não irá lutar comigo, mas sim contra esse ser criado por Glozium.")
    print("Seres mágicos do meu tipo não podem ser afetados por Glozium,")
    print("mas também não podem lutar contra ele. Glozium me atrapalha,")
    print("me desconcentra e provoca erros.")
    input("Pressione Enter para continuar...\n")

    print('"Surge entre as pernas do grande monstro um ser humanóide, da altura de Sandubinha."')
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Primeiro, não é 'enfraquecer', vou dar um fim total em Glozium...")
    print("Venha monstro!")
    input("Pressione Enter para começar a batalha!\n")


def iniciar_batalha():
    vida_monstro = 3
    vida_sandubinha = 3
    numeros_sorteados_por_rodada = 1
    numero_secreto_monstro = random.randint(1, 3)
    numero_secreto_sandubinha = random.randint(1, 3)
    historico_batalha = []
    inventario = []

    def rodada_sandubinha():
        nonlocal vida_monstro
        numeros = [random.randint(1, vida_monstro) for _ in range(numeros_sorteados_por_rodada)]
        dano = numero_secreto_monstro * numeros.count(numero_secreto_monstro)
        vida_monstro -= dano
        return ("Sandubinha", numeros, dano, numero_secreto_monstro)

    def rodada_monstro():
        nonlocal vida_sandubinha
        numeros = [random.randint(1, vida_sandubinha) for _ in range(numeros_sorteados_por_rodada)]
        dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)
        vida_sandubinha -= dano
        return ("Monstro", numeros, dano, numero_secreto_sandubinha)

    narrativa_inicial()
    turno = 0  # Sandubinha começa

    while vida_monstro > 0 and vida_sandubinha > 0:
        print("\n--- STATUS ---")
        print(f"Vida do Sandubinha: {vida_sandubinha}")
        print(f"Vida do Monstro: {vida_monstro}")

        if turno == 0:
            print("\n--- Sua vez ---")
            print("1. Atacar\n2. Itens\n3. Desistir")
            escolha = input("Escolha sua ação: ")

            if escolha == "1":
                resultado = rodada_sandubinha()
                historico_batalha.append(resultado)
                turno = 1
            elif escolha == "2":
                if inventario:
                    print("Seus itens:")
                    for item in inventario:
                        print(f"- {item}")
                else:
                    print("Você não tem itens disponíveis agora.")
                continue
            elif escolha == "3":
                print("Você desistiu da batalha!")
                return
            else:
                print("Opção inválida!")
                continue
        else:
            print("\n--- Turno do Monstro ---")
            resultado = rodada_monstro()
            historico_batalha.append(resultado)
            turno = 0

    if vida_monstro <= 0:
        print("\nVocê venceu! O Monstro foi derrotado!")
        input("Pressione Enter para continuar...\n")
        print("\nProcessus Ministerii - Muito Obrigado, tome o artefato [Guia de atendimento] e vá para o próximo desafio")
        inventario.append("Guia de atendimento")
    else:
        print("\nVocê foi derrotado pelo Monstro...")
        input("Pressione Enter para continuar...\n")
        print("Processus Ministerii - Oh não, o mundo será mais uma vez destruído por Glozium")
        input("Pressione Enter para continuar...\n")
        print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!")

    print("\nHistórico da batalha:")
    for personagem, numeros, dano, numero_secreto in historico_batalha:
        print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")

    if inventario:
        print("\n--- Itens adquiridos ---")
        for item in inventario:
            print(f"- {item}")

    print("\nDeseja jogar novamente? (s/n)")
    jogar_novamente = input("> ")
    if jogar_novamente.lower() == "s":
        iniciar_batalha()
    else:
        print("Fim de jogo. Obrigado por jogar!")


# Início do jogo
iniciar_batalha()
