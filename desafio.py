import random

vida_total_sandubinha = 5
inventario_global = []

def narrativa_inicial():
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

def iniciar_batalha(vida_sandubinha, inventario):
    vida_monstro = 3
    numeros_sorteados_por_rodada = 1
    fortalecido = False
    historico_batalha = []

    def rodada_sandubinha():
        nonlocal vida_monstro
        numero_secreto_monstro = random.randint(1, 3)
        n = 2 if fortalecido else numeros_sorteados_por_rodada
        numeros = [random.randint(1, vida_monstro) for _ in range(n)]
        dano = numero_secreto_monstro * numeros.count(numero_secreto_monstro)
        vida_monstro -= dano
        return ("Sandubinha", numeros, dano, numero_secreto_monstro)

    def rodada_monstro():
        nonlocal vida_sandubinha
        numero_secreto_sandubinha = random.randint(1, vida_sandubinha)
        numeros = [random.randint(1, vida_sandubinha) for _ in range(numeros_sorteados_por_rodada)]
        dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)
        vida_sandubinha -= dano
        return ("Monstro", numeros, dano, numero_secreto_sandubinha)

    narrativa_inicial()
    turno = 0

    while vida_monstro > 0 and vida_sandubinha > 0:
        print("\n--- STATUS ---")
        print(f"Vida do Sandubinha: {vida_sandubinha}")
        print(f"Vida do Monstro: {vida_monstro}")

        if turno == 0:
            print("\n--- Sua vez ---")
            print("1. Atacar\n2. Itens\n3. Desistir")
            escolha = input("Escolha sua acao: ")

            if escolha == "1":
                resultado = rodada_sandubinha()
                historico_batalha.append(resultado)
                turno = 1
            elif escolha == "2":
                if not inventario:
                    print("Você não tem itens disponíveis agora.")
                    continue
                print("Seus itens:")
                for i, item in enumerate(inventario):
                    print(f"{i + 1}. {item}")
                item_escolhido = input("Escolha o número do item para usar (ou pressione Enter para voltar): ")
                if item_escolhido.isdigit():
                    index = int(item_escolhido) - 1
                    if 0 <= index < len(inventario):
                        item = inventario.pop(index)
                        if item == "Guia de atendimento":
                            print("Você usou o Guia de atendimento e se fortaleceu!")
                            fortalecido = True
                        else:
                            print(f"Você usou {item}, mas nada aconteceu.")
                    else:
                        print("Item inválido.")
                continue
            elif escolha == "3":
                print("Você desistiu da batalha!")
                print("\nHistórico da batalha:")
                for personagem, numeros, dano, numero_secreto in historico_batalha:
                    print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                return False, vida_sandubinha
            else:
                print("Opção inválida!")
                continue
        else:
            print("\n--- Turno do Monstro ---")
            resultado = rodada_monstro()
            historico_batalha.append(resultado)
            turno = 0

    if vida_monstro <= 0:
        print("\nVocê venceu! O Monstro foi derrotado!\n")
        print("Histórico da batalha:\n")
        for personagem, numeros, dano, numero_secreto in historico_batalha:
            print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
        input("Pressione Enter para continuar...\n")
        if "Guia de atendimento" not in inventario:
            print("\nProcessus Ministerii - Muito Obrigado, tome o artefato [Guia de atendimento] e vá para o próximo desafio\n")
            inventario.append("Guia de atendimento")
        
        return True, vida_total_sandubinha + 2
    else:
        print("Você foi derrotado pelo Monstro...")
        input("Pressione Enter para continuar...\n")
        print("Histórico da batalha:\n")
        for personagem, numeros, dano, numero_secreto in historico_batalha:
            print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
        print("\nProcessus Ministerii - Oh não, o mundo será mais uma vez destruído por Glozium")
        print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
        
        return False, vida_sandubinha
    
    

def narrativa_segundoato():
    print("\nVocê avançou para as Cavernas de Faturamentus...")
    input("Pressione Enter para continuar...\n")
    print("\nExiste sempre um preço a se pagar pela cura do corpo e da alma, após a floresta do atendimentus")
    print("seu preço é calculado de acordo com o tipo de contrato divino que você tem")
    input("Pressione Enter para continuar...\n")

    print("Percorrendo a caverna segurando uma tocha. Sandubinha escuta sons assustadores de grunhidos")
    input("Pressione Enter para continuar...\n")
    print("O cenário é iluminado por minérios misteriosos. Anciões fantasmas anotam diversas coisas em pergaminhos,")
    print("estão todos muito ocupados para falar algo a Sandubinha.")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Que tipo de situação é essa?")
    input("Pressione Enter para continuar...\n")
    print("Um monstro em forma de urso surge e diz a Sandubinha")
    input("Pressione Enter para continuar...\n")
    print("Urso Sangrento - Finalmente diversão, esses anciões só sabem ficar anotando essas coisas inúteis.")
    print("Vamos lutar heroizinho!")
    input("Pressione Enter para continuar...\n")
    print("Sandubinha - Criatura desagradável, não me deu tempo nem de tomar uma água, então bora nessa!")

def iniciar_batalha2(vida_sandubinha, inventario):
        vida_urso = 6
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_urso = 2
        fortalecido = False
        historico_batalha = []

        def rodada_sandubinha():
                nonlocal vida_urso
                numero_secreto_urso = random.randint(1, 6)
                n = 2 if fortalecido else numeros_sorteados_por_rodada
                numeros = [random.randint(1, vida_urso) for _ in range(n)]
                dano = numero_secreto_urso * numeros.count(numero_secreto_urso)
                vida_urso -= dano
                return ("Sandubinha", numeros, dano, numero_secreto_urso)

        def rodada_urso():
            nonlocal vida_sandubinha
            numero_secreto_sandubinha = random.randint(1, vida_sandubinha)
            numeros = [random.randint(1, vida_sandubinha) for _ in range(numeros_sorteados_por_rodada_urso)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)
            vida_sandubinha -= dano
            return ("Urso", numeros, dano, numero_secreto_sandubinha)
        
        turno = 0

        while vida_urso > 0 and vida_sandubinha > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_sandubinha}")
            print(f"Vida do Urso: {vida_urso}")

            if turno == 0:
                print("\n--- Sua vez ---")
                print("1. Atacar\n2. Itens\n3. Desistir")
                escolha = input("Escolha sua ação: ")

                if escolha == "1":
                    resultado = rodada_sandubinha()
                    historico_batalha.append(resultado)
                    turno = 1
                elif escolha == "2":
                    if not inventario:
                        print("Você não tem itens disponíveis agora.")
                        continue
                    print("Seus itens:")
                    for i, item in enumerate(inventario):
                        print(f"{i + 1}. {item}")
                    item_escolhido = input("Escolha o número do item para usar (ou pressione Enter para voltar): ")
                    if item_escolhido.isdigit():
                        index = int(item_escolhido) - 1
                        if 0 <= index < len(inventario):
                            item = inventario.pop(index)
                            if item == "Guia de atendimento":
                                print("Você usou o Guia de atendimento e se fortaleceu!")
                                fortalecido = True
                            else:
                                print(f"Você usou {item}, mas nada aconteceu.")
                        else:
                            print("Item inválido.")
                    continue
                elif escolha == "3":
                    print("Você desistiu da batalha!")
                    for personagem, numeros, dano, numero_secreto in historico_batalha:
                        print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    return False
                else:
                    print("Opção inválida!")
                    continue
            else:
                print("\n--- Turno do Urso ---")
                resultado = rodada_urso()
                historico_batalha.append(resultado)
                turno = 0

        if vida_urso <= 0:
            print("\nVocê venceu! O Urso foi derrotado!")
            input("Pressione Enter para continuar...\n")
            print("Ancião faturador - Muito obrigado, mas tô ocupado demais para agradecimentos longos, tome o artegato sagrado e siga em frente\n")
            if "Faturamentus" not in inventario:
                print("Sandubinha ganha o artefato [Faturamentus] e o coloca no inventário.\n")
                inventario.append("Faturamentus")
            print("Histórico da batalha:")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            
            return True
            
        else:
            print("\nVocê foi derrotado pelo Urso...")
            input("Pressione Enter para continuar...\n")
            print("Ancião faturador - Herói merda, nem para cumprir o trabalho dele, estamos perdidos\n")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!")
            print("Histórico da batalha:")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            return False

def main():

    venceu_primeira, vida_total = iniciar_batalha(vida_total_sandubinha, inventario_global)

    if venceu_primeira:
        narrativa_segundoato()
        venceu_segunda = iniciar_batalha2(vida_total, inventario_global)
        if venceu_segunda:
            print("🎉 Você venceu as duas batalhas! Prepare-se para o próximo desafio.")
        else:
            print("\nDeseja jogar novamente? (s/n)")
            if input("> ").lower() == "s":
                main()
            else:
                print("Fim de jogo. Obrigado por jogar!")
    else:
        print("\nDeseja jogar novamente? (s/n)")
        if input("> ").lower() == "s":
            main()
        else:
            print("Fim de jogo. Obrigado por jogar!")


# Início do jogo
main()