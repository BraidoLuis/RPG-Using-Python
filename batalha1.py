import random

def narrativa_inicial():  #Narrativa do primeiro ato
    print("Sandubinha - Então você é meu primeiro desafio nessa floresta encantada?\n")
    input("Pressione Enter para continuar...\n")

    print("Monstro - Bem vindo, vejo que você é um dos escolhidos para enfraquecer Glozium,")
    print("meu nome é *Processus Ministerii*, sou o ser mágico que atende as almas feridas,")
    print("envio os informativos disso às cavernas de *Faturamentus*.\n") 
    input("Pressione Enter para continuar...\n")

    print("Processus - Você não irá lutar comigo, mas sim contra esse ser criado por Glozium.")
    print("Seres mágicos do meu tipo não podem ser afetados por Glozium,")
    print("mas também não podem lutar contra ele. Glozium me atrapalha,")
    print("me desconcentra e provoca erros.\n")
    input("Pressione Enter para continuar...\n")

    print("Surge entre as pernas do grande monstro um ser humanóide, da altura de Sandubinha.\n")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Primeiro, não é 'enfraquecer', vou dar um fim total em Glozium...")
    print("Venha monstro!\n")
    input("Pressione Enter para começar a batalha!\n")

def iniciar_batalha(vida_sandubinha, inventario): #Batalha do primeiro ato
    vida_monstro = 3
    vida_atual = vida_sandubinha
    numeros_sorteados_por_rodada = 1
    numero_secreto_monstro = random.randint(1, 3) #randint = Função para calcular valores num intervalo definido
    numero_secreto_sandubinha = random.randint(1, vida_sandubinha)
    historico_batalha = []

    def rodada_sandubinha():
        nonlocal vida_monstro
        n = numeros_sorteados_por_rodada
        numeros = [random.randint(1, 3) for _ in range(n)]
        dano = numero_secreto_monstro * numeros.count(numero_secreto_monstro)
        vida_monstro -= dano
        return ("Sandubinha", numeros, dano, numero_secreto_monstro)

    def rodada_monstro():
        nonlocal vida_atual
        numeros = [random.randint(1, 5) for _ in range(numeros_sorteados_por_rodada)]
        dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)
        vida_atual -= dano
        return ("Monstro", numeros, dano, numero_secreto_sandubinha)

    turno = 0

    while vida_monstro > 0 and vida_atual > 0:
        print("\n--- STATUS ---")
        print(f"Vida do Sandubinha: {vida_atual}")
        print(f"Vida do Monstro: {vida_monstro}")

        if turno == 0:
            print("\n--- Sua vez ---")
            print("1. Atacar\n2. Desistir")
            escolha = input("Escolha sua acao: ")

            if escolha == "1":
                resultado = rodada_sandubinha()
                historico_batalha.append(resultado) #Adiciona o resultado da batalha no histórico
                personagem, numeros, dano, numero_secreto = resultado
                print(f"\nVocê atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                if dano > 0:
                    print(f"Você causou {dano} de dano ao monstro!")
                else:
                    print("Seu ataque não causou dano ao monstro.")
                turno = 1
                
            elif escolha == "2":
                print("Você desistiu da batalha!")
                print("\nHistórico da batalha:")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                return False, vida_atual 
                
            else:
                print("Opção inválida!")
                continue
        else:
            print("\n--- Turno do Monstro ---")
            resultado = rodada_monstro()
            historico_batalha.append(resultado)
            personagem, numeros, dano, numero_secreto = resultado
            print(f"\nMonstro atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            if dano > 0:
                print(f" {dano} recebido!")
            else:
                print("Nenhum dano recebido.")
                    
            turno = 0

    if vida_monstro <= 0:
        print("\nVocê venceu! O Monstro foi derrotado!\n")
        input("Pressione Enter para continuar...\n")
        print("Histórico da batalha:\n")
        for personagem, numeros, dano, numero_secreto in historico_batalha:
            print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
        input("Pressione Enter para continuar...\n")
        if "Guia de atendimento" not in inventario: #Adiciona Guia de atendimento aos itens
            print("Formato: Pergaminho")
            print("\nProcessus Ministerii - Muito Obrigado, tome o artefato [Guia de atendimento] e vá para o próximo desafio")
            print("Esse artefato permite que você sorteie dois números por rodada, ao invés de um")
            inventario.append("Guia de atendimento")
        
        return True, vida_atual
    else:
        print("\nVocê foi derrotado pelo Monstro...")
        input("Pressione Enter para continuar...\n")
        print("Histórico da batalha:\n")
        for personagem, numeros, dano, numero_secreto in historico_batalha:
            print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
        print("\nProcessus Ministerii - Oh não, o mundo será mais uma vez destruído por Glozium")
        print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
        
        return False, vida_atual