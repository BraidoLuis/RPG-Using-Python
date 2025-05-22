import random

vida_sandubinha = 5
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
    numero_secreto_monstro = random.randint(1, 3)
    numero_secreto_sandubinha = random.randint(1, vida_sandubinha)
    fortalecido = False
    historico_batalha = []

    def rodada_sandubinha():
        nonlocal vida_monstro
        n = 2 if fortalecido else numeros_sorteados_por_rodada
        numeros = [random.randint(1, 3) for _ in range(n)]
        dano = numero_secreto_monstro * numeros.count(numero_secreto_monstro)
        vida_monstro -= dano
        return ("Sandubinha", numeros, dano, numero_secreto_monstro)

    def rodada_monstro():
        nonlocal vida_sandubinha
        numeros = [random.randint(1, 5) for _ in range(numeros_sorteados_por_rodada)]
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
            print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir")
            escolha = input("Escolha sua acao: ")

            if escolha == "1":
                resultado = rodada_sandubinha()
                historico_batalha.append(resultado)
                turno = 1
            elif escolha == "2":
                if not inventario:
                    print("\nVocê não tem itens disponíveis agora.")
                    continue
                print("Seus itens:")
                for i, item in enumerate(inventario):
                    print(f"{i + 1}. {item}")
                    item_escolhido = input("Escolha o número do item para usar (ou pressione Enter para voltar): \n")
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
                print("\nVocê não tem itens equipados agora.")
            elif escolha == "4":
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
        
        return True, vida_sandubinha + 2
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
        numero_secreto_urso = random.randint(1, 6)
        numero_secreto_sandubinha = random.randint(1, vida_sandubinha)
        historico_batalha = []

        estado_original = {
        "guia": False,
        }

        def restaurar_estado():
            nonlocal guia
            guia = estado_original["guia"]
            print("\nTodos os efeitos de itens foram removidos. Sandubinha voltou ao estado normal.\n")

        def rodada_sandubinha():
                nonlocal vida_urso
                if guia:
                    n = 2
                else:
                    n = numeros_sorteados_por_rodada

                numeros = [random.randint(1, 6) for _ in range(n)]
                dano = numero_secreto_urso * numeros.count(numero_secreto_urso)
                vida_urso -= dano

                return ("Sandubinha", numeros, dano, numero_secreto_urso)

        def rodada_urso():
            nonlocal vida_sandubinha
            
            numeros = [random.randint(1, 7) for _ in range(numeros_sorteados_por_rodada_urso)]
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
                print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir\n")
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
                                guia = True
                            else:
                                print(f"Você usou {item}, mas nada aconteceu.")
                            turno = 1
                        else:
                            print("Item inválido.")
                    continue
                elif escolha == "3":
                    restaurar_estado()
                    print("Você desequipou seus itens.")
                    continue
                elif escolha == "4":
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
        
def narrativa_terceiroato():
    print("Uma vila mágica que recebe cobranças vindas das cavernas de Faturamentus. Os moradores entregam as mensagens na Torre")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha é bem recebido em sua chegada. Ele é convidado para um jantar ritualístico com comidas típicas")
    input("Pressione Enter para continuar...\n")

    print("Os moradores contam que o monstro a ser enfrentado é um ser que voa. Para atacá-lo, o Sandubinha terá que derrubar o monstro e usar sua espada.")
    print("Então, dão a ele um item, o [Estilingue mágico]")
    input("Pressione Enter para continuar...\n")

    print("Logo, um monstro em forma de dragão surge voando e diz:")
    print("Dragão da transmissão - Você já tem sua arma...já fui guardião dessas terras e transmitia as mensagens à torre.")
    print("Mas milênios atrás Glozium me tornou seu escravo, sou obrigado a lutar com toda fúria. Livre-me do sofrimento...")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Você também está preso a um destino que não escolheu, vou te libertar!")

def iniciar_batalha3(vida_sandubinha, inventario):
        vida_dragao = 12
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_dragao = 3
        guia = False
        faturamentus = False
        estilingue = False
        penalidade_faturamentus = False
        penalidade_estilingue = False
        atordoamento = False
        usoestilingue = 0
        historico_batalha = []
        numero_secreto_dragao = random.randint(1, 12)
        numero_secreto_sandubinha = random.randint(1, vida_sandubinha)

        estado_original = {
            "guia": guia, 
            "faturamentus": faturamentus,
            "estilingue": estilingue
        }

        def restaurar_estado():
            nonlocal guia, faturamentus, estilingue
            guia = estado_original["guia"]
            faturamentus = estado_original["faturamentus"]
            estilingue = estado_original["estilingue"]
            print("\nTodos os efeitos de itens foram removidos. Sandubinha voltou ao estado normal.\n")

        if "Estilingue mágico" not in inventario:
            print("\nVocê recebeu o item [Estilingue mágico] dos moradores\n")
            inventario.append("Estilingue mágico")


        def rodada_sandubinha():
            nonlocal vida_dragao, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento

            n = numeros_sorteados_por_rodada
            if guia:
                n = 2
            elif faturamentus:
                n = 4
            elif estilingue:
                n = int(vida_dragao/2) + numeros_sorteados_por_rodada
            else:
                n = numeros_sorteados_por_rodada            

            numeros = [random.randint(1, 12) for _ in range(n)]
            dano = numero_secreto_dragao * numeros.count(numero_secreto_dragao)
            vida_dragao -= dano

            if faturamentus and dano == 0:
                penalidade_faturamentus = True
                
            if estilingue:
                if dano == 0:
                    usoestilingue += 1
                    if usoestilingue > 3:
                        penalidade_estilingue = True
                        print("Você não pode usar o Estilingue mágico mais de 3 vezes, tomou um de dano.")
                        vida_sandubinha -= 1    
                elif dano > 0:
                        atordoamento = True
                        print("Você atordoou o Dragão!")
                        print("O Dragão não pode atacar nesta rodada!") 


            return ("Sandubinha", numeros, dano, numero_secreto_dragao)

        def rodada_dragao():
            nonlocal vida_sandubinha, penalidade_faturamentus, penalidade_estilingue, atordoamento
            numeros = [random.randint(1, 9) for _ in range(numeros_sorteados_por_rodada_dragao)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)

            if penalidade_faturamentus and dano > 0:
                print("O dragão aproveitou do seu erro e te deu mais dano que o normal!")
                dano += 2
            penalidade_faturamentus = False

            if penalidade_estilingue:
                print("O dragão ri de você após se acertar com o próprio estilingue!")

            if atordoamento:
                print("O Dragão não pode atacar nesta rodada!")
                atordoamento = False
                return ("Dragão", numeros, 0, numero_secreto_sandubinha)

            vida_sandubinha -= dano
            return ("Dragão", numeros, dano, numero_secreto_sandubinha)

        turno = 0

        while vida_dragao > 0 and vida_sandubinha > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_sandubinha}")
            print(f"Vida do Dragão: {vida_dragao}")

            if turno == 0:
                print("\n--- Sua vez ---\n")
                print("1. Atacar\n2. Itens\n3. Desistir\n")
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
                                print("Você usou o Guia de atendimento e se fortaleceu!\n")
                                guia = True
                                print("Você já usou o Guia de atendimento.\n")
                            elif item == "Faturamentus":
                                print("Você usou o Faturamentus e se fortaleceu!\n")
                                faturamentus = True
                                print("Você já usou o Faturamentus.\n")
                            elif item == "Estilingue mágico":
                                print("Você usou o Estilingue mágico e se fortaleceu!\n")
                                estilingue = True
                                print("Você já usou o Estilingue mágico.\n")
                            else:
                                print(f"Você usou {item}, mas nada aconteceu.\n")

                            turno = 1
                            
                        else:
                            print("Item inválido.")
                    continue                                                                 
                elif escolha == "3":
                    restaurar_estado()
                    print("Você desequipou seus itens.")
                elif escolha == "4":
                    print("Você desistiu da batalha!\n")
                    print("\nHistórico da batalha:")
                    for personagem, numeros, dano, numero_secreto in historico_batalha:
                        print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    return False, vida_sandubinha
                else:
                    print("Opção inválida!")
                    continue
            else:
                print("\n--- Turno do Dragão ---\n")
                resultado = rodada_dragao()
                historico_batalha.append(resultado)
                turno = 0

        if vida_dragao <= 0:
            print("\nVocê venceu! O Dragão foi derrotado!\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            input("Pressione Enter para continuar...\n")
            if "Azah Transmissão" not in inventario:
                print("\nSandubinha ganha o artefato [Azah Transmissão]\n")
                inventario.append("Azah Transmissão")
            print("\nMuito obrigado, todo herói evitava essa batalha e seguia para a torre, agora sou livre!")
            print("Evitva? E dá pra seguir sem lutar?? Como assim????\n")
            return True, vida_sandubinha + 2
        else:
            print("Você foi derrotado pelo Dragão...")
            input("Pressione Enter para continuar...\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            print("\nDragão - Sinto muito herói, que sua alma seja livre")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
            
            return False, vida_sandubinha

def main():

    venceu_primeira, vida_total = iniciar_batalha(vida_sandubinha, inventario_global)

    if venceu_primeira:
        narrativa_segundoato()
        venceu_segunda = iniciar_batalha2(vida_total, inventario_global)
        if venceu_segunda:
            narrativa_terceiroato()
            venceu_terceira, vida_total = iniciar_batalha3(vida_total, inventario_global)
            if venceu_terceira:
                print("🎉 Você venceu todas as batalhas! Parabéns, Sandubinha!")
                print("Você derrotou Glozium e salvou o mundo!")
                print("Fim de jogo. Obrigado por jogar!")
            else:
                print("Você foi derrotado na batalha final...")
                print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!")
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