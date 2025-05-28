import random

def narrativa_terceiroato(inventario):
    print("\nUma vila mágica que recebe cobranças vindas das cavernas de Faturamentus. Os moradores entregam as mensagens na Torre")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha é bem recebido em sua chegada. Ele é convidado para um jantar ritualístico com comidas típicas")
    input("Pressione Enter para continuar...\n")

    print("Os moradores contam que o monstro a ser enfrentado é um ser que voa. Para atacá-lo, o Sandubinha terá que derrubar o monstro e usar sua espada.")
    print("Então, dão a ele um item, o [Estilingue mágico]")
    if "Estilingue mágico" not in inventario:
            print("\nVocê recebeu o item [Estilingue mágico] dos moradores\n")
            print("Formato: Estilingue")
            print("Esse artefato permite que você atordoe os inimigos por uma rodada, porém,")
            print("caso você erre o número secreto do oponente mais do que 3 vezes, você recebe 1 de dano a cada vez que você utiliza após isso.")
            inventario.append("Estilingue mágico")
    input("Pressione Enter para continuar...\n")

    print("Logo, um monstro em forma de dragão surge voando e diz:")
    print("Dragão da transmissão - Você já tem sua arma...já fui guardião dessas terras e transmitia as mensagens à torre.")
    print("Mas milênios atrás Glozium me tornou seu escravo, sou obrigado a lutar com toda fúria. Livre-me do sofrimento...")
    input("Pressione Enter para continuar...\n")

    print("Sandubinha - Você também está preso a um destino que não escolheu, vou te libertar!")
    input("Pressione Enter para começar a batalha")
    return inventario

def iniciar_batalha3(vida_sandubinha, inventario):
        vida_dragao = 12
        vida_atual = vida_sandubinha
        numeros_sorteados_por_rodada = 1
        numeros_sorteados_por_rodada_dragao = 3
        guia = False
        faturamentus = False
        estilingue = False
        penalidade_faturamentus = False
        penalidade_estilingue = False
        atordoamento = False
        usoestilingue = 0
        turnos_atordoados = 0
        historico_batalha = []
        numero_secreto_dragao = random.randint(1, 12)
        numero_secreto_sandubinha = random.randint(1, vida_atual)
        
    

        def listar_itens_equipados(): #Novos itens equipados
            itens_equipados = []
            if guia: itens_equipados.append("Guia de atendimento")
            if faturamentus: itens_equipados.append("Faturamentus")
            if estilingue: itens_equipados.append("Estilingue mágico")
            return itens_equipados
        
        

        def rodada_sandubinha():
            nonlocal vida_dragao, penalidade_faturamentus, usoestilingue, penalidade_estilingue, atordoamento,vida_atual, turnos_atordoados
            dano = 0
            n = numeros_sorteados_por_rodada
            numeros = [] # Adiciona uma lista vazia para não causar dano, antes de +3 usos

            if guia:
                n = 2
            if faturamentus:
                n = 4
            if estilingue:
                if not atordoamento: #Antes de atordoar, adiciona 1 aos usos
                    usoestilingue += 1
                    n = int(vida_dragao / 2)
                    numeros = [random.randint(1, 12) for _ in range(n)]
                    acertou_pedra = numero_secreto_dragao in numeros

                    if acertou_pedra: #Caso estilingue acerte, atordoa o dragão
                        print("Você acertou o Dragão com a pedra do Estilingue! Ele está atordoado e agora pode ser atingido!")
                        atordoamento = True
                        
                    else:
                        print(f"Você usou o Estilingue ({usoestilingue}/3), mas errou a pedra.") #Quantidade de usos do estilingue

                    if usoestilingue > 3: #Caso passe de 3 usos, perde 1 de vida
                        print("Você usou o Estilingue mais de 3 vezes e se feriu com o recuo! Perdeu 1 de vida.")
                        vida_atual -= 1
                        penalidade_estilingue = True
                        

                    return ("Sandubinha", numeros, 0, numero_secreto_dragao)
                else: #Dragão atordoado, pode receber dano
                    n = numeros_sorteados_por_rodada
                    if guia:
                        n = 2
                    if faturamentus:
                        n = 4
                    numeros = [random.randint(1, 12) for _ in range(n)]
                    dano = numero_secreto_dragao * numeros.count(numero_secreto_dragao)
                    vida_dragao -= dano
                    atordoamento = False
                    
            else:
                    # Sem estilingue — só pode causar dano se dragão já estiver atordoado
                numeros = [random.randint(1, 12) for _ in range(n)]
                if not atordoamento:
                    print("O Dragão está voando e invulnerável. Você precisa acertá-lo com o Estilingue primeiro!")
                    dano = 0
                else:
                    dano = numero_secreto_dragao * numeros.count(numero_secreto_dragao)
                    vida_dragao -= dano
                    atordoamento = False

            if faturamentus and dano == 0:
                penalidade_faturamentus = True

            return ("Sandubinha", numeros, dano, numero_secreto_dragao)

        def rodada_dragao():
            nonlocal vida_atual, penalidade_faturamentus, penalidade_estilingue, atordoamento, turnos_atordoados
            numeros = [random.randint(1, 9) for _ in range(numeros_sorteados_por_rodada_dragao)]
            dano = numero_secreto_sandubinha * numeros.count(numero_secreto_sandubinha)

            if atordoamento:
                turnos_atordoados += 1
                print("O Dragão está atordoado e não pode atacar nesta rodada!")
                if turnos_atordoados > 1:
                    print("O Dragão recuperou o fôlego pode atacar nesta rodada!")
                    atordoamento = False
                    turnos_atordoados = 0
                return ("Dragão", [], 0, numero_secreto_sandubinha)

            if penalidade_faturamentus and dano > 0:
                print("O dragão aproveitou do seu erro e te deu mais dano que o normal!")
                dano += 2
            penalidade_faturamentus = False #Penalidade é removida mesmo o dragão não causando dano

            if penalidade_estilingue:
                print("O dragão ri de você após se acertar com o próprio estilingue!")

            vida_atual -= dano
            return ("Dragão", numeros, dano, numero_secreto_sandubinha)

        turno = 0

        while vida_dragao > 0 and vida_atual > 0:
            print("\n--- STATUS ---\n")
            print(f"Vida do Sandubinha: {vida_atual}")
            print(f"Vida do Dragão: {vida_dragao}")

            if turno == 0:
                print("\n--- Sua vez ---\n")
                print("1. Atacar\n2. Itens\n3. Desequipar item\n4. Desistir\n")
                escolha = input("Escolha sua acao: ")

                if escolha == "1":
                    resultado = rodada_sandubinha()
                    historico_batalha.append(resultado)
                    personagem, numeros, dano, numero_secreto = resultado
                    print(f"\nVocê atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    if dano > 0:
                        print(f"Você causou {dano} de dano ao Dragão!")
                    else:
                        print("Seu ataque não causou dano ao Dragão.")
                    turno = 1
                elif escolha == "2":
                    item_usado = False
                    if not inventario:
                        print("Você não tem itens disponíveis agora.")
                        continue
                    print("Seus itens:")
                    for i, item in enumerate(inventario):
                        print(f"{i + 1}. {item}")
                    item_escolhido = input("Escolha o número do item para usar (ou pressione Enter para voltar): ")
                    if item_escolhido == "":
                        continue
                    if item_escolhido.isdigit():
                        index = int(item_escolhido) - 1
                        if 0 <= index < len(inventario):
                            item = inventario[index] 
                            if item == "Guia de atendimento":
                                if guia:
                                    print("Você já usou o Guia de atendimento.\n")
                                else :
                                    print("Você usou o Guia de atendimento e se fortaleceu!\n")
                                    guia = True
                                    item_usado = True
                            if item == "Faturamentus":
                                if faturamentus:
                                    print("Você já usou o Faturamentus.\n")
                                else: 
                                    print("Você usou o Faturamentus e se fortaleceu!\n")
                                    faturamentus = True
                                    item_usado = True
                                                                
                            if item == "Estilingue mágico":
                                if estilingue:
                                    print("Você já usou o Estilingue mágico.\n")
                                else:
                                    print("Você usou o Estilingue mágico e se fortaleceu!\n")
                                    estilingue = True
                                    item_usado = True
                    
                            if not any([guia, faturamentus, estilingue]):
                                print(f"Você usou {item}, mas nada aconteceu.\n")

                            if item_usado:
                                turno = 1
                            
                        else:
                            print("Item inválido.")
                    continue                                                                 
                elif escolha == "3":
                    itens_equipados = listar_itens_equipados()
                    if not itens_equipados:
                        print("Você não tem itens equipados no momento.")
                        continue
                    print("Itens equipados:")
                    for i, item in enumerate(itens_equipados):
                        print(f"{i + 1}. {item}")
                    escolha_item = input("Escolha o número do item que deseja desequipar (ou Enter para voltar): ").strip()
                    if escolha_item == "":
                        print("Você não escolheu nenhum item.")
                    if escolha_item.isdigit():
                        index = int(escolha_item) - 1
                        if 0 <= index < len(itens_equipados):
                            item = itens_equipados[index]
                            if item == "Guia de atendimento":
                                guia = False
                            elif item == "Faturamentus":
                                faturamentus = False
                            elif item == "Estilingue mágico":
                                estilingue = False
                            print(f"{item} foi desequipado com sucesso!")
                            turno = 1
                        else:
                            print("Escolha inválida!")
                        continue
                elif escolha == "4":
                    print("Você desistiu da batalha!\n")
                    print("\nHistórico da batalha:")
                    for personagem, numeros, dano, numero_secreto in historico_batalha:
                        print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                    return False, vida_atual
                else:
                    print("Opção inválida!")
                    continue
            else:
                print("\n--- Turno do Dragão ---\n")
                resultado = rodada_dragao()
                historico_batalha.append(resultado)
                personagem, numeros, dano, numero_secreto = resultado
                print(f"\nDragão atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
                if dano > 0:
                    print(f"{dano} recebido!")
                else:
                    print("Nenhum dano recebido.")
                turno = 0


        if vida_dragao <= 0:
            print("\nVocê venceu! O Dragão foi derrotado!\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            input("Pressione Enter para continuar...\n")
            if "Azah Transmissão" not in inventario:
                print("\nSandubinha ganha o artefato [Azah Transmissão]\n")
                print("Formato: Capa")
                print("Esse artefato permite que você sorteie 10 números por rodada, ao invés de um.")
                print("Porém, se você errar o número secreto do oponente, receberá o proximo dano proporcional do último número sorteado.")
                inventario.append("Azah Transmissão")
            print("\nDragão - Muito obrigado, todo herói evitava essa batalha e seguia para a torre, agora sou livre!")
            input("Pressione Enter para continuar...\n")
            print("Sandubinha - Evitava? E dá pra seguir sem lutar?? Como assim????\n")
            return True, vida_atual
        else:
            print("Você foi derrotado pelo Dragão...")
            input("Pressione Enter para continuar...\n")
            print("Histórico da batalha:\n")
            for personagem, numeros, dano, numero_secreto in historico_batalha:
                print(f"{personagem} atacou com os números {numeros} | Número secreto do oponente: {numero_secreto} | Dano causado: {dano}")
            print("\nDragão - Sinto muito herói, que sua alma seja livre")
            print("O mundo foi destruído por Glozium, uma fatalidade terrível... Fim de jogo!\n")
            
            return False, vida_atual